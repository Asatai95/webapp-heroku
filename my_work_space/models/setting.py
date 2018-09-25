from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# mysqlのDBの設定
# mysql://root@root:127.0.0.1:3306/webapp2test?charset=utf8mb4
try:
    if os.environ['DATABASE_URL']:
        DATABASE = os.environ['DATABASE_URL']
except:
    DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
        "root", # user
        "root", # password
        "127.0.0.1:3306", # host+port
        "mamp", # database name
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
