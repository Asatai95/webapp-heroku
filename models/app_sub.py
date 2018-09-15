import os
from setting_sub import session
from setting_sub import *
from user_sub import *
from bottle import template, run, redirect, get, route, static_file, request, response, view, url



@route("/static/:path#.+#", name='static')
def test(path):
    return static_file(path, root='static')

@route("/users")
def top():

    users = session.query(User).all()
    return template('templates/users', users=users)


run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
