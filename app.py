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

@route('/users/logout')
def logout():
        logout_user()
        return template('templates/users/logout', url=url, current_user=None)


@route('/static/<filepath:path>', name='static_file')
def server_static(filepath):
        return static_file(filepath, root='static')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
