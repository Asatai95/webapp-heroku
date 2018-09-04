from bottle import get, route, run, template, static_file, request, redirect, response, view
import os

@route("/static/:path#.+#", name='static')
def test(path):
    return static_file(path, root='static')

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/img")

@route('/')
def test():

    test = 'testです。'
    print(test)

    return template('test', test=test)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
