from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

import os, sys
sys.path.append(os.getcwd()) # コマンド実行ディレクトリを設定
from models.app_setting import ENGINE, Base

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key = True)
    stripe_id = Column('stripe_id', String(200))
    name = Column('name', String(45))
    password = Column('password', String(200))
    email = Column('email', String(45))
    pro_img = Column('pro_img', String(45))
    comment = Column('comment', String(45))
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
