from flask import request, jsonify, Blueprint

from services.reservas_service import (
    buscar_reserva_por_id,
    crear_reserva,
    cancelar_reserva,
    obtener_disponibilidad,
    buscar_mesa_disponible
)

from services.usuarios_service import (
    buscar_usuario_por_email,
    crear_usuario_cliente
)

reservas_bp = Blueprint("reservas", __name__)


# Crear reserva
@reservas_bp.route("/api/reservas", methods=["POST"])
def post_reserva():

    reserva = request.get_json()

    nombre = reserva.get("nombre")
    apellido = reserva.get("apellido")
    email = reserva.get("email")
    telefono = reserva.get("telefono")
    fecha = reserva.get("fecha")
    horario = reserva.get("horario")
    cantidad_personas = reserva.get("cantidad_personas")

    # Si faltan campos obligatorios, devolver error
    if not all([
        nombre,
        apellido,
        email,
        telefono,
        fecha,
        horario,
        cantidad_personas
    ]):
        return jsonify({
            "mensaje": "Datos incompletos"
        }), 400

    # Primero buscamos si el usuario ya existe por email
    usuario = buscar_usuario_por_email(email)

    # Si no existe, lo creamos como cliente
    if not usuario:
        usuario = crear_usuario_cliente(
            nombre,
            apellido,
            email,
            telefono
        )

    # Buscar mesa disponible
    mesa = buscar_mesa_disponible(
        fecha,
        horario,
        cantidad_personas
    )

    if not mesa:
        return jsonify({
            "mensaje": "No hay disponibilidad",
            "descripcion": "No existe una mesa disponible para esa fecha, horario y cantidad de personas"
        }), 404

    nueva_reserva = crear_reserva(
        usuario["id"],
        mesa["id"],
        fecha,
        horario,
        cantidad_personas,
        reserva.get("notas_adicionales", "")
    )

    return jsonify(nueva_reserva), 201


# Cancelar reserva
@reservas_bp.route(
    "/api/reservas/<int:id>/cancelar-cliente",
    methods=["PATCH"]
)
def patch_cancelar_reserva(id):

    reserva = buscar_reserva_por_id(id)

    if not reserva:
        return jsonify({
            "mensaje": "Reserva no encontrada"
        }), 404

    if reserva["estado"] == "cancelada":
        return jsonify({
            "mensaje": "Reserva ya cancelada"
        }), 400

    resultado = cancelar_reserva(id)

    if not resultado:
        return jsonify({
            "mensaje": "No se pudo cancelar la reserva"
        }), 400

    return jsonify({
        "mensaje": "Reserva cancelada exitosamente"
    }), 200


# Ver disponibilidad
@reservas_bp.route("/api/disponibilidad", methods=["GET"])
def get_disponibilidad():

    disponibilidad = obtener_disponibilidad()

    return jsonify(disponibilidad), 200