from models.filmes_models import Filme
from db import db
import json
from flask import make_response

def get_filmes():
    filmes = Filme.query.all()
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de filmes.',
            'dados': [filmes.json() for filmes in filmes]
        }, ensure_ascíí=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def create_filmes(filmes_data):
    if not all(key in filmes_data for key in ['Título', 'Gênero', 'Duração', 'Lançamento', 'Diretor']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Título, Gênero, Duração, lançamento e Diretor são obrigatórios.'}, ensure_ascíí=False),
            400
        )
        response.headers['Content.Type']= 'application/json'
        return response
    
    novo_filme = Filme(
        id =filmes_data['id'],  
        Titulo=filmes_data['Titulo'],  
        Genero=filmes_data['Genero'],    
        Duracao=filmes_data['Duracao'],
        Lancamento=filmes_data['lancamento'],
        Diretor=filmes_data['Diretor'],
    )
    db.session.add(novo_filme)
    db.session.commit()
    response = make_response(
        json.dumps({  
            'mensagem': 'Filme cadastrado com sucesso.',  
            'filmes': novo_filme.json()  
        },ensure_ascii=False, sort_keys=False)  
    )
    response.headers['content-Type'] = 'application/json'
    return response
