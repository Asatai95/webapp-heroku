from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting_sub import Base
from setting_sub import ENGINE
import sys

class User(Base):
    """
    ユーザモデル
    """
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String(200))
    age = Column('age', INT() )
    email = Column('email', String(200))

def main(args):
    """
    メイン関数
    """

    if args[1] == "create":
        Base.metadata.create_all(bind=ENGINE)
    elif args[1] == "delete" :
        User.__table__.drop(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)
