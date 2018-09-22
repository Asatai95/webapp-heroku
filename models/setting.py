from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# mysqlのDBの設定
# mysql://root@root:127.0.0.1:3306/webapp2test?charset=utf8mb4
try:
    if os.environ['mysql://b292b90b1818e0:4346c8fc@us-cdbr-iron-east-01.cleardb.net/heroku_ae66112c0cf1b10']:
        DATABASE = os.environ['mysql://b292b90b1818e0:4346c8fc@us-cdbr-iron-east-01.cleardb.net/heroku_ae66112c0cf1b10']
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
