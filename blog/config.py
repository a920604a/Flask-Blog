"""
Author: yuan
Date: 2021-05-24 15:39:59
LastEditTime: 2021-05-25 13:00:30
FilePath: /python-flask/blog/config.py
"""
"""
Author: yuan
Date: 2021-05-24 15:39:59
LastEditTime: 2021-05-25 12:51:52
FilePath: /python-flask/blog/config.py
"""

import os
import secrets

class Config:

    # SECRET_KEY = os.environ.get("SECRET_KEY")
    SECRET_KEY = secrets.token_hex(16)  # carefully
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQL_DB_URL")

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
