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

def create_facebook_user():
    user = User()
    session.add(user)
    session.commit()
    print('test')
    return user

def create_socials(user, data, provider):
    if provider == 'facebook':
        social = Social(
            user_id = user.id,
            provider = provider,
            provider_id = data['id'],
        )

    print('test_sub')
    # elif provider == 'twitter':

    session.add(social)
    session.commit()

def get_facebook_access_token(code):
    url = 'https://graph.facebook.com/v3.1/oauth/access_token'
    params = {
            'redirect_uri': models.app_setting.FACEBOOK_CALLBACK_URL,
            'client_id': models.app_setting.FACEBOOK_ID,
            'client_secret': models.app_setting.FACEBOOK_SECRET,
            'code': code
    }

    r = requests.get(url, params=params)
    return r.json()['access_token']

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
        'fields': 'name,email',
        'access_token': access_token,
    }
    return requests.get(url, params=params).json()


def check_socials(data, provider):
    if provider == 'facebook':
        social = session.query(Social).filter(
                        Social.provider == 'facebook',
                        Social.provider_id == data['id']
                    ).first()
    print('test_test')
    if social is None:
        return False
    else:
        login_user(social.user_id)
        return True

def _encrypt_password(password):
    return hmac.new(
                password.encode('UTF-8'),
                models.app_setting.SECRET_KEY.encode('UTF-8'),
                hashlib.sha256
           ).hexdigest()

def is_duplicate_email(email):
    user = session.query(User).filter(User.email==email).first()
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


def is_logged_in_redirect(user):
    if user is not None:
        redirect('/')

def authenticate(form):
    auth_user = session.query(User).filter(
                User.password == _encrypt_password(form.getunicode('password')),
                User.email == form.getunicode('email')
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
         path='/'
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

def tweet_create(form):

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
               desc(Tweet_comment.tweet_text)
            ).first()

    print(tweet)

    data = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    img = Img(
           img_url = request.POST.getunicode('img'),
           tweet_id = tweet,
           user_id = data
          )

    img_file = img.img_url

    if img_file == '':

        img_file = None
        img.img_url = img_file
        session.add(img)
        session.commit()
        return img
    else:

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

def tweet_table(form):

    content = session.query(Tweet_comment.id).filter(
                    Tweet_comment.tweet_text == form['tweet']
              ).order_by(
                    desc(Tweet_comment.tweet_text)
              ).first()

    data = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    img_db = session.query(Img).filter(
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

    follow_user = session.query(Follow.to_user_id).filter(Follow.to_user_id==form).all()
    print(follow_user)

    if follow_user == []:
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

    fab_view = session.query(Fab.tweet_id).filter(Fab.tweet_id == user_id).all()
    if fab_view == user_id:
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

        search = session.query(Tweet.created_at, Tweet_comment.tweet_text, Tweet_comment.id, User.id, User.name, Img.img_url, User.pro_img).join(
                      User, User.id == Tweet.user_id
                 ).join(
                      Tweet_comment, Tweet_comment.id == Tweet.tweet_id
                 ).join(
                      Img, Img.id == Tweet.img_id
                 ).filter(
                       Tweet.user_id != user_id,
                       Tweet_comment.tweet_text.like("%\\" +form.getunicode('search') + "%")
                 ).all()

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

def test_user(form):

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    profile_edit = session.query(User).filter(
                      User.id == user_id
                   ).first()

    profile_edit.comment = form['user_intro']
    print(profile_edit.comment)

    session.commit()

    return profile_edit

def profile_edit(form):

    user_id = request.get_cookie('user_id', secret=models.app_setting.SECRET_KEY)

    profile_edit = session.query(User).filter(
                      User.id == user_id
                   ).first()
    profile_edit.name = form.getunicode('user_name')
    profile_edit.email = form.getunicode('email')
    profile_edit.pro_img = form.getunicode('img_file')

    img_file = profile_edit.pro_img

    if img_file == '' :
        try:
            img_file = './static/img/ninwanko.png'
            profile_edit.pro_img = img_file
            session.commit()
            return profile_edit

        except OSError:

            session.commit()

            return profile_edit

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

def logout_user():
    response.delete_cookie('user_id', secret=models.app_setting.SECRET_KEY, path='/')


def tweet_view_test():

    view = session.query(Tweet_comment.tweet_text).all()

    return view
