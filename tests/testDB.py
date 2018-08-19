from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

CONNECT = "mysql+pymysql://blog:132942blog@localhost/BlogTest?charset=utf8mb4"

# 初始化数据库
engine = create_engine(CONNECT, echo=True)
db_session = sessionmaker(bind=engine)
session = db_session()

Base = declarative_base()

# Insert = []
