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
except:
    # for development
    SECRET_KEY = '2fsKgOLaAHbJUbi6kJsyboVLPchUjL88iZ7sM3A1'
    HOST_PASSWORD = 'PassWord'
    FACEBOOK_ID = '2165553107045876'
    FACEBOOK_SECRET = '2b3f9337bb73847b0a63846a74cb5bf7'
    FACEBOOK_CALLBACK_URL = 'http://localhost:5000/facebook/callback'
    DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
       "root", # user
       "root", # password
       "127.0.0.1:3306", # host+port
       "webapp2_sample_development", # database name
    ) # mysql://ユーザー名:パスワード@ホスト/データベース名

# mysqlのDBの設定
"""
LOCALとHEROKUで、データベースを切り替える
HEROKUで clearDB をつくると CLEARDB_DATABASE_URL という環境変数がセットされる
これはデータベースにアクセスするための情報になっている。
Pythonのアプリケーションが動作する環境(LOCALlかHEROKU)によってデータベースの
アクセス先を切り替える処理をしないといけない。今回は CLEARDB_DATABASE_URL という
環境変数があるかないかで判定します。
ただ、LOCALでは そのような環境変数が設定されていないのでエラーがでてしまいます。
なので例外処理を用いて エラーが出たときは LOCAL にするという処理をしておきます。
キーワード：例外処理
"""

"""
変数 中身が変わるかもしれない
定数 中身は上書きしないもの(上書きは可能)
"""


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
