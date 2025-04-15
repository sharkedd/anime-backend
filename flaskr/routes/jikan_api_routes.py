# routes/jikan_routes.py
from flask import Blueprint, request, jsonify
from ..services.jikan_api import  buscar_anime_avanzado
jikan_bp = Blueprint('jikan_routes', __name__)

@jikan_bp.route('/buscar', methods=['GET'])
def buscar_anime_route():
    nombre = request.args.get('nombre')
    if not nombre:
        return jsonify({"error": "El parámetro 'nombre' es obligatorio"}), 400
    
    query_params = {
        'q': nombre,                # El nombre del anime que se pasa desde el cliente
    }
    resultado = buscar_anime_avanzado(query_params)
    return jsonify(resultado)

@jikan_bp.route('/busqueda_avanzada', methods=['GET'])
def buscar_anime_route_avanzado():
    # request.args es un ImmutableMultiDict, se puede pasar directamente
    query_params = request.args.to_dict(flat=True)

    return jsonify(buscar_anime_avanzado(query_params))

@jikan_bp.route('/en_emision', methods=['GET'])
def buscar_animes_en_emision():
    # request.args es un ImmutableMultiDict, se puede pasar directamente
    query_params = request.args.to_dict(flat=True)
    query_params['status'] = 'airing'


    return jsonify(buscar_anime_avanzado(query_params))