from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, BigInteger
from datetime import datetime


"""
テーブル作成はアプリのルートディレクトリで行うこと
今回で言うと webapp2-sample/
テーブル作成実行例
  webapp2-sampleがカレントディレクトリとして
    python models/social.py create
    python models/social.py delete
"""
import os, sys
sys.path.append(os.getcwd()) # コマンド実行ディレクトリを設定
from app_setting import Base, ENGINE

# usersテーブルにリレーションするために読み込む
from models.user import User



class Social(Base):
    """
    ソーシャルモデル
    """
    __tablename__ = 'socials'
    id = Column('id', Integer, primary_key = True)
    user_id = Column('user_id', Integer,  ForeignKey('users.id',onupdate='CASCADE', ondelete='CASCADE')) # ここの users.id の users はテーブル名
    provider = Column('provider', String(200))
    provider_id = Column('provider_id', BigInteger)
    created_at = Column('created_at', DateTime, default=datetime.now())

def main(args):
    """
    メイン関数
    """
    if args[1] == "create":
        Base.metadata.create_all(bind=ENGINE)

    elif args[1] == "delete":
        Social.__table__.drop(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
