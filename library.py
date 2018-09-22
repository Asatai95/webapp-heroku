from bottle import  request, redirect, response, template

from models.setting import *
from models.user import *

import hmac
import hashlib

import setting


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
                User.email == form.getunicode('email'),
                User.password == form.getunicode('password')
    ).first()

    if auth_user is not None:
         response.set_cookie(
              'user_id',
              auth_user.id,
              secret=setting.SECRET_KEY,
              max_age=2678400,
              path='/'
         )
         return True
    else:
         return False

def logout_user():
    response.delete_cookie('user_id', secret=setting.SECRET_KEY, path='/')
