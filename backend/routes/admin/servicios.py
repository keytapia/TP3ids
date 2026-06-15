from flask import request, jsonify, Blueprint

from services.servicios import (
    listar_servicios,
    listar_servicio_por_id,
    modificar_servicio,
    crear_servicio,
    eliminar_servicio
)

servicios_admin_bp = Blueprint('servicios_admin', __name__, url_prefix='/api/admin')


# Listar todos los servicios
@servicios_admin_bp.route('/servicios', methods=['GET'])
def get_servicios():
    
    servicios = listar_servicios()
    
    return jsonify(servicios), 200


# Listar un servicio por id
@servicios_admin_bp.route('/servicios/<int:id>', methods=['GET'])
def get_servicio_por_id(id):

    servicio = listar_servicio_por_id(id)

    return jsonify(servicio), 200


# Crear un servicio
@servicios_admin_bp.route('/servicios', methods=['POST'])
def post_servicio():
    
    data = request.get_json()

    nombre = data.get("nombre")
    disponible = data.get("disponible")

    if not nombre:
        return jsonify({"mensaje": "El nombre es obligatorio"}), 400

    nuevo_servicio = crear_servicio(nombre, disponible)

    return jsonify({"mensaje": "Servicio creado correctamente"}, nuevo_servicio), 201


# Modificar un servicio
@servicios_admin_bp.route('/servicios/<int:id>', methods=['PUT'])
def put_servicio(id):

    data = request.get_json()

    nombre = data.get("nombre")
    disponible = data.get("disponible")

    actualizado = modificar_servicio(nombre, disponible, id)

    if not actualizado:
        return jsonify({"mensaje": "No se pudo modificar el servicio"}), 404

    return jsonify({"mensaje": "Servicio actualizado correctamente"}), 200


# Eliminar un servicio
@servicios_admin_bp.route('/servicios/<int:id>', methods=['DELETE'])
def delete_servicio(id):

    eliminado = eliminar_servicio(id)

    if not eliminado:
        return jsonify({"mensaje": "No se pudo eliminar el servicio"}), 404

    return jsonify({"mensaje": "Servicio eliminado correctamente"}), 200

