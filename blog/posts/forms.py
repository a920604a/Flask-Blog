'''
Author: yuan
Date: 2021-05-24 13:41:38
LastEditTime: 2021-05-25 11:22:27
FilePath: /python-flask/blog/posts/forms.py
'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_pagedown.fields import PageDownField

from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")

class PageDownForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = PageDownField("Content", validators=[DataRequired()])
    submit = SubmitField('Post')
