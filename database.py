from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///db.db", echo=True, connect_args={"check_same_thread": False}
)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    links = Column(String)


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    date = Column(DateTime)

class Key(Base):
    __tablename__ = "key"

    id = Column(String, primary_key=True)
