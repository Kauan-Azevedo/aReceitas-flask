from typing import Literal
from flask import Blueprint, jsonify, request, Response
from core.app import db
from core.models.recipe import Recipe

recipe_blueprint = Blueprint('recipe', __name__)


@recipe_blueprint.route("/recipes")
def get_all():
    recipes = Recipe.query.all()
    return jsonify([recipe.serialize() for recipe in recipes])


@recipe_blueprint.route("/recipes", methods=["POST"])
def send_recipe():
    data = request.get_json()
    new_recipe = Recipe(nome=data["nome"], ingredientes=data['ingredientes'],
                        instrucoes=data['instrucoes'], descricao=data['descricao'], Usuario_id=data["usuario_id"])
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify(new_recipe.serialize()), 201


@recipe_blueprint.route("/recipes/<int:recipe_id>")
def get_single_recipe(recipe_id) -> tuple[Response, Literal[404]] | Response:
    recipe: Recipe = Recipe.query.get(recipe_id)
    if recipe is None:
        return jsonify({'error': 'Recipe not found!'}), 404
    return jsonify(recipe.serialize())


@recipe_blueprint.route("/recipes/<int:recipe_id>", methods=['DELETE'])
def delete_recipe(recipe_id) -> tuple[Response, Literal[404]] | tuple[Response, Literal[200]]:
    recipe: Recipe = Recipe.query.get(recipe_id)
    if recipe is None:
        return jsonify({"error": "Recipe not found!"}), 404
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"success": "Recipe deleted"}), 200
