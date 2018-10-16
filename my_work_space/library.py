from bottle import  request, redirect, response, template

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

import hmac
import hashlib

import models.app_setting

from email.mime.text import MIMEText
import smtplib

import os
import random

import sys

import requests

import stripe
stripe.api_key = models.app_setting.STRIPE_SECRET

from httplib2 import Http
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from apiclient.discovery import build
import httplib2

from requests_oauthlib import OAuth1Session

import urllib
import oauth2 as oauth


SCOPE = 'https://www.googleapis.com/auth/plus.login'
CREDENTIALS_FILE = "./google/test"

request_token_url = 'http://twitter.com/oauth/request_token'
access_token_url = 'http://twitter.com/oauth/access_token'
authenticate_url = 'https://api.twitter.com/oauth/authenticate'
callback_url = 'http://localhost:5000/twitter/callback/'


flow = flow_from_clientsecrets(
   './client_id.json',
   scope=SCOPE,
   redirect_uri= "http://localhost:5000/google/callback")

UPLOAD_FOLDER = './static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'gif'])
path = './static/img/*.ALLOWED_EXTENSIONS'

def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def set_stripe_id(stripe_id, email):

    user = User(
        stripe_id = stripe_id,
        email = email
    )
    session.add(user)
    session.commit()

def check_account_payafter(email, stripe_id):

    user = session.query(User).filter(
               User.email == email,
               User.stripe_id == stripe_id
           ).all()

    if user is None:
        return False
    else:
        return True

def check_email_stripe_id(form):

    user = session.query(User.stripe_id).filter(
                User.email == form.getunicode('email')
           ).all()

    if user is None:
        return False
    else:
        return user

def user_email_first():

    stripe_id = request.get_cookie('stripe_id', secret=models.app_setting.SECRET_KEY)

    email = session.query(User.email).filter(
            User.stripe_id == stripe_id
    ).all()

    email = email[0][0]
    return email

def user_stripe_delete():

    stripe_id = request.get_cookie('stripe_id', secret=models.app_setting.SECRET_KEY)

    email = session.query(User).filter(
            User.stripe_id == stripe_id,
            User.name == None,
            User.password == None
    ).delete()

    if email == 0:
        pass
    else:
        session.commit()
        return True

def _encrypt_password(password):

    return hmac.new(
                password.encode('UTF-8'),
                models.app_setting.SECRET_KEY.encode('UTF-8'),
                hashlib.sha256
           ).hexdigest()

def remake_password_email(form):

    user = session.query(User.email).filter(
               User.email == form.getunicode('email')
           ).all()

    if user == []:
        return False
    else:
        user = user[0][0]
        return user

def url_check(mail_id, mail, get_stripe_cookie):

    text = 'email_change'
    email = hmac.new(
                text.encode('UTF-8'),
                models.app_setting.SECRET_KEY.encode('UTF-8'),
                hashlib.sha256
           ).hexdigest()
    user = session.query(User.email).filter(
            User.email == mail,
            User.stripe_id == get_stripe_cookie
    ).all()

    if user[0][0] == mail:
        if email == mail_id:
            return True
        else:
            return False
    else:
        return False


def remake_password_check(mail, form, stripe_id):

    password_check = session.query(User.password).filter(
              User.email == mail,
              User.stripe_id == stripe_id
    ).all()

    if password_check is None:

        remake = User(
              password = _encrypt_password(form.getunicode('password2'))
        )
        session.add(remake)
        session.commit()

    else:
        remake = session.query(User).filter(
              User.email == mail,
              User.stripe_id == stripe_id
        ).first()
        print(remake)
        remake.password = _encrypt_password(form.getunicode('password2'))
        session.commit()

def password_checker(form):

    if form.getunicode('password1') == form.getunicode('password2'):
        return True
    else:
        return False

def loggedin_account():

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    account = session.query(User.id).filter(
                 User.id == user_id
              ).all()
    return account

def create_user(form):

    stripe_id = request.get_cookie('stripe_id', secret=models.app_setting.SECRET_KEY)

    user = User(
        stripe_id = stripe_id,
        name = form.getunicode('name'),
        email = form.getunicode('email'),
        password = _encrypt_password(form.getunicode('password')),
        pro_img = './static/img/hi.png'
    )
    session.add(user)
    session.commit()

    return user

def create_facebook_user(form):

    stripe_id = request.get_cookie('stripe_id', secret=models.app_setting.SECRET_KEY)

    user = User(
               stripe_id = stripe_id,
               name = form['name'],
               email = form['email'],
               pro_img = './static/img/ninwanko.png'
            )
    session.add(user)
    session.commit()
    return user

def create_google_user():

    stripe_id = request.get_cookie('stripe_id', secret=models.app_setting.SECRET_KEY)

    user = User(
          stripe_id = stripe_id
    )
    session.add(user)
    session.commit()
    return user

def create_twitter_user(form):

    stripe_id = request.get_cookie('stripe_id', secret=models.app_setting.SECRET_KEY)

    user = User(
          stripe_id = stripe_id,
          name = form['screen_name']
    )
    session.add(user)
    session.commit()
    return user

def create_socials(user, data, provider):

    if provider == 'facebook':
        social = Social(
            user_id = user.id,
            provider = provider,
            provider_id = data['id'],
        )
    elif provider == 'google':
        social = Social(
            user_id = user.id,
            provider = provider,
            provider_id = data
        )
    elif provider == 'twitter':
        social = Social(
            user_id = user.id,
            provider = provider,
            provider_id = data['user_id']
        )

    session.add(social)
    session.commit()

def check_socials(data, provider):

    if provider == 'facebook':
        social = session.query(Social).filter(
                        Social.provider == 'facebook',
                        Social.provider_id == data['id']
                    ).first()
    elif provider == 'twitter':
        social = session.query(Social).filter(
                        Social.provider == 'twitter',
                        Social.provider_id == data['user_id']
                    ).first()
    else:
        social = session.query(Social).filter(
                       Social.provider == 'google',
                       Social.provider_id == data
                    ).first()

    if social is None:
        return False
    else:
        login_user(social.user_id)
        return True

def get_facebook_access_token(code):

    url = 'https://graph.facebook.com/v3.1/oauth/access_token'
    params = {
            'redirect_uri': models.app_setting.FACEBOOK_CALLBACK_URL,
            'client_id': models.app_setting.FACEBOOK_ID,
            'client_secret': models.app_setting.FACEBOOK_SECRET,
            'code': code,
    }
    r = requests.get(url, params=params)
    return r.json()['access_token']


def get_twitter_request_token():

    request_token = request.GET["oauth_token"] # リクエストトークンは以前と同じもの
    verifier = request.GET["oauth_verifier"]
    oauth = OAuth1Session(
            models.app_setting.CONSUMER_KEY,
            client_secret=models.app_setting.CONSUMER_SECRET,
            resource_owner_key=request_token,
            verifier=verifier)
    access_token_url = "https://api.twitter.com/oauth/access_token"
    # アクセストークン取得
    response = oauth.fetch_request_token(access_token_url)
    print(response)
    return response
#
#     # consumer = oauth.Consumer(key=models.app_setting.CONSUMER_KEY, secret=models.app_setting.CONSUMER_SECRET)
#     # client = oauth.Client(consumer)
#     # print(client)
#     #
#     # # reqest_token を取得
#     # content = client.request(request_token_url, 'GET')
#     # request_token = dict(parse_qsl(content))
#     # print(content)
#     #
#     # url = '%s?&oauth_token=%s' % (authenticate_url , request_token['oauth_token'])
#     # print(url)
#
#     # request token取得
#     oauth = OAuth1Session(
#             models.app_setting.CONSUMER_KEY,
#             client_secret=models.app_setting.CONSUMER_SECRET,
#             callback_uri=callback_url)
#     request_token_url = "https://api.twitter.com/oauth/request_token"
#     response = oauth.fetch_request_token(request_token_url)
#
#     # 認証用URL作成
#     redirect_url = "https://api.twitter.com/oauth/authenticate?oauth_token=" + response["oauth_token"]
#     print(oauth)
#
#     # 認証へリダイレクト
#     return redirect(redirect_url)

#
# def parse_qsl(url):
#     param = {}
#     for i in str(url).split("&"):
#         _p = i.split("=")
#         param.update({_p[0]: _p[1]})
#     return param
#
# def get_access_token(oauth_token, oauth_verifier):
#     consumer = oauth.Consumer(key=models.app_setting.CONSUMER_KEY, secret=models.app_setting.CONSUMER_SECRET)
#     token = oauth.Token(oauth_token, oauth_verifier)
#
#     client = oauth.Client(consumer, token)
#     content = client.request("https://api.twitter.com/oauth/access_token",
#                                    "POST", body="oauth_verifier={0}".format(oauth_verifier))
#     return content


# def get_twitter_access_token():
#
#     headers = { "Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8" }
#     data = { "grant_type":"client_credentials" }
#     oauth2_url = "https://api.twitter.com/oauth2/token"
#     r = requests.post(oauth2_url, data=data, headers=headers, auth=(models.app_config.CONSUMER_KEY, models.app_config.CONSUMER_SECRET))
#
#     print(r.json()["access_token"])
#     print(r.json()["access_token"])
#     print(r.json()["access_token"])
#     print(r.json()["access_token"])
#
#
#     return r.json()["access_token"]


def check_facebook_access_tokn(access_token):

    url = 'https://graph.facebook.com/debug_token'
    params = {
        'input_token': access_token,
        'access_token': '%s|%s' % (models.app_setting.FACEBOOK_ID, models.app_setting.FACEBOOK_SECRET)
    }
    r = requests.get(url, params=params)
    return r.json()['data']

def get_facebook_user_info(access_token, user_id):

    url = 'https://graph.facebook.com/%s' % (user_id)
    params = {
        'fields': 'name, email',
        'access_token': access_token,
    }
    return requests.get(url, params=params).json()

def google_login_flow(code):

    credentials = flow.step2_exchange(code)

    CREDENTIALS_FILE = "./credentials"
    Storage(CREDENTIALS_FILE).put(credentials)

    credentials = Storage(CREDENTIALS_FILE).get()
    http_auth = credentials.authorize(Http())
    service = build('plus', 'v1', http=http_auth)

    result = service.people().get(userId='me').execute()

    return result['id']


def is_duplicate_email(email):

    user = session.query(User).filter(User.email==email).first()
    if user is None:
        return False
    else:
        return True

def is_duplicate_name(name):

    user = session.query(User).filter(User.name == name).first()
    if user is None:
        return False
    else:
        return True

def get_current_user():

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)
    if user_id:
        return session.query(User).get(user_id)
    else:
        return None

def get_stripe_cookie():

    stripe_id = request.get_cookie('stripe_id', secret=models.app_setting.SECRET_KEY)
    if stripe_id:
        return stripe_id
    else:
        return None

def get_current_stripe_id():

    stripe_id = request.get_cookie('stripe_id', secret=models.app_setting.SECRET_KEY)
    if stripe_id:
        return True
    else:
        return None

def get_current_stripe_id_check():

    stripe_id = request.get_cookie('stripe_id', secret=models.app_setting.SECRET_KEY)
    user = session.query(User).filter(User.stripe_id==stripe_id).all()

    if user:
        return True
    else:
        return None

def is_logged_in_redirect(user):
    if user is not None:
        return True
    else:
        redirect('/')

def authenticate(form):
    auth_user = session.query(User).filter(
                User.email == form.getunicode('email'),
                User.password == _encrypt_password(form.getunicode('password'))
    ).first()

    if auth_user is not None:
        login_user(auth_user.id)
        return True
    else:
        return False

def login_user(user_id):

    response.set_cookie(
         'user_id',
         user_id,
         secret=models.app_setting.SECRET_KEY,
         max_age=2678400,
         path='/',
    )

def login_stripe_id(stripe_id):

    response.set_cookie(
         'stripe_id',
         stripe_id,
         secret=models.app_setting.SECRET_KEY,
         max_age=2678400,
         path='/',
    )

def tweet_view():

    cookie_id = request.get_cookie('user_id' ,secret=models.app_setting.SECRET_KEY)

    tweet_view = session.query(Tweet.created_at, Tweet_comment.tweet_text, Tweet_comment.id, User.id, User.name, Img.img_url, User.pro_img, Tweet.tweet_id, Tweet.id).join(
                      User, User.id == Tweet.user_id
                  ).join(
                      Tweet_comment, Tweet_comment.id == Tweet.tweet_id
                  ).join(
                      Img, Img.id == Tweet.img_id
                  ).filter(
                      Tweet.user_id != cookie_id
                  ).all()

    return tweet_view

def follow_id_view():

    cookie_id = request.get_cookie('user_id' ,secret=models.app_setting.SECRET_KEY)

    follow_view = session.query(Follow.to_user_id).filter(
                     Follow.from_user_id == cookie_id,
                     Follow.follow_id == 1
                  ).all()

    return follow_view

def follow_comment():

    comment = session.query(Follow_comment.comment).all()

    return comment

def tweet_comment_create(form):

    tweet_text = Tweet_comment(
                       tweet_text = form['tweet']
                    )
    session.add(tweet_text)
    session.commit()

    return tweet_text

def img_table(form):

    tweet = session.query(Tweet_comment.id).filter(
               Tweet_comment.tweet_text == form['tweet']
            ).order_by(
               desc(Tweet_comment.id)
            ).first()

    data = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    if request.POST.getunicode('img') != '' :

        img = Img(
               img_url = request.POST.getunicode('img'),
               tweet_id = tweet,
               user_id = data
              )

        img_file = img.img_url

        if img_file and allowed_file(img_file.filename):
            filename = img_file.filename
            path = UPLOAD_FOLDER + filename

            try:
                img_file.save(os.path.join(UPLOAD_FOLDER, filename))
                img.img_url = path
                session.add(img)
                session.commit()
                return img
            except OSError:

                os.remove(path)
                img_file.save(os.path.join(UPLOAD_FOLDER, filename))
                img.img_url = path
                session.add(img)
                session.commit()
                return img
    else:
        img = Img(
               img_url = None,
               tweet_id = tweet,
               user_id = data
              )
        session.add(img)
        session.commit()
        print(img)
        print(img.img_url)
        return img

def tweet_table(form):

    content = session.query(Tweet_comment.id).filter(
                    Tweet_comment.tweet_text == form['tweet']
              ).order_by(
                    desc(Tweet_comment.id)
              ).first()

    data = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    img_db = session.query(Img).join(
                    Tweet_comment, Tweet_comment.id == Img.tweet_id
             ).filter(
                    Tweet_comment.tweet_text == form['tweet'],
                    Img.user_id == data
             ).order_by(
                    desc(Img.id)
             ).first()

    tweet = Tweet(
               tweet_id = content,
               user_id = data,
               img_id = img_db.id
            )
    session.add(tweet)
    session.commit()
    return tweet

def img_view(form):

    img_view = session.query(Img).filter(
                 Img.img == form.getunicode('img')
               ).first()
    return img_view

def follow_table(form):

    from_id = request.get_cookie('user_id' ,secret=models.app_setting.SECRET_KEY)
    follow_id = 1

    follow_user = session.query(Follow.follow_id).filter(
                   Follow.to_user_id==form,
                   Follow.from_user_id == from_id
                  ).all()

    if follow_id == 1:
        follow = Follow(
                  from_user_id = from_id,
                  to_user_id = form,
                  follow_id = follow_id
                )
        session.add(follow)
        session.commit()
        return redirect('/follower')
    else:
        return redirect('/follower')

def fab_view():

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)
    flag = 1

    fabs = session.query(Tweet.id ,Tweet.tweet_id, Tweet.img_id, Tweet.created_at, Fab.user_id, Tweet_comment.tweet_text, User.id, User.name, User.pro_img, Img.img_url, Fab.id).join(
                    User, User.id == Tweet.user_id
               ).join(
                    Fab, Fab.tweet_id == Tweet.id
               ).join(
                    Tweet_comment, Tweet_comment.id == Tweet.tweet_id
               ).join(
                    Img, Img.id == Tweet.img_id
               ).filter(
                    Fab.user_id == user_id,
                    Fab.fab_id == flag
               ).all()
    print(fabs)
    return fabs

def fab_table(form):

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    fab_view = session.query(Fab.fab_id).filter(
                Fab.user_id == user_id,
                Fab.tweet_id == form
               ).all()
    if fab_view == 1:
        return redirect('/fab')
    else:
        fab = Fab(
               user_id = user_id,
               tweet_id = form,
               fab_id = 1
          )
        session.add(fab)
        session.commit()
        return redirect('/fab')

def fab_delete(form):

    delete = session.query(Fab).filter(
                Fab.tweet_id == form
             ).delete()
    session.commit()
    return redirect('/fab')

def fab_check_view():

    user_id = request.get_cookie('user_id' ,secret=models.app_setting.SECRET_KEY)

    check = session.query(Fab.tweet_id).filter(
                Fab.user_id == user_id,
                Fab.fab_id == 1
           ).all()
    return check


def tweet_search(form):

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    if form.getunicode('search') == '':
        return False
    else:
        search = session.query(Tweet.created_at, Tweet_comment.tweet_text, Tweet_comment.id, User.id, User.name, Img.img_url, User.pro_img, Tweet.tweet_id, Tweet.id).join(
                      User, User.id == Tweet.user_id
                 ).join(
                      Tweet_comment, Tweet_comment.id == Tweet.tweet_id
                 ).join(
                      Img, Img.id == Tweet.img_id
                 ).filter(
                       Tweet.user_id != user_id,
                       Tweet_comment.tweet_text.like("%\\" +form.getunicode('search') + "%")
                 ).all()
        if search == []:
            error = 'error'
            return error
        else:
            return search

def my_tweet():

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)


    profile = session.query(Tweet.created_at, Tweet_comment.tweet_text, Tweet.tweet_id, User.id, User.name, Img.img_url, User.pro_img).join(
                  User, User.id == Tweet.user_id
             ).join(
                  Tweet_comment, Tweet_comment.id == Tweet.tweet_id
             ).join(
                  Img, Img.id == Tweet.img_id
             ).filter(
                  Tweet.user_id == user_id,
             ).all()

    return profile

def my_profile():

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    profile = session.query(User.name, User.comment, User.pro_img).filter(
                  User.id == user_id
              ).all()
    return profile

def my_tweet_img():

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    profile = session.query(User.pro_img).filter(
                   User.id == user_id

             ).all()

    return profile


def comment():

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    profile = session.query(User.id, User.name, User.email, User.pro_img, User.comment).filter(
                   User.id == user_id
              ).all()

    return profile

def my_comment(form):

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    profile_edit = session.query(User).filter(
                      User.id == user_id
                   ).first()

    profile_edit.name = form['user_name']
    profile_edit.comment = form['user_intro']

    session.commit()

    return profile_edit

def profile_edit(form):

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)
    user_mail = session.query(User.email).all()
    user_email_check = session.query(User.email).filter(User.id == user_id).all()

    if user_email_check == [('',)]:
        for mail in user_mail:
            if (form.getunicode('email'),) == mail:
                return False

        profile_edit = session.query(User).filter(
                          User.id == user_id
                     ).first()
        profile_edit.email = form.getunicode('email')
        profile_edit.pro_img = form.getunicode('img_file')

        img_file = profile_edit.pro_img

        if img_file == '' :
            try:
                img_file = './static/img/ninwanko.png'
                profile_edit.pro_img = img_file
                session.commit()
                return profile_edit
            except:
                redirect('/edit')

        else:
            if img_file and allowed_file(img_file.filename):
                filename = img_file.filename
                path = UPLOAD_FOLDER + filename
                try:
                    img_file.save(os.path.join(UPLOAD_FOLDER, filename))
                    profile_edit.pro_img = path
                    session.commit()
                    return profile_edit
                except OSError:
                    os.remove(path)
                    img_file.save(os.path.join(UPLOAD_FOLDER, filename))
                    profile_edit.pro_img = path
                    session.commit()
                    return profile_edit

    else:
        print('test')
        profile_edit = session.query(User).filter(
                        User.id == user_id
                       ).first()
        profile_edit.email = form.getunicode('email')
        profile_edit.pro_img = form.getunicode('img_file')

        img_file = profile_edit.pro_img

        if img_file == '' :
            try:
                img_file = './static/img/ninwanko.png'
                profile_edit.pro_img = img_file
                session.commit()
                return profile_edit
            except:
                redirect('/edit')

        else:
            if img_file and allowed_file(img_file.filename):
                filename = img_file.filename
                path = UPLOAD_FOLDER + filename
                try:
                    img_file.save(os.path.join(UPLOAD_FOLDER, filename))
                    profile_edit.pro_img = path
                    session.commit()
                    return profile_edit
                except OSError:
                    os.remove(path)
                    img_file.save(os.path.join(UPLOAD_FOLDER, filename))
                    profile_edit.pro_img = path
                    session.commit()
                    return profile_edit

def commit():

    text = '正しく内容を変更致しました。'

    return text

def delete(form):

    delete = session.query(Tweet_comment).filter(
                Tweet_comment.id == form
             ).delete()
    session.commit()
    return delete

def my_tweet_edit(form):

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    tweet_edit = session.query(Tweet_comment.tweet_text).join(
                  Tweet, Tweet.tweet_id == Tweet_comment.id
             ).filter(
                  Tweet.user_id == user_id,
                  Tweet_comment.id == form
             ).all()

    return tweet_edit

def my_tweet_edit_input(form):

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    tweet_edit = session.query(Tweet_comment.id).join(
                  Tweet, Tweet.tweet_id == Tweet_comment.id
             ).filter(
                  Tweet.user_id == user_id,
                  Tweet_comment.id == form
             ).all()
    if tweet_edit != form:
        redirect('/mypage')

    tweet_edit = session.query(Tweet_comment).join(
                  Tweet, Tweet.tweet_id == Tweet_comment.id
             ).filter(
                  Tweet.user_id == user_id,
                  Tweet_comment.id == form
             ).first()

    tweet_edit.tweet_text = request.POST.getunicode('tweet')
    print(tweet_edit.tweet_text)
    session.commit()

    return tweet_edit

def follower_view():

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)
    follower = session.query(Follow.to_user_id, User.name, User.comment, User.pro_img).join(
                    User, User.id == Follow.to_user_id
               ).filter(
                    Follow.from_user_id == user_id,
                    Follow.to_user_id == User.id,
                    Follow.to_user_id != user_id,
                    Follow.follow_id == 1
               ).all()

    return follower

def delete_follower(form):

    delete = session.query(Follow).filter(
               Follow.to_user_id == form,
               Follow.follow_id == 1
             ).delete()
    session.commit()

    return redirect('/follower')

def user_profile(form):

    profile = session.query(User.name, User.pro_img, User.comment, User.id).filter(
                 User.id == form
              ).all()

    return profile

def users_tweet(form):

    user_tweet = session.query(Tweet.created_at, Tweet_comment.tweet_text, Tweet.tweet_id, User.id, User.name, Img.img_url, User.pro_img, Tweet.id).join(
                    User, User.id == Tweet.user_id
               ).join(
                    Tweet_comment, Tweet_comment.id == Tweet.tweet_id
               ).join(
                    Img, Img.id == Tweet.img_id
               ).filter(
                    Tweet.user_id == form
               ).all()
    return user_tweet

def send_mail(to_email, send_type):
    body=''
    subject = ''
    url = "http://localhost:5000/user/"+to_email+" "
    if send_type == 'create':
        body = '〇〇です。 \n\n新規登録ありがとうございます。'
        subject = '【新規登録完了】〇〇〇〇〇'
    elif send_type == 'delete':
        body = '〇〇です。\n\n〇〇アプリをご利用いただきありがとうございます。'
        subject = '【削除完了】〇〇〇〇〇'


    message = MIMEText(body)  # 本文
    message['Subject'] = subject         # 件名
    message['From'] = models.app_setting.HOST_EMAIL  # 送信元
    message['To'] = to_email      # 送信先

    sender = smtplib.SMTP_SSL(models.app_setting.HOST_SMTP)
    sender.login(models.app_setting.HOST_EMAIL, models.app_setting.HOST_PASSWORD)
    sender.sendmail(models.app_setting.HOST_EMAIL, to_email, message.as_string())
    sender.quit()

def stripe_create_mail(to_email, stripe_id, send_type):
    body=''
    subject = ''

    url = "http://localhost:5000/user/"+to_email+"/"+stripe_id+" "

    if send_type == 'pay':
        body = '〇〇です。\n\nご購入いただきありがとうございます。\n\n下記のURLからアカウントを登録してください。\n\n'+url+' '
        subject = '【支払い完了】〇〇〇〇〇'

    message = MIMEText(body)  # 本文
    message['Subject'] = subject         # 件名
    message['From'] = models.app_setting.HOST_EMAIL  # 送信元
    message['To'] = to_email      # 送信先

    sender = smtplib.SMTP_SSL(models.app_setting.HOST_SMTP)
    sender.login(models.app_setting.HOST_EMAIL, models.app_setting.HOST_PASSWORD)
    sender.sendmail(models.app_setting.HOST_EMAIL, to_email, message.as_string())
    sender.quit()

def remake_check_mail(to_email, send_type, mail):
    body=''
    subject = ''
    text = 'email_change'
    email = hmac.new(
                text.encode('UTF-8'),
                models.app_setting.SECRET_KEY.encode('UTF-8'),
                hashlib.sha256
           ).hexdigest()

    url = "http://localhost:5000/remake/"+email+"/"+mail+" "

    if send_type == 'remake':
        body = 'パスワード再設定用のメールです。\n\n下記のURLからパスワードを再設定してください。\n\n '+ url +' '

    message = MIMEText(body)  # 本文
    message['Subject'] = subject         # 件名
    message['From'] = models.app_setting.HOST_EMAIL  # 送信元
    message['To'] = to_email      # 送信先

    sender = smtplib.SMTP_SSL(models.app_setting.HOST_SMTP)
    sender.login(models.app_setting.HOST_EMAIL, models.app_setting.HOST_PASSWORD)
    sender.sendmail(models.app_setting.HOST_EMAIL, to_email, message.as_string())
    sender.quit()

def delete_check(form):

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    check = session.query(User).filter(
               User.email == form.getunicode('email')
            ).all()

    if check is not None:
        return True
    else:
        return False

def delete_mail():

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    mail = session.query(User.email).filter(
                User.id == user_id
            ).all()
    return mail

def delete_account():

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    user_account_delete = session.query(User).filter(
                             User.id == user_id
                         ).delete()
    session.commit()
    return user_account_delete

def logout_user():
    response.delete_cookie('user_id', secret=models.app_setting.SECRET_KEY, path='/')
