import os
from flask import Flask
from flask_migrate import Migrate
from config import db
import app.models
from app.routes import main_bp
from app.api_routes import api_bp

migrate = Migrate()

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))  # 현재 app/ 까지의 절대경로
    root_dir = os.path.dirname(base_dir)  # oz_form/ 폴더

    template_dir = os.path.join(root_dir, 'app', 'templates')
    static_dir = os.path.join(root_dir, 'app', 'static')

    application = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)
    migrate.init_app(application, db)

    application.register_blueprint(main_bp)
    application.register_blueprint(api_bp, url_prefix='/api')

    return application
