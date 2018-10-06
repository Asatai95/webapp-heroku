import os
from bottle import  (
    route, run, template, static_file, url, get, post,
    request, response, redirect, hook,
)

# database
from app_setting import session
from models.user import User
from models.social import Social

# library
from library import *

# setting
import app_setting

#api
import requests

# 各ルートのメソッドの実行前に実行される
@hook('before_request')
def before_action():
        global current_user
        current_user = get_current_user()

# 各ルートのメソッドreturnの後に実行される
@hook('after_request')
def after_action():
        session.close()

@route('/')
def index():
        return template('templates/index',url=url, current_user=current_user)

@route('/users/sign_up', method="GET")
def users_new():
        is_logged_in_redirect(current_user)
        duplicate_error = None
        return template('templates/users/new',url=url, current_user=current_user, user=User(), duplicate_error=duplicate_error)

@route('/users/sign_up_confirm', method="POST")
def users_new_confirm():
        is_logged_in_redirect(current_user)
        user = User(
                email=request.POST.getunicode("email"),
                password=request.POST.getunicode("password1"),
                name=request.POST.getunicode("name"),
                age=request.POST.getunicode("age"),
        )

        if is_duplicate_email(user.email):
                duplicate_error = '既に登録されているメールアドレスです'
                return template('templates/users/new', url=url, current_user=current_user, user=user, duplicate_error=duplicate_error)

        return template('templates/users/new_confirm', url=url, current_user=current_user, user=user )

@route('/users/sign_up', method="POST")
def users_create():
        is_logged_in_redirect(current_user)

        user = create_user(request.POST)
        send_mail(user.email, 'create')
        return template('templates/users/create', url=url, user=user, current_user=current_user)

@route('/users/login', method='GET')
def login_get():
        is_logged_in_redirect(current_user)
        return template('templates/users/login', url=url, current_user=current_user)

@route('/users/login', method='POST')
def login_post():
        is_logged_in_redirect(current_user)

        if authenticate(request.POST):
            redirect('/')
        else:
            return template('templates/users/login', url=url, current_user=current_user)
@route('/users/check')
def check():

    return template('templates/users/check', url=url, current_user=current_user)

@route('/users/check_account')
def check_account():

    return template('templates/users/check_account', url=url, current_user=current_user)

"""
passはスルー
"""

@route('/facebook/login')
def facebook_login():

    url = 'https://www.facebook.com/dialog/oauth'
    params = {
        'response_type': 'code',
        'redirect_uri': app_setting.FACEBOOK_CALLBACK_URL,
        'client_id': app_setting.FACEBOOK_ID
    }

    redirect_url = requests.get(url, params=params).url
    print(redirect_url)
    # print('r.url:', r.url)
    # print('r: ', vars(r))
    # return r.url
    # redirect_url = r.url

    redirect(redirect_url)

@route('/facebook/callback')
def facebook_callback():
    try: # 予期せぬエラーがでたらログイン画面にリダイレクトする
        if request.GET.getunicode('code'):
            access_token = get_facebook_access_token(request.GET.getunicode('code'))
            data = check_facebook_access_tokn(access_token)
            if data['is_valid']:
                data = get_facebook_user_info(access_token, data['user_id'])
                if check_socials(data, 'facebook'):
                    redirect('/')
                else:
                    user = create_facebook_user()
                    create_socials(user, data, 'facebook')
                    login_user(user.id)
                    redirect('/')
            else:
        		# アクセストークンが不正なものだったらログイン画面にリダイレクトする
                redirect('users/login')

    except:
        redirect('/users/login')


@route('/users/logout')
def logout():
        logout_user()
        return template('templates/users/logout', url=url, current_user=None)


@route('/static/<filepath:path>', name='static_file')
def server_static(filepath):
        return static_file(filepath, root='static')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
