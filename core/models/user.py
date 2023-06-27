
from core.app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "Usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    senha = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(300), nullable=False)
    cpf = db.Column(db.String(22), nullable=False)

    recipes = db.relationship('Recipe', backref='user', lazy=True)

    def serialize(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf
        }
