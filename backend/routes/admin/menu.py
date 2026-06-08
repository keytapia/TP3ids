from flask import request, jsonify, Blueprint

from services.menu import (
    listar_menu,
    modificar_plato,
    eliminar_plato
)

menu_admin_bp = Blueprint('menu_admin', __name__, url_prefix='/api/admin')


# Listar el menú completo
@menu_admin_bp.route("/menu", methods=["GET"])
def get_platos():

    resultado = listar_menu()

    return jsonify(resultado), 200


# Crear un plato del menú
@menu_admin_bp.route("/menu", methods=["POST"])
def post_plato():

    data = request.get_json()

    nombre = data.get("nombre")
    descripcion = data.get("descripcion")
    precio = data.get("precio")

    if (not nombre or not precio):
        return jsonify({"error": "El nombre y el precio son obligatorios"}), 400

    # Acá va la función del servicio para crear el plato
    # resultado = crear_plato(nombre, descripcion, precio)

    # if resultado:
    #     return jsonify({"mensaje": "Plato creado exitosamente"}), 201
    # else:
    #     return jsonify({"mensaje": "No se pudo crear el plato"}), 400
    return jsonify({"mensaje": "Falta hacer función de crear plato"}), 200


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