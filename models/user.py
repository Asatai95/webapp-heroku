from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime


"""
テーブル作成はアプリのルートディレクトリで行うこと
今回で言うと webapp2-sample/
テーブル作成実行例
  webapp2-sampleがカレントディレクトリとして
    python models/user.py create
    python models/user.py delete
"""
import os, sys
sys.path.append(os.getcwd()) # コマンド実行ディレクトリを設定
from app_setting import ENGINE, Base



class User(Base):
    """
    ユーザモデル
    """
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))
    password = Column('password', String(200))
    created_at = Column('created_at', DateTime, default=datetime.now())

def main(args):
    """
    メイン関数
    """
    if args[1] == "create":
        Base.metadata.create_all(bind=ENGINE)

    elif args[1] == "delete":
        User.__table__.drop(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
