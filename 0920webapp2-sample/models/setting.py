from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import os

# mysqlのDBの設定
"""
LOCALとHEROKUで、データベースを切り替える
HEROKUで clearDB をつくると CLEARDB_DATABASE_URL という環境変数がセットされる
これはデータベースにアクセスするための情報になっている。
Pythonのアプリケーションが動作する環境(LOCALlかHEROKU)によってデータベースの
アクセス先を切り替える処理をしないといけない。今回は CLEARDB_DATABASE_URL という
環境編素があるかないかで判定します。
ただ、LOCALでは そのような環境変数が設定されていないのでエラーがでてしまいます。
なので例外処理を用いて エラーが出たときは LOCAL にするという処理をしておきます。
キーワード：例外処理
"""
try:
    if os.environ['DATABASE_URL']:
        DATABASE = os.environ['DATABASE_URL']
except:
    DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
        "root", # user
        "root", # password
        "127.0.0.1:3306", # host+port
        "webapp2_sample_development", # database name
    )

ENGINE = create_engine(
    DATABASE,
    encoding = "utf8",
    echo=True # Trueだと実行のたびにSQLが出力される
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
