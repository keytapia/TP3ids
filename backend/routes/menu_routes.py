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
        categoria = categoria.lower()
        menu = listar_menu_por_categoria(categoria)
        if not menu:
            return jsonify({"message":"No hay ningún plato en esa categoria"}), 404
        return jsonify(menu),200
    menu = listar_menu()
    return jsonify(menu), 200


#filtrar un plato especifico por numero id
@menu_bp.route('/api/menu/<int:plato_id>', methods=['GET'])
def get_plato(plato_id):
    plato = obtener_plato_id(plato_id)

    if not plato:
        return jsonify({"message": "EL plato no pudo ser encontrado"}), 404
    
    return jsonify(plato), 200