from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

import os, sys
sys.path.append(os.getcwd()) # コマンド実行ディレクトリを設定
from models.app_setting import ENGINE, Base


class Comment(Base):
    __tablename__ = 'pro_comment'
    id = Column('id', Integer, primary_key = True)
    pro_comment = Column('pro_comment', String(200))
    user_id = Column('user_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())

def main(args):
    """
    メイン関数
    """
    if args[1] == "create":
        Base.metadata.create_all(bind=ENGINE)

    elif args[1] == "delete":
        Tweet_comment.__table__.drop(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)
