from flask import Blueprint, jsonify, request
from core.models.receita import Receita
from core.app import db

receitas_bp = Blueprint('receitas', __name__)

@receitas_bp.route("/receitas", methods=["GET"])
def get_receitas():
    receitas = Receita.query.all()
    receitas_dict = [receita.to_dict() for receita in receitas]
    return jsonify(receitas_dict)


@receitas_bp.route("/receitas/<int:receita_id>", methods=["GET"])
def get_receita(receita_id):
    receita = Receita.query.get(receita_id)
    if receita is None:
        return jsonify({"error": "Receita não encontrada"}), 404
    return jsonify(receita.to_dict())

@receitas_bp.route("/receitas", methods=["POST"])
def create_receita():
    data = request.get_json()
    receita = Receita(nome=data.get("nome"), ingredientes=data.get("ingredientes"),
                      instrucoes=data.get("instrucoes"), descricao=data.get("descricao"))
    db.session.add(receita)
    db.session.commit()
    return jsonify({"message": "Receita criada com sucesso"})

@receitas_bp.route("/receitas/<int:receita_id>", methods=["PUT"])
def update_receita(receita_id):
    receita = Receita.query.get(receita_id)
    if receita is None:
        return jsonify({"error": "Receita não encontrada"}), 404

    data = request.get_json()
    receita.nome = data.get("nome")
    receita.ingredientes = data.get("ingredientes")
    receita.instrucoes = data.get("instrucoes")
    receita.descricao = data.get("descricao")

    db.session.commit()
    return jsonify({"message": "Receita atualizada com sucesso"})

@receitas_bp.route("/receitas/<int:receita_id>", methods=["DELETE"])
def delete_receita(receita_id):
    receita = Receita.query.get(receita_id)
    if receita is None:
        return jsonify({"error": "Receita não encontrada"}), 404

    db.session.delete(receita)
    db.session.commit()
    return jsonify({"message": "Receita excluída com sucesso"})
