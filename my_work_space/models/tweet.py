from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

import os, sys
sys.path.append(os.getcwd()) # コマンド実行ディレクトリを設定
from models.app_setting import ENGINE, Base

class Tweet(Base):
    __tablename__ = 'tweet'
    id = Column('id', Integer, primary_key = True)
    tweet_id = Column('tweet_id', Integer)
    user_id = Column('user_id', Integer)
    img_id = Column('img_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())

def main(args):
    """
    メイン関数
    """
    if args[1] == "create":
        Base.metadata.create_all(bind=ENGINE)

    elif args[1] == "delete":
        Tweet.__table__.drop(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)
