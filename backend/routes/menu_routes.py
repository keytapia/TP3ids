from flask import Flask, request, jsonify, Blueprint
from datetime import datetime

from backend.services.menu_service import (
    listar menu
    obtener_plato_id
    listar_menu_por_categoria
)

menu_bp = Blueprint('menu', __name__)

#filtrar menu completo o por categoria
@menu_bp.route('/api/menu', methods=['GET'])
def get_menu():
    categoria = request.args.get('categoria')

    if categoria:
        menu = listar_menu_por_categoria(categoria)
        
        if not menu:
            return jsonify({"mensaje":"No hay platos en esa categoria"}), 404
    else:
        menu = listar_menu

    return jsonify(menu), 200


#filtrar un plato especifico por numero id
@menu_bp.route('/api/menu/<int:plato_id>', methods=['GET'])
def get_plato(plato_id):
    plato = obtener_plato_id(plato_id)

    if not plato:
        return jsonify({"mensaje": "plato no encontrado"}), 404
    
    return jsonify(plato), 200