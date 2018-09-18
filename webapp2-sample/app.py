import os
from bottle import  (
        route, run, template, static_file, url, get, post,
        request, response
)

# database
from models.setting import *
from models.user import *

@route('/')
def index():

    user_id = request.get_cookie(secret='test12345678')
    current_user = session.query(User).get(user_id)
    return template('templates/index',url=url, current_user=current_user)

@route('/users/sign_up', method="GET")
def users_new():
    return template('templates/users/new', url=url)

@route('/users/sign_up', method="POST")
def users_create():

    email = request.POST.getunicode('email')
    password1 = request.POST.getunicode('password1')
    password2 = request.POST.getunicode('password2')
    name = request.POST.getunicode('name')
    age = int(request.POST.getunicode('age'))

    user = User(
            email = email,
            password = password1,
            name = name,
            age = age
    )

    session.add(user)
    session.commit()
    # session.close()

    return template('templates/users/create', url=url, user=user)
@route('/users/login', method='GET')
def login():
    current_user=None
    return template('templates/users/login', url=url, current_user=current_user)

@route('/users/login', method='POST')
def login():

    current_user=None
    email = request.POST.getunicode('email')
    password = request.POST.getunicode('password')

    user = session.query(User).filter(User.email==email, User.password==password).all()

    if user[0] is not None:
        response.set_cookie(
               'user_id', user[0].id,
               secret='test12345678',
               max_age=2678400
        )
        return template('templates/index', url=url, current_user=user[0])

    else:
        return template('templates/users/login', url=url, current_user=current_user)

@route('/static/<filepath:path>', name='static_file')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
