from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager



db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    #setups app and secret key for sessins and sqlalchemy for storing user data and instance of a app

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    #handle application and authentication routes and registers the the bluprint to organize routes

    from .models import User, Note

    with app.app_context():
        db.create_all()

    #include these functions and if db doesn't exist create

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    #if user tries to access a protected route without being logged in, they are redirected to this view
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    # tells Flask-Login how to load a user from the database:function fetches the user by their ID, which Flask-Login uses to keep track of the logged-in user.

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
#check if db exist in the same dir if not create
