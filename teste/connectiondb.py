from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/youropinion'  # Substitua com a URI do seu banco de dados
db = SQLAlchemy(app)

# Defina o modelo da tabela
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    idade = db.Column(db.Integer)

    def __repr__(self):
        return f"<Usuario {self.nome}>"
