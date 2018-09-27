from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
import sys

if __name__ == "__main__":
    from setting import Base
    from setting import ENGINE
else:
    from .setting import Base
    from .setting import ENGINE

class Img(Base):

    __tablename__ = 'imgs'
    id = Column('id', Integer, primary_key = True)
    img_url = Column('img_url', String(200))
    tweet_id = Column('tweet_id', Integer)
    user_id = Column('user_id', Integer)
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
