from flask import Flask, render_template, request
from database import Base, engine
from datetime import datetime

app = Flask(__name__)

Base.metadata.create_all(engine)


@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/projects")
def projects():
    return render_template("pages/projects.html")


@app.route("/contact")
def contact():
    return "contact page"


@app.route("/about/")
def about():
    return "about page"


@app.route("/addpost")
def add_post():
    return render_template("pages/add_post.html")
