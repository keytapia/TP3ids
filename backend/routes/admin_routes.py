from flask import Flask, request, jsonify, Blueprint
from datetime import datetime

from backend.services import reservas_service
from backend.services import servicios_service

admin_bp = Blueprint('admin', __name__)

# Visualizar las reservas
@admin_bp.route('/api/admin/reservas', methods=['GET'])
def get_reservas():
    reservas = reservas_service.listar_reservas()
    return jsonify(reservas)

#Visualizar el estado de las reservas (filtra por estado)
@admin_bp.route('/api/admin/reservas/estado/<estado>', methods=['GET'])
def get_reservas_por_estado(estado):
    reservas = reservas_service.listar_reservas_por_estado(estado)
    return jsonify(reservas)

# Cancelar una reserva por id cambiando su estado a "cancelada"
@admin_bp.route('/api/admin/reservas/cancelar/<int:reserva_id>', methods=['PATCH'])
def cancelar_reserva(reserva_id):
    resultado = reservas_service.cancelar_reserva(reserva_id)
    if resultado:
        return jsonify({"message": "Reserva cancelada exitosamente"})
    else:
        return jsonify({"message": "No se pudo cancelar la reserva"}), 400

# Visualizar los servicios
@admin_bp.route('/api/admin/servicios', methods=['GET'])
def get_servicios():
	servicios = servicios_service.listar_servicios()
	return jsonify(servicios)

# Modificar un servicio
@admin_bp.route('/api/admin/servicios/<id>', methods=['PUT'])
def put_servicios(id):
	data = request.json
	modificacion_servicio = servicios_service.modificar_servicio(nombre, descripcion, id)
	if modificacion_servicio:
		return jsonify({"message": "Servicio modificado exitosamente"}), 200
	else:
		return jsonify({"message": "No se pudo modificar el servicio"}), 400

# Crear un servicio
@admin_bp.route('/api/admin/servicios', methods=['POST'])
def post_servicio():
	data = request.json
	nuevo_servicio = servicios_service.crear_servicio(nombre, descripcion)
	return jsonify({"message": "Servicio creado exitosamente"}), 201

# Eliminar un servicio
@app.route('/api/admin/servicios/<id>', methods=['DELETE'])
def delete_servicio(id):
	eliminado_servicio = servicios_service.eliminar_servicio(id)
	return jsonify({"message": "Servicio eliminado exitosamente"}), 200
