from typing import Literal
from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        "SQLALCHEMY_DATABASE_URI")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from core.routes.user_routes import user_blueprint
    from core.routes.recipe_routes import recipe_blueprint

    app.register_blueprint(user_blueprint)
    app.register_blueprint(recipe_blueprint)

    @app.route("/")
    def home() -> tuple[Response, Literal[200]]:
        return jsonify({"success": True, "message": "aReceitas API"}), 200

    return app