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
        STRIPE_KEYS_SECRET_KEY = os.environ['SECRET_KEY']
        STRIPE_KEYS_PUBLISHABLE_KEY = os.environ['PUBLISHABLE_KEY']
except:
    # for development
    SECRET_KEY = '2fsKgOLaAHbJUbi6kJsyboVLPchUjL88iZ7sM3A1'
    HOST_PASSWORD = 'PassWord'
    FACEBOOK_ID = '469722980181511'
    FACEBOOK_SECRET = '67fcea638494b27eeb9e46756d195e75'
    FACEBOOK_CALLBACK_URL = 'http://localhost:5000/facebook/callback'
    DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
       "root", # user
       "root", # password
       "127.0.0.1:3306", # host+port
       "mamp", # database name
    ) # mysql://ユーザー名:パスワード@ホスト/データベース名

# stripe_keys = {
#   'secret_key': os.environ['SECRET_KEY'],
#   'publishable_key': os.environ['PUBLISHABLE_KEY']
# }
#
# stripe.api_key = stripe_keys['secret_key']

STRIPE_KEYS_SECRET_KEY = 'sk_test_7HfVra2HNiZZMFX4y9qgrhb8'
STRIPE_KEYS_PUBLISHABLE_KEY = 'pk_test_6f1H3GnB57e4UQDSlMQBCPZ6'

HOST_EMAIL = 'official@webapp2.com'
HOST_PASSWORD = 'asatai951156'
HOST_SMTP = 'smtp.muumuu-mail.com'

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
