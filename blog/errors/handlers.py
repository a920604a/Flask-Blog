'''
Author: yuan
Date: 2021-05-24 16:15:00
LastEditTime: 2021-05-24 16:25:22
FilePath: /python-flask/blog/errors/handlers.py
'''
from flask import Blueprint, render_template
from flask import jsonify

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    # return render_template('errors/500.html'), 500
    return jsonify(code=500, msg="服务器异常,500")
