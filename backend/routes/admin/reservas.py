from flask import jsonify, Blueprint

from services.reservas import (
    listar_reservas,
    listar_reservas_por_estado,
    cancelar_reserva
)

reservas_admin_bp = Blueprint('reservas_admin', __name__, url_prefix='/api/admin')


# Visualizar las reservas
@reservas_admin_bp.route('/reservas', methods=['GET'])
def get_reservas():
    
    reservas = listar_reservas()
    
    return jsonify(reservas), 200


# Visualizar el estado de las reservas (filtra por estado)
@reservas_admin_bp.route('/reservas/estado/<estado>', methods=['GET'])
def get_reservas_por_estado(estado):
    
    reservas = listar_reservas_por_estado(estado)
    
    return jsonify(reservas), 200


# Cancelar una reserva por id cambiando su estado a "cancelada"
@reservas_admin_bp.route('/reservas/cancelar/<int:reserva_id>', methods=['PATCH'])
def delete_reserva(reserva_id):
    
    resultado = cancelar_reserva(reserva_id)
    
    if resultado:
        return jsonify({"mensaje": "Reserva cancelada exitosamente"}), 200
    else:
        return jsonify({"mensaje": "No se pudo cancelar la reserva"}), 400