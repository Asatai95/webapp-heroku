# -*- coding: utf_8 -*-
# coding: UTF-8
import sqlalchemy
from sqlalchemy import exc
from setting import session
from user import *
from img import *
from bottle import get, route, run, template, static_file, request, redirect, response, view, url
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import message
from email import charset
import email
import base64
import smtplib
import os
import stripe
import sys
import requests

UPLOAD_FOLDER = './static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'gif'])
path = './static/img/*.ALLOWED_EXTENSIONS'

def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

charset.add_charset('utf-8', charset.SHORTEST, None, 'utf-8')
cset = 'utf-8'
sys.setrecursionlimit(30000)
#
# stripe_keys = {
#   'secret_key': os.environ['SECRET_KEY'],
#   'publishable_key': os.environ['PUBLISHABLE_KEY']
# }
#
# stripe.api_key = stripe_keys['secret_key']

def test():

    if request.urlparts.path == 'https://webapp2-heroku.herokuapp.com':
        url = request.urlparts.path.replace('https://webapp2-heroku.herokuapp.com', 'https://www.webapp2.com', 1)
        code = 301
        return redirect(url, code=code)


@route("/static/:path#.+#", name='static')
def test(path):
    return static_file(path, root='static')

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/img")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")


@route('/oauth2callback')
def callback():

    return template('templates/google')

@route("/")
def top():

    error = ""
    return template("templates/tatume", error=error)

@route('/', method='POST')
def create():

    log_id_new = request.forms.log_id_new
    passwd_new = request.forms.passwd_new
    user_name = request.forms.user_name
    print(log_id_new)
    print(passwd_new)
    print(user_name)


    user = User()
    user.name = str(user_name)
    user.passwd = str(passwd_new)
    user.email = str(log_id_new)
    print('test')


    user = User()
    users_sub = session.query(User.passwd).filter(User.passwd==passwd_new).all()
    print(users_sub)

    if users_sub == [ ]:
        users = session.add(user)
        session.commit()
        print(users)

    else:

        print('test')
        return template('templates/tatume')
    return redirect('/info')


@route("/info")
def info():

    return template('templates/info')


@route("/img")
def img():

    img = Img()

    imgs = session.query(Img.image)

    session.commit()


    for img in imgs:
        print(img)

    return template('templates/image', imgs=imgs)



@route('/new')
def new_test():

    error= ''
    return template('templates/create', error=error)

# @route("/new", method='POST')
# def new():
#
#     user_name = request.forms.user_name
#     passwd_new = request.forms.new_passwd
#     log_id_new = request.forms.new_log_id
#     print(log_id_new)
#     print(passwd_new)
#     print(user_name)
#
#     try:
#         user = User()
#         user.name = str(user_name)
#         user.passwd = str(passwd_new)
#         user.email = str(log_id_new)
#         print('test')
#
#         users = session.add(user)
#         session.commit()
#         print(users)
#
#
#         return redirect('/info')
#
#
#     except exc.InvalidRequestError :
#
#         error = 'すでに登録されているパスワードです。'
#         print('test')
#
#         return template('templates/create', error=error)
#
#     except exc.IntegrityError:
#
#         error = 'すでに登録されているパスワードです。'
#         print('test')
#
#         return template('templates/create', error=error)





#
# @route("/test")
# @view("test")
# def test_view():
#
#     return dict(key=stripe_keys['publishable_key'])
#
# @route("/test", method='POST')
# def test_sub():
#
#     db = MySQLdb.connect(user='b292b90b1818e0', passwd='4346c8fc', host='us-cdbr-iron-east-01.cleardb.net', db='heroku_ae66112c0cf1b10', charset='utf8')
#     con = db.cursor()
#
#     sql = 'select test from test where id = 1'
#     test = con.execute(sql)
#     db.commit()
#
#     result = con.fetchall()
#     result = result[0][0]
#
#     amount = '500'
#
#     stripe_token = request.forms.get('stripeToken')
#     mail_address = request.forms.get('stripeEmail')
#
#     stripe.api_key = stripe_keys['secret_key']
#
#     stripe.Charge.create(
#         amount=amount,
#         currency="jpy",
#         description="Charge for {mail}".format(mail=mail_address),
#         source=stripe_token
#     )
#
#     gmail_usr = 'defense433@gmail.com'
#     gmail_password = 'Asatai95!'
#     you = mail_address
#     jp_encoding = 'iso-2022-jp'
#     mail_subject = '〇〇商品について'
#     body = 'text.txt'
#     sender_name = u"OkiDoki株式会社"
#
#     with open(body, 'r', encoding='utf-8') as file:
#         body = file.read()
#
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#
#     server.ehlo()
#
#     server.starttls()
#
#     server.ehlo()
#
#     server.login(gmail_usr, gmail_password)
#
#
#     if server is not False:
#
#         msg = MIMEText(body.encode(jp_encoding), "plain", jp_encoding)
#
#         from_jp = Header(sender_name, jp_encoding)
#         msg['From'] = from_jp
#         From = gmail_usr
#         msg['Subject'] = Header(mail_subject, jp_encoding)
#         msg['To'] = you
#         to = msg['To']
#
#         server.sendmail(From, to, msg.as_string())
#
#
#         print('Email')
#         if server is not False:
#             message = '確かに支払いは完了しました。'
#             return template('message' ,message=message, main=result)
#
#         server.close()
#
#     else:
#
#         print('test')
#
#         return template("top", amount=amount)

@route('/text')
def text():

    message = 'データベースの中身を公開するよー！！'

    db = sqlalchemy.connect(user='root', passwd='root', host='localhost', db='mamp', charset='utf8')
    con = db.cursor()

    sql = 'select user from name where id = 1'
    test = con.execute(sql)
    db.commit()

    result = con.fetchall()
    result = result[0][0]

    return template('message', message=message, main=result)

@route('/text', method='POST')
def text_db():

    message = 'データベースの中身を公開するよー！！'

    form = request.forms.form
    print(form)

    db = MySQLdb.connect(user='b292b90b1818e0', passwd='4346c8fc', host='us-cdbr-iron-east-01.cleardb.net', db='heroku_ae66112c0cf1b10', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'insert into test(test) values(%s)'
    text = con.execute(sql, [str(form)])
    db.commit()
    print(text)

    result = con.fetchall()
    print(result)

    return template('message', main=form, message=message)

@route('/text_sub')
def text_db():

    img_sub = 'static/img/ninwanko.png'

    return template('img', img_sub=img_sub)

@route('/text_sub', method='POST')
def text_db():

    img_file = request.files.img_file
    print(img_file)

    if img_file and allowed_file(img_file.filename):
        filename = img_file.filename
        img_file.save(os.path.join(UPLOAD_FOLDER, filename))
        path = UPLOAD_FOLDER + filename
        print(path)

        db = MySQLdb.connect(user='b292b90b1818e0', passwd='4346c8fc', host='us-cdbr-iron-east-01.cleardb.net', db='heroku_ae66112c0cf1b10', charset='utf8')
        con = db.cursor()
        print('???')

        sql = 'insert into test(img) values(%s)'
        test = con.execute(sql, [path])
        db.commit()
        print(test)

        result = con.fetchall()
        print(result)

        return template('img', img_sub=path)

@route('/view')
def view():

    return template('singlepage_template_sample')

@route('/test_main')
def test_main():

    hello_str = hello()
    return template('templates/index', hello=hello_str)


run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
