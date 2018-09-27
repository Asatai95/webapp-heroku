from bottle import (
    response, request, redirect
)

import hmac
import hashlib

from app_setting import session
from models.user import User

import app_setting

from email.mime.text import MIMEText
import smtplib

"""
ユーザーを作成する
"""
def create_user(form):
    user = User(
        email=form.getunicode('email'),
        password=_encrypt_password(form.getunicode('password1')),
        name=form.getunicode('name'),
        age=int(form.getunicode('age')) if form.getunicode('age') else None
    )
    session.add(user)
    session.commit()
    return user

def _encrypt_password(password):
    return hmac.new(
                msg=password.encode('UTF-8'),
                key=app_setting.SECRET_KEY.encode('UTF-8'),
                digestmod=hashlib.sha256
            ).hexdigest()

def is_duplicate_email(email):
    user = session.query(User).filter(User.email==email).first()
    if user is None:
        return False
    else:
        return True

"""
ログインしているユーザーを取得する
返り値
ログインしている：ログインユーザーのオブジェクト
ログインしていない：None
"""
def get_current_user():
    user_id = request.get_cookie('user_id', secret=app_setting.SECRET_KEY)
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
            secret=app_setting.SECRET_KEY,
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
    response.delete_cookie('user_id', secret=app_setting.SECRET_KEY, path='/')


def send_mail(to_email, send_type):

    body = ''
    subject = ''
    if send_type == 'create':
        body = '〇〇です。\n\n新規登録ありがとうございます。'
        subject = '[新規登録完了] 〇〇〇〇〇〇'
    # elif 'delete':
    #     body = ''
    #     subject =''

    message = MIMEText(body)  # 本文
    message['Subject'] = subject         # 件名
    message['From'] = app_setting.HOST_EMAIL  # 送信元
    message['To'] = to_email     # 送信先

    sender = smtplib.SMTP_SSL(app_setting.HOST_SMTP)
    sender.login(app_setting.HOST_EMAIL, app_setting.HOST_PASSWORD)
    sender.sendmail(app_setting.HOST_EMAIL, to_email, message.as_string())
    sender.quit()

def session_clear(exception):
    if exception and Session.is_active:
        session.rollback()
    else:
        pass
    session.close()
