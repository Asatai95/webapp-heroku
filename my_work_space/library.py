from bottle import  request, redirect, response, template

from models.setting import *
from models.user import *
from models.tweet import *
from models.tweet_comment import *
from models.img import *

import hmac
import hashlib

import setting

import os
import random

UPLOAD_FOLDER = './static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'gif'])
path = './static/img/*.ALLOWED_EXTENSIONS'

def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def create_user(form):

    user = User(
           email = form.getunicode('email'),
           password=_encrypt_password(form.getunicode('password')),
           name = form.getunicode('name')
    )

    session.add(user)
    session.commit()
    return user

def _encrypt_password(password):
    return hmac.new(
                password.encode('UTF-8'),
                setting.SECRET_KEY.encode('UTF-8'),
                hashlib.sha256
           ).hexdigest()

def is_duplicate_email(email):
    user = session.query(User).filter(User.email==email).first()
    if user is None:
        return False
    else:
        return True

def get_current_user():

    user_id = request.get_cookie('user_id', secret=setting.SECRET_KEY)
    if user_id:
        return session.query(User).get(user_id)
    else:
        return None


def is_logged_in_redirect(user):
    if user is not None:
        redirect('/')

def authenticate(form):
    auth_user = session.query(User).filter(
                User.password == _encrypt_password(form.getunicode('password')),
                User.email == form.getunicode('email')
    ).first()

    if auth_user is not None:
         response.set_cookie(
              'user_id',
              auth_user.id,
              secret=setting.SECRET_KEY,
              max_age=2678400,
              path='/tweet'
         )
         return True
    else:
         return False

def tweet_create(form):

    tweet_text = Tweet_comment(
                       tweet_comment = form.getunicode('tweet')
                    )
    session.add(tweet_text)
    session.commit()

    return tweet_text
#
# def tweet_table(form):
#
#     content = session.query(Tweet_comment.id).filter(
#                     Tweet_comment.tweet_comment == form.getunicode('tweet')
#               ).order_by(
#                     Tweet_comment.tweet_comment.desc()
#               ).first()
#     data = request.get_cookie('user_id', secret=setting.SECRET_KEY)
#
#     img_db = session.query(Img.id).order_by(
#                      Img.id.desc()
#               ).first()
#
#     tweet = Tweet(
#         tweet_id = content,
#         user_id = data,
#         img_id = img_db
#     )
#
#     session.add(tweet)
#     session.commit()
#
#     return tweet
#
# def img_table(form):
#
#     tweet = session.query(Tweet_comment).filter(
#                Tweet_comment.tweet_comment == form.getunicode('tweet')
#             ).order_by(
#                Tweet_comment.tweet_comment.desc()
#             ).first()
#
#     img = Img(
#            img_url = form.getunicode('img'),
#            tweet_id = tweet.id
#           )
#
#     img_file = img.img_url
#
#     if img_file and allowed_file(img_file.filename):
#         filename = img_file.filename
#         path = UPLOAD_FOLDER + filename
#
#         try:
#             img_file.save(os.path.join(UPLOAD_FOLDER, filename))
#             img.img_url = path
#             session.add(img)
#             session.commit()
#             return img
#         except OSError:
#
#             img_file.save(os.path.join('./static/trash', "無題" ) )
#             path = UPLOAD_FOLDER + filename
#
#             img.img_url = path
#             session.add(img)
#             session.commit()
#             return img

def tweet_view():

    tweet_view = session.query(Tweet.created_at, User.name, Tweet_comment.tweet_comment).join(
                      User, User.id == Tweet.user_id
                  ).join(
                      Tweet_comment, Tweet_comment.id == Tweet.tweet_id
                  ).all()

    return tweet_view


def img_view(form):

    img_view = session.query(Img).filter(
                 Img.img == form.getunicode('img')
               ).first()
    return img_view

def logout_user():
    response.delete_cookie('user_id', secret=setting.SECRET_KEY, path='/')
