from flask import Flask, request, jsonify, Blueprint
from datetime import datetime, date, timedelta

from services.reservas_service import (
    buscar_reserva_por_id,
    cancelar_reserva_cliente,
    obtener_disponibilidad,
    construir_error_api
)

reservas_bp = Blueprint('reservas', __name__)


#Cancelar reserva

@reservas_bp.route("/api/reservas/<int:id>/cancelar-cliente", methods=["PATCH"])
def cancelar_reserva_cliente(id):
    reserva = buscar_reserva_por_id(id)

    if not reserva:
        return jsonify(construir_error_api(
            code=404,
            message="Reserva no encontrada",
            description=f"No existe una reserva con id '{id}'"
        )), 404

    if reserva["estado"] == "cancelada":
        return jsonify(construir_error_api(
            code=400,
            message="Reserva ya cancelada",
            description=f"La reserva con id '{id}' ya se encuentra cancelada"
        )), 400

    reserva_cancelada = cancelar_reserva_cliente(id)

    if not reserva_cancelada:
        return jsonify(construir_error_api(
            code=400,
            message="No se pudo cancelar la reserva",
            description=f"No fue posible cancelar la reserva con id '{id}'"
        )), 400

    return jsonify({
        "message": "Reserva cancelada exitosamente",
        "reserva": reserva_cancelada
    }), 200

#ver disponibilidad para reservar

@reservas_bp.route("/api/disponibilidad", methods=["GET"])
def get_disponibilidad():
    disponibilidad = obtener_disponibilidad()

    if not disponibilidad:
        return jsonify(construir_error_api(
            code=404,
            message="Disponibilidad no encontrada",
            description="No hay fechas, horarios o mesas disponibles para reservar"
        )), 404

    return jsonify(disponibilidad), 200
