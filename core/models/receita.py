from html import unescape
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Receita(db.Model):
    __tablename__: str = 'Receita'
    id: int = db.Column(db.Integer, primary_key=True)
    nome: str = db.Column(db.String(200), nullable=False, unique=True)
    ingredientes: str = db.Column(db.String, nullable=False)
    instrucoes: str = db.Column(db.String, nullable=False)
    descricao: str = db.Column(db.String, nullable=False)
    Usuario_id: int = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=False)

    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            "nome": unescape(self.nome),
            "ingredientes": unescape(self.ingredientes),
            "instrucoes": unescape(self.instrucoes),
            "descricao": unescape(self.descricao),
            "Usuario_id": self.Usuario_id
        }