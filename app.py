from bottle import get, route, run, template, static_file, request, redirect, response, view
import os

@route("/static/:path#.+#", name='static')
def test(path):
    return static_file(path, root='static')

@route('/')
def test():

    test = 'testです。'
    print(test)

    return template('test', test=test)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
