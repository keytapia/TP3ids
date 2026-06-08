from flask import request, jsonify, Blueprint

from services.menu import (
    listar_menu,
    obtener_plato_id,
    listar_menu_por_categoria, 
    listar_categorias
)

menu_bp = Blueprint('menu', __name__, url_prefix='/api')


# Filtrar menu completo o por categoria
@menu_bp.route('/menu', methods=['GET'])
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


# Filtrar un plato especifico por numero id
@menu_bp.route('/menu/<int:plato_id>', methods=['GET'])
def get_plato(plato_id):
    plato = obtener_plato_id(plato_id)

    if not plato:
        return jsonify({"message": "EL plato no pudo ser encontrado"}), 404
    
    return jsonify(plato), 200

# Listar categorias disponibles
@menu_bp.route('/categorias', methods=['GET'])
def get_categorias():
    categorias = listar_categorias()
    return jsonify(categorias), 200