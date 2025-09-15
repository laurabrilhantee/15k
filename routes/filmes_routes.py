from flask import Blueprint, request  
from controllers.filmes_controllers import get_filmes, create_filmes

filme_routes = Blueprint('filme_routes', __name__) 

@filme_routes.route('/filme', methods=['GET']) 
def filme_get():
    return get_filmes()

@filme_routes.route('/filme', methods=['POST'])
def filme_post():
    filme_data = request.json
    return create_filmes(request.json)

