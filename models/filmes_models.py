from db import db

class Filme(db.Model):
    __tablename__ = 'filmes'

    id = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(80), nullable=False)
    Genero = db.Column(db.String(80), nullable=False)
    Duracao = db.Column(db.String(80), nullable=False)
    Lancamento = db.Column(db.Integer, nullable=False)
    Diretor = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'Titulo': self.titulo,           
            'Genero': self.genero,    
            'Duracao': self.duracao,      
            'Lancamento': self.Lancamento,
            'Diretor': self.diretor           
        }
     