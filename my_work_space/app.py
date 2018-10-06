# -*- coding: utf_8 -*-
# coding: UTF-8
from bottle import get, route, run, template, static_file, request, redirect, response, view, url, hook
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
from models.user import *
from models.tweet import *
from models.tweet_comment import *
from models.img import *
from models.follow import *
from models.fab import *
from models.pro_comment import *
from models.social import *
from models.follow_comment import *

from library import *

import models.app_setting

import requests

import sys

@hook('before_request')
def before_action():
        global current_user
        current_user = get_current_user()

@hook('after_request')
def close_db_session():
        session.close()

#
# stripe_keys = {
#   'secret_key': os.environ['SECRET_KEY'],
#   'publishable_key': os.environ['PUBLISHABLE_KEY']
# }
#
# stripe.api_key = stripe_keys['secret_key']

def test():

    if request.urlparts.path == 'https://webapp2-heroku.herokuapp.com':
        url = request.urlparts.path.replace('https://webapp2-heroku.herokuapp.com', 'https://www.webapp2.com', 1)
        code = 301
        return redirect(url, code=code)


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
    is_logged_in_redirect(current_user)

    return template("templates/tatume" , current_user=current_user)

@route("/", method='POST')
def login():
    current_user = get_current_user()
    is_logged_in_redirect(current_user)

    if authenticate(request.POST):
        redirect('/tweet')
    else:
        return template('templates/tatume', current_user=current_user)


@route('/facebook/login', method='GET')
def facebok_login():
        """
        ユーザーにFacebookアプリに情報取得許可のログインをしてもらう
        ログイン成功後 code というデータとともにリダイレクトされる
        """
        url = 'https://www.facebook.com/dialog/oauth'
        params = {
                'response_type': 'code',
                'redirect_uri': models.app_setting.FACEBOOK_CALLBACK_URL,
                'client_id': models.app_setting.FACEBOOK_ID,
        }
        redirect_url = requests.get(url, params=params).url
        redirect(redirect_url)


@route('/facebook/callback')
def facebook_callback():
    try: # 予期せぬエラーがでたらログイン画面にリダイレクトする
        if request.GET.getunicode('code'):
            """
            リダイレクトと同時に送られてきたcodeを用いてアクセストークンを取得
            """
            url = 'https://graph.facebook.com/v3.1/oauth/access_token'
            params = {
                    'redirect_uri': models.app_setting.FACEBOOK_CALLBACK_URL,
                    'client_id': models.app_setting.FACEBOOK_ID,
                    'client_secret': models.app_setting.FACEBOOK_SECRET,
                    'code': request.GET.getunicode('code'),
            }
            r = requests.get(url, params=params)
            access_token = r.json()['access_token']
            print(access_token)

            """
            取得したアクセストークンが不正じゃないか確認する
            """
            url = 'https://graph.facebook.com/debug_token'
            params = {
                'input_token': access_token,
                'access_token': '%s|%s' % (models.app_setting.FACEBOOK_ID, models.app_setting.FACEBOOK_SECRET)
            }
            r = requests.get(url, params=params)

            if r.json()['data']['is_valid']:
                """
				アクセストークンが不正じゃないことがわかったら
				アクセストークンをもとにユーザーの情報を取得する
				"""
                url = 'https://graph.facebook.com/%s' % (r.json()['data']['user_id'])
                params = {
                    'fields': 'name,email',
                    'access_token': access_token,
                }
                r = requests.get(url, params=params)
                return r.json()
            else:
    			# アクセストークンが不正なものだったらログイン画面にリダイレクトする
                redirect('/')

    except:
        redirect('/')

# @route('/facebook/login')
# def facebook_login():
#
#     url = 'https://www.facebook.com/dialog/oauth'
#     params = {
#         'response_type': 'code',
#         'redirect_uri': models.app_setting.FACEBOOK_CALLBACK_URL,
#         'client_id': models.app_setting.FACEBOOK_ID
#     }
#
#     redirect_url = requests.get(url, params=params).url
#     # print('r.url:', r.url)
#     # print('r: ', vars(r))
#     # return r.url
#     # redirect_url = r.url
#
#     redirect(redirect_url)
#
# @route('/facebook/callback')
# def facebook_callback():
#     try: # 予期せぬエラーがでたらログイン画面にリダイレクトする
#         if request.GET.getunicode('code'):
#
#             access_token = get_facebook_access_token(request.GET.getunicode('code'))
#             print(access_token)
#             data = check_facebook_access_tokn(access_token)
#
#             if data['is_valid']:
#                 data = get_facebook_user_info(access_token, data['user_id'])
#                 if check_socials(data, 'facebook'):
#                     redirect('/tweet')
#                 else:
#                     user = create_facebook_user()
#                     create_socials(user, data, 'facebook')
#                     login_user(user.id)
#                     redirect('/tweet')
#             else:
#         		# アクセストークンが不正なものだったらログイン画面にリダイレクトする
#                 redirect('/')
#
#     except:
#         redirect('/')

@route("/logout")
def logout():

    current_user = get_current_user()
    logout = logout_user()

    return template('templates/logout', current_user=current_user, logout=logout)

@route("/create", method='GET')
def create_get():

    current_user = get_current_user()
    is_logged_in_redirect(current_user)
    duplicate_error = ''

    return template('templates/create', duplicate_error=duplicate_error, user=User(), current_user=current_user)

@route('/check', method='POST')
def users_new_confirm():

    current_user = get_current_user()
    is_logged_in_redirect(current_user)
    user = User(
            email = request.POST.getunicode('email'),
            password = request.POST.getunicode('password'),
            name = request.POST.getunicode('name')
    )

    if is_duplicate_email(user.email):
        duplicate_error = '既に登録されているメールアドレスです。'
        return template('templates/create', url=url, user=user, current_user=current_user, duplicate_error=duplicate_error)

    return template('templates/check', current_user=current_user, user=user)

@route('/create', method='POST')
def create():
    current_user = get_current_user()
    is_logged_in_redirect(current_user)
    user = create_user(request.POST)
    duplicate_error = '登録完了しました。'

    return template('templates/create_after', user=user, current_user=current_user , duplicate_error=duplicate_error)

@route("/info")
def info():

    current_user = get_current_user()

    return template('templates/info', url=url, current_user=current_user)

@route('/tweet', method='GET')
def tweet():

    current_user = get_current_user()
    tweets = tweet_view()
    follow_check = follow_id_view()
    fab_check = fab_check_view()

    return template('templates/tweet', follow_view=follow_check, fab_check=fab_check, tweets=tweets, current_user=current_user)

@route('/tweet', method='POST')
def tweer_db():

    current_user = get_current_user()
    tweet_comment = tweet_create(request.forms)
    img = img_table(request.forms)
    tweet_db = tweet_table(request.forms)
    tweets = tweet_view()
    comment = 'フォローする'

    return template('templates/tweet', tweet_comment=tweet_comment, tweets=tweets, tweet=tweet_db, img=img_table, current_user=current_user, comment=comment)

@route('/follower')
def follower():

    current_user = get_current_user()
    follower_view_table = follower_view()

    return template('templates/follower', current_user=current_user, follower_view_table=follower_view_table)

@route('/follow/<user_follow:int>')
def follow(user_follow):

    follow_user = follow_table(user_follow)

    return follow_user

@route('/follow/delete/<delete_follower_id:int>')
def delete_follower_id(delete_follower_id):

    delete = delete_follower(delete_follower_id)

    return delete

@route('/fab')
def fab_test():

    current_user = get_current_user()
    tweets = fab_view()
    follow_check = follow_id_view()
    fab_check = fab_check_view()

    return template('templates/fab', current_user=current_user, tweets=tweets, fab_check=fab_check, follow_check=follow_check)

@route('/fab/<fab_id:int>')
def fab(fab_id):

    fab = fab_table(fab_id)

    return fab

@route('/fab/delete/<fab_id:int>')
def fab(fab_id):

    delete = fab_delete(fab_id)

    return delete

@route('/search')
def view():

    tweets = tweet_view()
    current_user = get_current_user()
    follow_check_view = follow_id_view()
    test = ''

    return template('templates/search', tweets=tweets, test=test, current_user=current_user,follow_check_view=follow_check_view)

@route('/search', method='POST')
def search():

    search = tweet_search(request.POST)
    follow_check_view = follow_id_view()
    current_user = get_current_user()
    print(search)

    if search is not False:
        test=''
        tweets = search
        return template("templates/search", follow_check_view=follow_check_view, search=search, test=test, current_user=current_user, tweets=tweets)
    else:
        test = 'キーワードを入力してください。'
        tweets = tweet_view()
        return template("templates/search", follow_check_view=follow_check_view, tweets=tweets, test=test, current_user=current_user)

@route('/mypage')
def profile():

    current_user = get_current_user()
    pro=None
    my_tweets = my_tweet()
    profile = my_profile()

    return template('templates/mypage', my_tweets=my_tweets, current_user=current_user, pro=pro, profile=profile)

@route('/edit')
def edit():

    current_user = get_current_user()
    profile_view = comment()
    error = ''

    return template('templates/profile_remake', current_user=current_user, profile_view=profile_view, error=error)

@route('/edit', method='POST')
def edit_post():

    current_user = get_current_user()
    test_edit = test_user(request.forms)
    edit = profile_edit(request.POST)

    profile_view = comment()
    commit_text = commit()

    return template('templates/profile_remake', current_user=current_user, edit=edit, profile_view=profile_view, error=commit_text, test_edit=test_edit)

@route('/mypage/delete/<delete_id>')
def delete_tweet(delete_id):

    current_user = get_current_user()
    delete_tweet = delete(delete_id)

    return redirect('/mypage')

@route('/mypage/edit/<tweet_edit_id>')
def tweet_edit(tweet_edit_id):

    current_user = get_current_user()
    mytweet_edit = my_tweet_edit(tweet_edit_id)
    mytweet_edit = mytweet_edit[0][0]

    return template('templates/mytweet_edit', current_user=current_user, tweet_edit_id=tweet_edit_id, mytweet_edit=mytweet_edit)

@route('/mypage/edit/<tweet_edit_id>', method='POST')
def tweet_edit_input(tweet_edit_id):

    current_user = get_current_user()
    tweet_input = my_tweet_edit_input(tweet_edit_id)

    return redirect('/mypage')

@route('/users/profile/<user_id_number>')
def users_profile(user_id_number):

    current_user = get_current_user()
    tweet = users_tweet(user_id_number)
    profile = user_profile(user_id_number)
    fab_check = fab_check_view()
    follow_check = follow_id_view()

    return template('templates/users/profile', follow_check=follow_check, fab_check=fab_check, user_id_number=user_id_number, current_user=current_user, user_profile=profile, user_tweets=tweet)
#
# @route("/test")
# @view("test")
# def test_view():
#
#     return dict(key=stripe_keys['publishable_key'])
#
# @route("/test", method='POST')
# def test_sub():
#
#     db = MySQLdb.connect(user='b292b90b1818e0', passwd='4346c8fc', host='us-cdbr-iron-east-01.cleardb.net', db='heroku_ae66112c0cf1b10', charset='utf8')
#     con = db.cursor()
#
#     sql = 'select test from test where id = 1'
#     test = con.execute(sql)
#     db.commit()
#
#     result = con.fetchall()
#     result = result[0][0]
#
#     amount = '500'
#
#     stripe_token = request.forms.get('stripeToken')
#     mail_address = request.forms.get('stripeEmail')
#
#     stripe.api_key = stripe_keys['secret_key']
#
#     stripe.Charge.create(
#         amount=amount,
#         currency="jpy",
#         description="Charge for {mail}".format(mail=mail_address),
#         source=stripe_token
#     )
#
#     gmail_usr = 'defense433@gmail.com'
#     gmail_password = 'Asatai95!'
#     you = mail_address
#     jp_encoding = 'iso-2022-jp'
#     mail_subject = '〇〇商品について'
#     body = 'text.txt'
#     sender_name = u"OkiDoki株式会社"
#
#     with open(body, 'r', encoding='utf-8') as file:
#         body = file.read()
#
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#
#     server.ehlo()
#
#     server.starttls()
#
#     server.ehlo()
#
#     server.login(gmail_usr, gmail_password)
#
#
#     if server is not False:
#
#         msg = MIMEText(body.encode(jp_encoding), "plain", jp_encoding)
#
#         from_jp = Header(sender_name, jp_encoding)
#         msg['From'] = from_jp
#         From = gmail_usr
#         msg['Subject'] = Header(mail_subject, jp_encoding)
#         msg['To'] = you
#         to = msg['To']
#
#         server.sendmail(From, to, msg.as_string())
#
#
#         print('Email')
#         if server is not False:
#             message = '確かに支払いは完了しました。'
#             return template('message' ,message=message, main=result)
#
#         server.close()
#
#     else:
#
#         print('test')
#
#         return template("top", amount=amount)


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
