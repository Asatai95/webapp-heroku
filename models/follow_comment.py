from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

import os, sys
sys.path.append(os.getcwd()) # コマンド実行ディレクトリを設定
from models.app_setting import ENGINE, Base


class Follow_comment(Base):
    __tablename__ = 'follow_comment'
    id = Column('id', Integer, primary_key = True)
    comment = Column('comment', String(45))
    

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
