import os
from bottle import  (
        route, run, template, static_file, url, get, post,
)

# database
from models.setting import *
from models.user import *

@route('/')
def index():
        return template('templates/index',url=url)

@route('/users/sign_up', method="GET")
def users_new():
        return template('templates/users/new', url=url)

@route('/users/sign_up', method="POST")
def users_create():
        return template('templates/users/create', url=url)

@route('/static/<filepath:path>', name='static_file')
def server_static(filepath):
        return static_file(filepath, root='static')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)