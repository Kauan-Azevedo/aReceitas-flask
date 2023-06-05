from typing import Literal
from flask import Blueprint, jsonify, request, Response
from core.app import db
from core.models.user import User


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route("/users")
def all_users() -> Response:
    users = User.query.all()
    return jsonify([user.serialize() for user in users])


@user_blueprint.route("/users", methods=["POST"])
def create_user() -> tuple[Response, Literal[201]]:
    data = request.get_json()
    new_user = User(nome=data['nome'], senha=data['senha'],
                    email=data['email'], cpf=data['cpf'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201


@user_blueprint.route("/users/<int:user_id>")
def get_single_user(user_id: int) -> tuple[Response, Literal[404]] | tuple[Response, Literal[201]]:
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": True, "message": "Usuário não encontrado."}), 404
    return jsonify(user.serialize()), 201


@user_blueprint.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id) -> tuple[Response, Literal[404]] | tuple[Response, Literal[200]]:
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": True, "message": "Usuário não encontrado."}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"success": True, "message": "User deleted"}), 200
