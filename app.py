# -*- coding: utf_8 -*-
# coding: UTF-8
from bottle import get, route, run, template, static_file, request, redirect, response, view, url, hook, post
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import message
from email import charset
import email
import base64
import smtplib
import os
import stripe

from models.app_setting import session
from models.user import User
from models.tweet import Tweet
from models.tweet_comment import Tweet_comment
from models.img import Img
from models.follow import Follow
from models.fab import Fab
from models.pro_comment import Comment
from models.social import Social
from models.follow_comment import Follow_comment

from library import *

import models.app_setting

import requests

import sys

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from apiclient.discovery import build
import httplib2

@hook('before_request')
def before_action():
        global current_user
        current_user = get_current_user()

@hook('after_request')
def close_db_session():
        session.close()

@route("/static/:path#.+#", name='static')
def test(path):
    return static_file(path, root='static')

@route("/TextInputEffects/:path#.+#", name='static')
def test(path):
    return static_file(path, root='TextInputEffects')

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/img")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@route("/", method='GET')
def top():

    current_user = get_current_user()
    stripe_cookie = get_stripe_cookie()

    return template("templates/tatume" , current_user=current_user, stripe_cookie=stripe_cookie)

@route("/", method='POST')
def login():

    current_user = get_current_user()

    if authenticate(request.POST):
        redirect('/tweet')
    else:
        redirect('/')

@route('/facebook/login')
def facebook_login():

    script_cookie = get_stripe_cookie()

    if script_cookie is None:
        redirect('/pay')
    else:
        url = 'https://www.facebook.com/dialog/oauth'
        params = {
            'response_type': 'code',
            'redirect_uri': models.app_setting.FACEBOOK_CALLBACK_URL,
            'client_id': models.app_setting.FACEBOOK_ID
        }

        redirect_url = requests.get(url, params=params).url
        redirect(redirect_url)

@route('/facebook/callback')
def facebook_callback():
    # try: # 予期せぬエラーがでたらログイン画面にリダイレクトする
    if request.GET.getunicode('code'):
        access_token = get_facebook_access_token(request.GET.getunicode('code'))
        data = check_facebook_access_tokn(access_token)
        if data['is_valid']:
            data = get_facebook_user_info(access_token, data['user_id'])
            if check_socials(data, 'facebook'):
                social = session.query(User.name).join(
                         Social, User.id == Social.user_id).filter(
                         Social.provider == 'google',
                         Social.provider_id == data).first()
                if social is None:
                    redirect('/mypage')
                else:
                    redirect('/tweet')
            else:
                user = create_facebook_user(data)
                create_socials(user, data, 'facebook')
                login_user(user.id)
                # send_mail(data['email'], 'create')
                redirect('/tweet')
        else:
        	# アクセストークンが不正なものだったらログイン画面にリダイレクトする
            redirect('/')
    else:
        redirect('/')
    # except:
    #     redirect('/')

@route('/google/login')
def google_login():

    SCOPE = 'https://www.googleapis.com/auth/plus.login'

    flow = flow_from_clientsecrets(
       './client_id.json',
       scope=SCOPE,
       redirect_uri= "http://localhost:5000/google/callback")

    auth_uri = flow.step1_get_authorize_url()

    redirect(auth_uri)

@route('/google/callback')
def google_callback():

    # try:
    if request.GET.getunicode('code'):
        data = google_login_flow(request.GET.getunicode('code'))
        check = check_socials(data, 'google')
        if check is not False:
            social = session.query(User.name).join(
                     Social, User.id == Social.user_id).filter(
                     Social.provider == 'google',
                     Social.provider_id == data).first()

            if social is None:
                redirect('/mypage')
            else:
                redirect('/tweet')
        else:
            user = create_google_user()
            create_socials(user, data, 'google')
            login_user(user.id)
            redirect('/mypage')
    else:
        redirect('/')
    # except:
        # redirect('/')


@route('/twitter/login')
def facebook_login():

    test = get_twitter_access_token()

    return test
# 
# @route('/twitter/callback')
# def facebook_callback():
#     # try: # 予期せぬエラーがでたらログイン画面にリダイレクトする
#     if request.GET.getunicode('code'):
#         access_token = get_twitter_access_token(request.GET.getunicode('code'))
#         data = check_twitter_access_tokn(access_token)
#         if data['is_valid']:
#             data = get_facebook_user_info(access_token, data['user_id'])
#             if check_socials(data, 'facebook'):
#                 social = session.query(User.name).join(
#                          Social, User.id == Social.user_id).filter(
#                          Social.provider == 'google',
#                          Social.provider_id == data).first()
#                 if social is None:
#                     redirect('/mypage')
#                 else:
#                     redirect('/tweet')
#             else:
#                 user = create_facebook_user(data)
#                 create_socials(user, data, 'facebook')
#                 login_user(user.id)
#                 # send_mail(data['email'], 'create')
#                 redirect('/tweet')
#         else:
#         	# アクセストークンが不正なものだったらログイン画面にリダイレクトする
#             redirect('/')
#     else:
#         redirect('/')
#

@route('/remake_password')
def remake():

    duplicate_error = ''
    return template('templates/remake_password', duplicate_error=duplicate_error)

@route('/check_email')
def email():

    return template('templates/check_email')

@route('/remake_password', method='POST')
def remake_password():

    remake_mail = remake_password_email(request.POST)

    if remake is False:
        duplicate_error='登録したEmailを入力してください。'
        return template('templates/remake_password', duplicate_error=duplicate_error)
    else:
        remake_check_mail(remake_mail, 'remake', remake_mail)
        redirect('/check_email')

@route('/remake/<mail_id>/<mail>')
def update_password(mail_id ,mail):

    duplicate_error= ''
    check_mail_accuount = url_check(mail_id, mail, get_stripe_cookie())
    if check_mail_accuount is True:
        if get_stripe_cookie() is not None:
            return template('templates/remake', mail=mail, mail_id=mail_id, duplicate_error=duplicate_error)
        else:
            redirect('/')
    else:
        redirect('/')

@route('/remake/<mail_id>/<mail>', method='POST')
def update_password(mail_id, mail):

    stripe_id_check = get_current_stripe_id_check()
    if stripe_id_check is True:
        checker = password_checker(request.POST)
        if checker is True:
            remake_password_check(mail, request.POST, get_stripe_cookie() )
            redirect('/check_password')
        else:
            duplicate_error = 'パスワードは確認用と同様の内容を記述してください。'
            return template('templates/remake', duplicate_error=duplicate_error, mail=mail, mail_id=mail_id)
    else:
        redirect('/pay')

@route("/check_password")
def check_password():

    return template('templates/check_password')

@route("/logout")
def logout():

    current_user = get_current_user()
    logout = logout_user()

    return template('templates/logout', current_user=current_user, logout=logout)

@route("/pay")
def pay():

    return template('templates/pay', publishable_key=models.app_setting.STRIPE_PUBLISHABLE)

@route("/pay/charge", method='POST')
def pay_commit():

    customer = stripe.Customer.create(
        email = request.POST.getunicode('stripeEmail'),
        source = request.POST.getunicode('stripeToken')
    )

    set_stripe_id(customer.id, customer.email)
    login_stripe_id(customer.id)

    charge = stripe.Charge.create(
         customer = customer.id,
         amount = request.POST.getunicode('amount'),
         currency = 'jpy',
         description = request.POST.getunicode('description')
    )

    stripe_create_mail(request.POST.getunicode('stripeEmail'), customer.id, 'pay')

    return template('templates/pay_after', current_user=current_user)

@route("/user/<user_account_email>/<stripe_id>")
def user_account_email_redirect(user_account_email, stripe_id):

    check = check_account_payafter(user_account_email, stripe_id)

    if check is True:
        redirect('/create')
    else:
        redirect('/pay')

@route('/check_account')
def check_account():

    duplicate_error = ''
    return template('templates/check_account', duplicate_error=duplicate_error)

@route('/check_account', method='POST')
def check_account_email():

    check_account = check_email_stripe_id(request.POST)

    if check_account is not False:
        login_stripe_id(check_account)
        redirect('/create')
    else:
        duplicate_error = '登録したEmailアドレスを入力してください。'
        return template('templates/check_account', duplicate_error=duplicate_error)

@route("/create", method='GET')
def create_get():

    stripe_id = get_current_stripe_id()

    if stripe_id is None:
        redirect('/pay')
    else:
        current_user = get_current_user()
        user_stripe_delete()
        duplicate_error = ''
        return template('templates/create', current_user=current_user, duplicate_error=duplicate_error)

@route('/check', method='POST')
def users_new_confirm():

    current_user = get_current_user()
    user =  User(
               name = request.POST.getunicode('name'),
               email = request.POST.getunicode('email'),
               password = request.POST.getunicode('password')
          )
    if is_duplicate_email(user.email) and is_duplicate_name(user.name):
        duplicate_error = '既に登録されているメールアドレス、ユーザー名です。'
        return template('templates/create', url=url, user=user, current_user=current_user, duplicate_error=duplicate_error, view=view)
    elif is_duplicate_email(user.email):
        duplicate_error = '既に登録されているメールアドレスです。'
        return template('templates/create', url=url, user=user, current_user=current_user, duplicate_error=duplicate_error, view=view)
    elif is_duplicate_name(user.name):
        duplicate_error = '既に登録されているユーザ名です。'
        return template('templates/create', url=url, user=user, current_user=current_user, duplicate_error=duplicate_error, view=view)

    return template('templates/check', current_user=current_user, user=user)

@route('/create', method='POST')
def create():
    current_user = get_current_user()
    user = create_user(request.POST)
    login_user(user.id)
    send_mail(user.email, 'create')
    duplicate_error = '登録完了しました。'
    # return template('templates/create_after', user=user, current_user=current_user , duplicate_error=duplicate_error)

    return template('templates/create_after', duplicate_error=duplicate_error, current_user=current_user)

@route("/user/delete/<user_id>")
def delete_user(user_id):

    delete_user = delete_check(request.POST)
    mail = delete_mail()
    mail = mail[0][0]
    if delete_user is True:
        send_mail(mail, 'delete')
        delete_account()
        logout_user()
        redirect('/')
    else:
        redirect('/mypage')

@route("/info")
def info():

    current_user = get_current_user()
    stripe_cookie = get_stripe_cookie()
    return template('templates/info', url=url, current_user=current_user, stripe_cookie=stripe_cookie)

@route('/tweet')
def tweet():

    current_user = get_current_user()
    tweets = tweet_view()
    follow_check = follow_id_view()
    fab_check = fab_check_view()
    is_logged_in_redirect(current_user)

    return template('templates/tweet', follow_view=follow_check, fab_check=fab_check, tweets=tweets, current_user=current_user)

@route('/tweet', method='POST')
def tweer_db():

    current_user = get_current_user()
    tweet_comment = tweet_create(request.forms)
    img = img_table(request.forms)
    tweet_db = tweet_table(request.forms)
    tweets = tweet_view()
    follow_check = follow_id_view()
    fab_check = fab_check_view()

    return template('templates/tweet',follow_view=follow_check ,fab_check=fab_check, tweet_comment=tweet_comment, tweets=tweets, tweet=tweet_db, img=img_table, current_user=current_user)

@route('/follower')
def follower():

    current_user = get_current_user()
    follower_view_table = follower_view()
    is_logged_in_redirect(current_user)

    return template('templates/follower', current_user=current_user, follower_view_table=follower_view_table)

@route('/follow/<user_follow:int>')
def follow(user_follow):

    current_user = get_current_user()
    follow_user = follow_table(user_follow)
    is_logged_in_redirect(current_user)

    return follow_user

@route('/follow/delete/<delete_follower_id:int>')
def delete_follower_id(delete_follower_id):

    delete = delete_follower(delete_follower_id)
    is_logged_in_redirect(current_user)

    return delete

@route('/fab')
def fab_test():

    current_user = get_current_user()
    tweets = fab_view()
    follow_check = follow_id_view()
    fab_check = fab_check_view()
    is_logged_in_redirect(current_user)

    return template('templates/fab', current_user=current_user, tweets=tweets, fab_check=fab_check, follow_check=follow_check)

@route('/fab/<fab_id:int>')
def fab(fab_id):

    fab = fab_table(fab_id)
    is_logged_in_redirect(current_user)

    return fab

@route('/fab/delete/<fab_id:int>')
def fab(fab_id):

    delete = fab_delete(fab_id)
    is_logged_in_redirect(current_user)

    return delete

@route('/search')
def view():

    tweets = tweet_view()
    current_user = get_current_user()
    follow_check = follow_id_view()
    fab_check = fab_check_view()
    is_logged_in_redirect(current_user)
    test = ''

    return template('templates/search', fab_check=fab_check, follow_check=follow_check, tweets=tweets, test=test, current_user=current_user)

@route('/search', method='POST')
def search():

    search = tweet_search(request.POST)
    follow_check = follow_id_view()
    fab_check = fab_check_view()
    current_user = get_current_user()
    is_logged_in_redirect(current_user)

    if search is not False:
        test=''
        tweets = search
        return template("templates/search", follow_check=follow_check, fab_check=fab_check, search=search, test=test, current_user=current_user, tweets=tweets)
    else:
        test = 'キーワードを入力してください。'
        tweets = tweet_view()
        return template("templates/search", follow_check=follow_check, fab_check=fab_check, tweets=tweets, test=test, current_user=current_user)

@route('/mypage')
def profile():

    current_user = get_current_user()
    user_account = loggedin_account()
    user_account = user_account[0][0]
    my_tweets = my_tweet()
    profile = my_profile()
    error=''
    is_logged_in_redirect(current_user)

    return template('templates/mypage', error=error, user_account=user_account, my_tweets=my_tweets, current_user=current_user, profile=profile)

@route('/edit')
def edit():

    current_user = get_current_user()
    profile_view = comment()
    error = ''
    is_logged_in_redirect(current_user)

    return template('templates/profile_remake', current_user=current_user, profile_view=profile_view, error=error)

@route('/edit', method='POST')
def edit_post():

    current_user = get_current_user()
    edit = profile_edit(request.POST)
    if edit is False:
        commit_text = '既に使用されているメールアドレスです。'
        profile_view = comment()
        return template('templates/profile_remake', current_user=current_user, edit=edit, error=commit_text, profile_view=profile_view)
    else:
        test_edit = my_comment(request.forms)
        profile_view = comment()
        commit_text = commit()
        return template('templates/profile_remake', current_user=current_user, edit=edit, profile_view=profile_view, error=commit_text, test_edit=test_edit)

@route('/mypage/delete/<delete_id>')
def delete_tweet(delete_id):

    current_user = get_current_user()
    delete_tweet = delete(delete_id)
    is_logged_in_redirect(current_user)

    return redirect('/mypage')

@route('/mypage/edit/<tweet_edit_id>')
def tweet_edit(tweet_edit_id):

    current_user = get_current_user()
    mytweet_edit = my_tweet_edit(tweet_edit_id)
    mytweet_edit = mytweet_edit[0][0]
    is_logged_in_redirect(current_user)

    return template('templates/mytweet_edit', current_user=current_user, tweet_edit_id=tweet_edit_id, mytweet_edit=mytweet_edit)

@route('/mypage/edit/<tweet_edit_id>', method='POST')
def tweet_edit_input(tweet_edit_id):

    current_user = get_current_user()
    tweet_input = my_tweet_edit_input(tweet_edit_id)
    is_logged_in_redirect(current_user)

    return redirect('/mypage')

@route('/users/profile/<user_id_number>')
def users_profile(user_id_number):

    current_user = get_current_user()
    tweet = users_tweet(user_id_number)
    profile = user_profile(user_id_number)
    fab_check = fab_check_view()
    follow_check = follow_id_view()
    is_logged_in_redirect(current_user)

    return template('templates/users/profile', follow_check=follow_check, fab_check=fab_check, user_id_number=user_id_number, current_user=current_user, user_profile=profile, user_tweets=tweet)


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
