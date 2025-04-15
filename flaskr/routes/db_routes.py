# routes/db_routes.py
from flask import Blueprint, jsonify

db_bp = Blueprint('db_routes', __name__)

@db_bp.route('/usuarios')
def obtener_usuarios():
    # Aquí iría tu lógica para acceder a la BD
    return jsonify({"mensaje": "Aquí se mostrarán los usuarios"})
