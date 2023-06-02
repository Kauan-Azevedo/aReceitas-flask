from core.app import db
from core.models.user import User


class Recipe(db.Model):
    __tablename__ = 'Receita'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(), nullable=False)
    ingredientes = db.Column(db.String(1000), nullable=False)
    instrucoes = db.Column(db.String(2000), nullable=False)
    descricao = db.Column(db.String(1000), nullable=False)

    Usuario_id = db.Column(db.Integer, db.ForeignKey(
        'Usuario.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'ingredientes': self.ingredientes,
            'instrucoes': self.instrucoes,
            'descricao': self.descricao,
            'Usuario_id': self.Usuario_id
        }
