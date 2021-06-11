from flask import Flask, render_template, request, redirect, url_for
from database import Base, engine, session, Post
from datetime import datetime

app = Flask(__name__)
app.run(debug=True)

Base.metadata.create_all(engine)


@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/blog")
def blog():
    posts = session.query(Post).all()

    return render_template("pages/blog.html", posts=posts)


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


@app.route("/added", methods=["POST"])
def added():
    title = request.form["title"]
    content = request.form["content"]
    date = request.form["date"]
    
    if date == "":
        date=datetime.now()

    post = Post(title=title, content=content, date=date)
    session.add(post)
    session.commit()

    return redirect(url_for("blog", id=post.id))


@app.route("/blog/<int:id>")
def post(id):
    post = session.query(Post).filter(Post.id == id).one()

    return render_template("pages/post.html", post=post)
