from flask import Blueprint, Response, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from core.models.user import User
from core.app import db
from flask_login import login_required, logout_user


auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/cadastro', methods=['POST'])
def cadastro() -> Response:
    data = request.get_json()
    email = data["email"]
    senha = data["senha"]
    nome = data["nome"]
    cpf = data["cpf"]

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"error": True, "messsage": "Email já registrado no banco!"})
    if senha is None:
        return jsonify({"error": True, "message": "Senha inválida!"})

    new_user = User(nome=nome, email=email, senha=generate_password_hash(
        senha, method="sha256"), cpf=cpf)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "message": "Cadastro realizado com sucesso!"})


@auth_blueprint.route("/login", methods=['POST'])
def login() -> Response:
    data = request.get_json()
    email = data['email']
    senha = data["senha"]

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.senha, senha):
        return jsonify({"error": True, "message": "Usuário não existente"})

    from flask_login import login_user

    login_user(user, remember=True)

    return jsonify({"success": True, "message": "Login realizado com sucesso!"})


@auth_blueprint.route("/logout", methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"success": False, "message": "Sessão encerrada com sucesso"})
