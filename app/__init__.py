# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# -------------------------
# EXTENSIONS
# -------------------------
db = SQLAlchemy()
login_manager = LoginManager()


# -------------------------
# APP FACTORY
# -------------------------
def create_app():
    app = Flask(__name__)

    # -------------------------
    # CONFIGURATION
    # -------------------------
    app.config["SECRET_KEY"] = "supersecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # -------------------------
    # INITIALIZE EXTENSIONS
    # -------------------------
    db.init_app(app)
    login_manager.init_app(app)

    # If user tries to access protected page without login
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "warning"

    # -------------------------
    # IMPORT MODELS (IMPORTANT)
    # -------------------------
    from .models import User, MatchHistory

    # -------------------------
    # REGISTER BLUEPRINTS
    # -------------------------
    from .auth import auth
    from .main import main

    app.register_blueprint(auth)
    app.register_blueprint(main)

    # -------------------------
    # CREATE DATABASE TABLES
    # -------------------------
    with app.app_context():
        db.create_all()

    return app