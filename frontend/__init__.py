
'''
This file is used for base configurtion of the Flask app which runs the forntend service.

Creates the base flask app,
1. integrated with SQL-Alchemy for Database integration
2. flask-login app for handling user login sessions in the init_app
3. registers all the blueprints that consists routes to various services and pages.
'''

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)


    login_manager.init_app(app)
    login_manager.login_view = "auth.login"


    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # blueprint for non-auth parts of app
    from .services import services as services_blueprint
    app.register_blueprint(services_blueprint)

    from .models_db import User


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
