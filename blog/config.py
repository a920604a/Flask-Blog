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
