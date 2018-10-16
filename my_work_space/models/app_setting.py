from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import os

try:
    # for HEROKU
    if os.environ['APP_ENVIRONMENT'] == 'production':
        SECRET_KEY = os.environ['SECRET_KEY']
        HOST_PASSWORD = os.environ['HOST_PASSWORD']
        FACEBOOK_ID = os.environ['FACEBOOK_ID']
        FACEBOOK_SECRET = os.environ['FACEBOOK_SECRET']
        FACEBOOK_CALLBACK_URL = os.environ['FACEBOOK_CALLBACK_URL']
        DATABASE = os.environ['DATABASE_URL']
        STRIPE_SECRET = os.environ['SECRET_KEY']
        STRIPE_PUBLISHABLE = os.environ['PUBLISHABLE_KEY']
        CONSUMER_KEY = os.environ['CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
except:
    # for development
    SECRET_KEY = '2fsKgOLaAHbJUbi6kJsyboVLPchUjL88iZ7sM3A1'
    HOST_PASSWORD = 'PassWord'
    FACEBOOK_ID = '469722980181511'
    FACEBOOK_SECRET = '67fcea638494b27eeb9e46756d195e75'
    FACEBOOK_CALLBACK_URL = 'http://localhost:5000/facebook/callback'
    STRIPE_SECRET = 'sk_test_RcPOmGOhD54o5kg6ixEr3yQZ'
    STRIPE_PUBLISHABLE = 'pk_test_8j23sG5Ssj7DKgN4CsIyRlNX'
    HOST_EMAIL = 'official@webapp2.com'
    HOST_PASSWORD = 'asatai951156'
    HOST_SMTP = 'smtp.muumuu-mail.com'
    CONSUMER_KEY = 'b5Ud0FkI8ldJMjXF8yKP5OXuJ'
    CONSUMER_SECRET = '8DWwAjpfLwwo96kP9Dcmq1GeY9V7esHkv6uwXJM342jvHiQgEC'
    DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
       "root", # user
       "root", # password
       "127.0.0.1:3306", # host+port
       "mamp", # database name
    ) # mysql://ユーザー名:パスワード@ホスト/データベース名

ENGINE = create_engine(
    DATABASE,
    encoding = "utf8",
    echo=True, # Trueだと実行のたびにSQLが出力される
    pool_pre_ping=True
)

# Sessionの作成
session = scoped_session(
        sessionmaker( # ORM実行時の設定。自動コミットするか、自動反映するなど。
            autocommit = False,
            autoflush = False,
            bind = ENGINE
            )
        )

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
