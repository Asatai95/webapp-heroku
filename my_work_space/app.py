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

from models.setting import *
from models.user import *
from models.tweet import *
from models.tweet_comment import *
from models.img import *
from models.follow import *
from models.fab import *
from models.pro_comment import *

from library import *

import setting

import sys

from urllib.parse import urljoin


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

    return template('templates/create', user=user, current_user=current_user , duplicate_error=duplicate_error)

@route("/info")
def info():

    return template('templates/info', url=url)

@route('/tweet', method='GET')
def tweet():

    current_user = get_current_user()
    tweets = tweet_view()
    check = follow_id_view()
    follow_check = follower_check()
    print(follow_check)
    for tweet in tweets:
        if check in tweet:
            print('test')
        else:
            print('testdes')


    return template('templates/tweet', tweets=tweets, current_user=current_user, check=check, follow_check=follow_check)

@route('/tweet', method='POST')
def tweer_db():

    current_user = get_current_user()
    tweet_comment = tweet_create(request.forms)
    img = img_table(request.forms)
    tweet_db = tweet_table(request.forms)
    tweets = tweet_view()

    return template('templates/tweet', tweet_comment=tweet_comment, tweets=tweets, tweet=tweet_db, img=img_table, current_user=current_user)

@route('/follow/<user_follow:int>')
def follow(user_follow):

    current_user = get_current_user()
    follow_user = follow_table(user_follow)
    tweets = tweet_view()

    return redirect('/follower')

@route('/follower')
def follower():

    current_user = get_current_user()
    follower_view_table = follower_view()

    return template('templates/follower', current_user=current_user, follower_view_table=follower_view_table)

@route('/follower/delete/<delete_follower_id>')
def delete_follower_id(delete_follower_id):

    current_user = get_current_user()
    delete = delete_follower(delete_follower_id)

    return redirect('/follower')

@route('/fab/<fab_id:int>')
def fab(fab_id):

    current_user = get_current_user()
    fab_db = fab_table(fab_id)
    tweets = tweet_view()

    return template('templates/fab', tweets=tweets, fab_db=fab_db, fab_id=fab_id, current_user=current_user)

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
    mytweet_img = my_tweet_img()
    mytweet_img = mytweet_img[0][0]

    return template('templates/mypage', my_tweets=my_tweets, current_user=current_user, pro=pro, mytweet_img=mytweet_img)

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

@route('/test')
def test_view():

    tweets = tweet_view_test()

    return template('templates/test_sub', tweets=tweets)


# @route('/follow/<follow_user_id:int>')
# def follow(follow_user_id):
#
#     return redirect('/tweet')

# @route('/follow/<follow_id_test:int>')
# def follow(follow_id_test):
#
#
# @route('/follow/<follow_id:int>')
# def follow_back(follow_id):
#
#     return redirect('/tweet')
# @route("/new", method='POST')
# def new():
#
#     user_name = request.forms.user_name
#     passwd_new = request.forms.new_passwd
#     log_id_new = request.forms.new_log_id
#     print(log_id_new)
#     print(passwd_new)
#     print(user_name)
#
#     try:
#         user = User()
#         user.name = str(user_name)
#         user.passwd = str(passwd_new)
#         user.email = str(log_id_new)
#         print('test')
#
#         users = session.add(user)
#         session.commit()
#         print(users)
#
#
#         return redirect('/info')
#
#
#     except exc.InvalidRequestError :
#
#         error = 'すでに登録されているパスワードです。'
#         print('test')
#
#         return template('templates/create', error=error)
#
#     except exc.IntegrityError:
#
#         error = 'すでに登録されているパスワードです。'
#         print('test')
#
#         return template('templates/create', error=error)





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
