"""
Author: yuan
Date: 2021-05-22 19:58:55
LastEditTime: 2021-05-24 15:40:57
FilePath: /python-flask/blog/__init__.py
"""
"""
Author: yuan
Date: 2021-05-22 19:58:55
LastEditTime: 2021-05-24 13:27:59
FilePath: /python-flask/blog/__init__.py
"""
"""
Author: yuan
Date: 2021-05-22 19:58:55
LastEditTime: 2021-05-22 20:00:36
FilePath: /python-flask/blog/__init__.py
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskext.markdown import Markdown
from flask_pagedown import PageDown

from blog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"  # this login is the function
login_manager.login_message_category = "info"
mail = Mail()


# db.create_all()
def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    Markdown(app)
    PageDown(app)

    from blog.users.routes import users
    from blog.posts.routes import posts
    from blog.main.routes import main
    from blog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    with app.app_context():
        db.create_all()
        
    return app
