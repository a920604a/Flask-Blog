'''
Author: yuan
Date: 2021-05-24 13:40:51
LastEditTime: 2021-05-25 12:40:21
FilePath: /python-flask/blog/main/routes.py
'''

from blog.models import Post
from flask import Blueprint, render_template, request
import markdown

# import markdown
# from blog.main.forms import PageDownFormExample




main = Blueprint("main", __name__)



@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)




@main.route("/about")
def about():
    with open('./blog/about.md') as f:
        text = f.read()
    post = markdown.markdown(text)
    return render_template("about.html", title="About", post = post)
