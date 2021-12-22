import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

#Global
db = SQLAlchemy()
migrate = Migrate()

def init_app():
    """Initialize app and plugins"""
    #Main
    app = Flask(__name__)
    app.config.from_object(config.Config)

    #Database
    db.init_app(app)
    migrate.init_app(app, db)

    #Context
    with app.app_context():
        from . import views, api
        from .commands import fetch_entries

        db.create_all()

        return app
