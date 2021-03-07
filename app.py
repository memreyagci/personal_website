from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/projects")
def projects():
    return "projecys page"


@app.route("/contact")
def contact():
    return "contact page"


@app.route("/about/")
def about():
    return "about page"
