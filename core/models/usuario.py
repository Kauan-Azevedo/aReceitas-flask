from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    nome: str = db.Column(db.String(200), nullable=False)
    senha: str = db.Column(db.String(36), nullable=False)
    email: str = db.Column(db.String(200), nullable=False, unique=True)
    cpf: str =db.Column(db.String(15), nullable=False, unique=True)