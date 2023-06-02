from core.app import db


class User(db.Model):
    __tablename__: str = "Usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    senha = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(300), nullable=False)
    cpf = db.Column(db.String(22), nullable=False)

    recipes = db.relationship('Recipe', backref='user', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'senha': self.senha,
            'email': self.email,
            'cpf': self.cpf
        }
