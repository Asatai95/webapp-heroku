import os
from bottle import  (
    route, run, template, static_file, url, get, post,
    request, response, redirect, hook,
)

# database
from app_setting import session
from models.user import User

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

@route('/top')
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
@route('/users/sns')
def sns():

    redirect('/')

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
    # print('r.url:', r.url)
    # print('r: ', vars(r))
    # return r.url
    # redirect_url = r.url

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
                    'redirect_uri': app_setting.FACEBOOK_CALLBACK_URL,
                    'client_id': app_setting.FACEBOOK_ID,
                    'client_secret': app_setting.FACEBOOK_SECRET,
                    'code': request.GET.getunicode('code'),
            }
            r = requests.get(url, params=params)
            access_token = r.json()['access_token']

            """
            取得したアクセストークンが不正じゃないか確認する
            """
            url = 'https://graph.facebook.com/debug_token'
            params = {
                'input_token': access_token,
                'access_token': '%s|%s' % (app_setting.FACEBOOK_ID, app_setting.FACEBOOK_SECRET)
            }
            r = requests.get(url, params=params)
            print(r.json())

            if r.json()['data']['is_valid']:
                """
				アクセストークンが不正じゃないことがわかったら
				アクセストークンをもとにユーザーの情報を取得する
				"""
                url = 'https://graph.facebook.com/%s' % (r.json()['data']['user_id'])
                params = {
                    'fields': 'name, email',
                    'access_token': access_token,
                }

                r = requests.get(url, params=params)

                login_sns = user_sns_login(r.json())
                if login_sns == True:
                    print(r.json())
                    redirect('/users/check')
                else:
                    print(r.json())
                    user = create_user_sns(r.json())
                    redirect('/users/check_account')
            else:
    			# アクセストークンが不正なものだったらログイン画面にリダイレクトする
                redirect('/users/login')

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
