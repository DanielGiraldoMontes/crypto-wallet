import os

from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()


def create_app(script_info=None):
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    db.init_app(app)
    migrate.init_app(app, db)

    from app.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.wallet import wallet_bp
    app.register_blueprint(wallet_bp)

    @app.route('/')
    def hello_world():
        return render_template('index.html')

    return app
