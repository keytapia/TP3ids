from flask import Flask, request, jsonify, Blueprint

servicios_bp = Blueprint('servicios', __name__)

from services.servicios_service import (
	listar_servicios, 
	modificar_servicio, 
	crear_servicio, 
	eliminar_servicio
)


# Listar todos los servicios
@servicios_bp.route('/api/servicios', methods=['GET'])
def get_servicios():
    
    servicios = listar_servicios()
    
    return jsonify(servicios), 200


# Crear un servicio
@servicios_bp.route('/api/servicios', methods=['POST'])
def post_servicio():
    
    data = request.get_json()

    nombre = data.get("nombre")
    descripcion = data.get("descripcion")

    if not nombre:
        return jsonify({"mensaje": "El nombre es obligatorio"}), 400

    servicio = crear_servicio(nombre, descripcion)

    return jsonify({"mensaje": "Servicio creado correctamente"}), 201


# Modificar un servicio
@servicios_bp.route('/api/servicios/<int:id>', methods=['PUT'])
def put_servicio(id):

    data = request.get_json()

    nombre = data.get("nombre")
    descripcion = data.get("descripcion")

    actualizado = modificar_servicio(nombre, descripcion, id)

    if not actualizado:
        return jsonify({"mensaje": "No se pudo modificar el servicio"}), 404

    return jsonify({"mensaje": "Servicio actualizado correctamente"}), 200


# Eliminar un servicio
@servicios_bp.route('/api/servicios/<int:id>', methods=['DELETE'])
def delete_servicio(id):

    eliminado = eliminar_servicio(id)

    if not eliminado:
        return jsonify({"mensaje": "No se pudo eliminar el servicio"}), 404

    return jsonify({"mensaje": "Servicio eliminado correctamente"}), 200