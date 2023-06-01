from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLACHEMY_DATABASE_URI')
db = SQLAlchemy(app)

from core.routes.receitas import receitas_bp
app.register_blueprint(receitas_bp)


@app.route('/', methods=['GET'])
def home():
    return 'aReceitas API!'

if __name__ == "__main__":
    app.run(debug=True)
