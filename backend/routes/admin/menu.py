from flask import request, jsonify, Blueprint

from services.menu import (
    listar_menu,
    listar_menu_por_categoria, 
    obtener_plato_id,
    modificar_plato,
    eliminar_plato,
    agregar_plato
)

menu_admin_bp = Blueprint('menu_admin', __name__, url_prefix='/api/admin')


# Listar menú (completo o por categorias)
@menu_admin_bp.route("/menu", methods=["GET"])
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
@menu_admin_bp.route('/menu/<int:id>', methods=['GET'])
def get_plato(id):
    plato = obtener_plato_id(id)

    if not plato:
        return jsonify({"message": "EL plato no pudo ser encontrado"}), 404
    
    return jsonify(plato), 200


# Crear un plato
@menu_admin_bp.route("/menu", methods=["POST"])
def crear_nuevo_plato():

    datos = request.get_json()

    resultado = agregar_plato(
        categoria_id=datos["categoria_id"],
        nombre=datos["nombre"],
        precio=datos["precio"],
        imagen=datos["imagen"],
        descripcion=datos.get("descripcion"),
        restricciones_alimentarias=datos.get("restricciones_alimentarias"),
        disponible=datos.get("disponible", True)
    )

    if resultado["ok"]:
        return jsonify(resultado), 201

    return jsonify(resultado), 400


# Modificar un plato del menú
@menu_admin_bp.route("/menu/<int:id>", methods=["PUT"])
def put_plato(id):

    data = request.get_json()

    if modificar_plato(id, data) == 0:
        return jsonify({"error": "Plato no encontrado"}), 404

    return jsonify({"mensaje": "Plato modificado exitosamente"}), 200


# Eliminar un plato del menú
@menu_admin_bp.route("/menu/<int:id>", methods=["DELETE"])
def delete_plato(id):

    if eliminar_plato(id) == 0:
        return jsonify({"error": "Plato no encontrado"}), 404

    return jsonify({"mensaje": "Plato eliminado exitosamente"}), 200