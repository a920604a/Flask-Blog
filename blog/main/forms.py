'''
Author: yuan
Date: 2021-05-24 21:31:51
LastEditTime: 2021-05-24 21:38:08
FilePath: /python-flask/blog/main/forms.py
'''
from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import SubmitField


class PageDownFormExample(FlaskForm):
    #  加入一個form，單純的一個PageDownField跟提交欄位測試
    pagedown = PageDownField('Enter your markdown')
    submit = SubmitField('Submit')