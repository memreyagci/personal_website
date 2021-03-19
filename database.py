from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    links = db.Column(db.String)


class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    date = db.Column(db.DateTime)
