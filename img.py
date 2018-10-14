from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting import Base
from setting import ENGINE
from sqlalchemy import exc
import sys


class Img(Base):
    """
    画像モデル
    """
    __tablename__ = 'img'
    id = Column('id', Integer, primary_key = True)
    image = Column('image', String(45))
    date = Column('date', DateTime)

def main(args):
    """
    メイン関数
    """

    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)
