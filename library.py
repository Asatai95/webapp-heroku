from bottle import (
    response, request, redirect
)

import hmac
import hashlib

from app_setting import session
from models.user import User
from models.social import Social
from models.plan import Plan

import app_setting

from email.mime.text import MIMEText
import smtplib

import requests

import stripe

def stripe_pay_after(form):

    mail = form.getunicode('stripeEmail')

    return mail

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

"""
Facebookログインしたユーザのモデルを生成する
今回はデータの入力はしない
個々の処理は、APIの取得情報追加申請などで変えると良い
"""
def create_facebook_user(data):
    user = User(
             name = data['name']
            )
    session.add(user)
    session.commit()
    return user


"""
APIで受け取った情報をもとにソーシャルレコードを作成
"""
def create_socials(user, data, provider):
    if provider == 'facebook':
        social = Social(
            user_id = user.id,
            provider = provider,
            provider_id = data['id'],
        )
    # elif provider == 'twitter':

    session.add(social)
    session.commit()


"""
APIで受け取ったユーザー情報でDB照合
返り値
照合失敗：False
照合成功：True
照合成功後はログイン処理を行う
"""
def check_socials(data, provider):
    if provider == 'facebook':
        social = session.query(Social).filter(
                        Social.provider == 'facebook',
                        Social.provider_id == data['id']
                    ).first()

    if social is None:
        return False
    else:
        login_user(social.user_id)
        return True


"""
リダイレクトと同時に送られてきたcodeを用いてアクセストークンを取得
"""
def get_facebook_access_token(code):
    url = 'https://graph.facebook.com/v3.1/oauth/access_token'
    params = {
            'redirect_uri': app_setting.FACEBOOK_CALLBACK_URL,
            'client_id': app_setting.FACEBOOK_ID,
            'client_secret': app_setting.FACEBOOK_SECRET,
            'code': code,
    }
    r = requests.get(url, params=params)

    return r.json()['access_token']


"""
取得したアクセストークンが不正じゃないか確認する
"""
def check_facebook_access_tokn(access_token):
    url = 'https://graph.facebook.com/debug_token'
    params = {
        'input_token': access_token,
        'access_token': '%s|%s' % (app_setting.FACEBOOK_ID, app_setting.FACEBOOK_SECRET)
    }
    r = requests.get(url, params=params)
    return r.json()['data']

"""
アクセストークンが不正じゃないことがわかったら
アクセストークンをもとにユーザーの情報を取得する
"""
def get_facebook_user_info(access_token, user_id):
    url = 'https://graph.facebook.com/%s' % (user_id)
    params = {
        'fields': 'name,email',
        'access_token': access_token,
    }
    return requests.get(url, params=params).json()


"""
現在のユーザーのソーシャルログイン情報を取得する
"""
def get_socials_info(user):
    return session.query(Social).filter(Social.user_id == user.id)

"""
ユーザー編集
"""
def update_user(current_user, form):
    user = session.query(User).get(current_user.id)
    if form.getunicode('name'):
        user.name = form.getunicode('name')
    if form.getunicode('age'):
        user.age=int(form.getunicode('age')) if form.getunicode('age') else None
    if form.getunicode('email'):
        user.email = form.getunicode('email')
    session.commit()

def set_stripe_id(user, stripe_id):

    user.stripe_id = stripe_id
    session.commit()


"""
パスワード編集
"""
def update_password(current_user, form):
    user = session.query(User).get(current_user.id)
    if form.getunicode('password1'):
        user.password = _encrypt_password(form.getunicode('password1'))
    session.commit()

"""
パスワードの暗号化
"""
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
        login_user(auth_user.id)
        return True
    else:
        return False


"""
引数で受け取った ユーザーIDでクッキーをセットする
"""
def login_user(user_id):
    response.set_cookie(
        'user_id',
        user_id,
        secret=app_setting.SECRET_KEY,
        max_age=2678400, # 31日間有効
        path='/'
    )

"""
ログアウト
"""
def logout_user():
    response.delete_cookie('user_id', secret=app_setting.SECRET_KEY, path='/')


"""
メール送信
引数1つ目：送り先のメール
引数2つ目：メールの種類
例
 send_mail(user.email, 'create')
 send_mail(user.email, 'delete')
"""
# send_mail(user.email, 'create')
def send_mail(to_email, send_type):
    body=''
    subject = ''
    if send_type == 'create':
        body = '〇〇です。 \n\n新規登録ありがとうございます。'
        subject = '【新規登録完了】〇〇〇〇〇'
    elif 'pay':
        body = '〇〇です。\n\n商品購入ありがとうございます。'
        subject = '【商品購入完了】〇〇〇〇〇'

    message = MIMEText(body)  # 本文
    message['Subject'] = subject         # 件名
    message['From'] = app_setting.HOST_EMAIL  # 送信元
    message['To'] = to_email      # 送信先

    sender = smtplib.SMTP_SSL(app_setting.HOST_SMTP)
    sender.login(app_setting.HOST_EMAIL, app_setting.HOST_PASSWORD)
    sender.sendmail(app_setting.HOST_EMAIL, to_email, message.as_string())
    sender.quit()


def get_twitter_access_token():

    headers = { "Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8" }
    data = { "grant_type":"client_credentials" }
    oauth2_url = "https://api.twitter.com/oauth2/token"
    r = requests.post(oauth2_url, data=data, headers=headers, auth=(app_setting.CONSUMER_KEY, app_setting.CONSUMER_SECRET))

    print(r.json()["access_token"])
    print(r.json()["access_token"])
    print(r.json()["access_token"])
    print(r.json()["access_token"])


    return r.json()["access_token"]
