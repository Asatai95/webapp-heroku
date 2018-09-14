from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting import Base
from setting import ENGINE
from sqlalchemy import exc
import sys

class User(Base):
    """
    ユーザモデル
    """
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String(45))
    passwd = Column('passwd', String(45))
    email = Column('email', String(45))

def main(args):
    """
    メイン関数
    """
    try:
        Base.metadata.create_all(bind=ENGINE)

    except exc.InvalidRequestError:
         session.rollback()
         raise

    except exc.IntegrityError:
         session.rollback()
         raise

if __name__ == "__main__":
    main(sys.argv)
