from typing import Literal
from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        "SQLALCHEMY_DATABASE_URI")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from core.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    with app.app_context():
        db.create_all()

    from core.routes.user_routes import user_blueprint
    from core.routes.recipe_routes import recipe_blueprint
    from core.auth import auth_blueprint

    app.register_blueprint(user_blueprint)
    app.register_blueprint(recipe_blueprint)
    app.register_blueprint(auth_blueprint)

    @app.route("/")
    def home() -> tuple[Response, Literal[200]]:
        return jsonify({"success": True, "message": "aReceitas API"}), 200

    return app
