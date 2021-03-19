# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///db.db", echo=True)

Base = declarative_base()

# db = SQLAlchemy()


class Project(Base):
    __tablename__ = "project"

    name = Column(String, primary_key=True)
    description = Column(String)
    links = Column(String)


class Post(Base):
    __tablename__ = "post"

    title = Column(String, primary_key=True)
    content = Column(String)
    date = Column(DateTime)
