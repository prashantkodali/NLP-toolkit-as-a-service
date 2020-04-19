from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)


    login_manager = LoginManager()
    login_manager.init_app(app)

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

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(name):
        return User.query.filter_by(name=name).first()

    return app
