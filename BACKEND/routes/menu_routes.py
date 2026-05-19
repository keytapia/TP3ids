from flask import Flask, request, jsonify, Blueprint
from datetime import datetime

from BACKEND.services import reservas_service

menu_bp = Blueprint('menu', __name__)

# Visualizar las reservas
@app.route('/api/admin/reservas', methods=['GET'])
def get_reservas():
    reservas = reservas_service.listar_reservas()
    return jsonify(reservas)

#Visualizar el estado de las reservas (filtra por estado)
@app.route('/api/admin/reservas/estado/<estado>', methods=['GET'])
def get_reservas_por_estado(estado):
    reservas = reservas_service.listar_reservas_por_estado(estado)
    return jsonify(reservas)

# Cancelar una reserva por id cambiando su estado a "cancelada"
@app.route('/api/admin/reservas/cancelar/<int:reserva_id>', methods['PATCH'])
def cancelar_reserva(reserva_id):
    resultado = reservas_service.cancelar_reserva(reserva_id)
    if resultado:
        return jsonify({"message": "Reserva cancelada exitosamente"})
    else:
        return jsonify({"message": "No se pudo cancelar la reserva"}), 400
