from bottle import (
    response, request, redirect
)

import hmac
import hashlib


from models.setting import *
from models.user import *

import setting


"""
import setting
setting.SECRET_KEY

from setting import *
SECRET_KEY

ディレクトリの数によって判断する
"""

"""
ユーザーを作成する
"""
def create_user(form):
    user = User(
        email= form.getunicode('email'),
        password= _encrypt_password(form.getunicode('password1')),
        name= form.getunicode('name'),
        age= int(form.getunicode('age')) if form.getunicode('age') else None
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
"""
ログインしているユーザーを取得する
返り値
ログインしている：ログインユーザーのオブジェクト
ログインしていない：None
"""
def get_current_user():
    user_id = request.get_cookie('user_id', secret=setting.SECRET_KEY)
    if user_id:
        return session.query(User).get(user_id)
    else:
        return None

"""
ログインしていればルートパスにリダイレクトさせる
"""
def is_logged_in_redirect(user):
    if user is not None:
        redirect('/')

"""
ログイン認証をする
フォームから送られてきた値でDBで確認
該当ユーザーがいればクッキーに設定
返り値
ログイン成功：True
ログイン失敗：False
"""
def authenticate(form):
    auth_user = session.query(User).filter(
                  User.email==form.getunicode('email'),
                  User.password==_encrypt_password(form.getunicode('password'))
                ).first()

    if auth_user is not None:
        response.set_cookie(
            'user_id',
            auth_user.id,
            secret=setting.SECRET_KEY,
            max_age=2678400, # 31日間有効
            path='/'
        )
        return True
    else:
        return False

"""
ログアウト
"""
def logout_user():
    response.delete_cookie('user_id', secret=setting.SECRET_KEY, path='/')
