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
    python models/plan.py create
    python models/plan.py delete
"""
import os, sys
sys.path.append(os.getcwd()) # コマンド実行ディレクトリを設定
from app_setting import Base, ENGINE, session




class Plan(Base):
    """
    プラン
    """
    __tablename__ = 'plans'
    id = Column('id', Integer, primary_key = True)
    stripe_plan_id = Column('stripe_plan_id', String(255))
    product_name = Column('product_name', String(255))
    name = Column('name', String(255))
    namespace = Column('namespace', String(255))
    amount = Column('amount', Integer)
    detail = Column('detail', String(255))
    created_at = Column('created_at', DateTime, default=datetime.now())

def main(args):
    """
    メイン関数
    """
    if args[1] == "create":
        Base.metadata.create_all(bind=ENGINE)

    elif args[1] == "delete":
        Plan.__table__.drop(bind=ENGINE)

    elif args[1] == "maketestdata":
        """
        [StripeプランID, Stripeプラン名, 金額]
        StripeプランIDは各自でつくったものを用意してください
        """
        datas = [
            ['plan_DmJAmdIJgDeQrl', 'ビギナープラン', 'beginner', 380],
            ['plan_DmJBmSkZsnm8z1', 'スタンダードプラン', 'standard', 1000],
            ['plan_DmJCkiLukDd4cY', 'プロフェッショナルプラン', 'professional', 2000],
        ]
        for data in datas:
            plan = Plan(
                stripe_plan_id=data[0],
                product_name='WEBプログラミングコース',
                name=data[1],
                namespace=data[2],
                amount=data[3],
                detail='テキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキスト',
            )
            session.add(plan)
            session.commit()
        session.close()

if __name__ == "__main__":
    main(sys.argv)
