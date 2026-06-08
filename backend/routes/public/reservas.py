from flask import request, jsonify, Blueprint

from services.reservas import (
    buscar_reserva_por_id,
    crear_reserva,
    cancelar_reserva,
    obtener_disponibilidad,
    obtener_mesas_por_estado,
    buscar_mesa_disponible
)

from utils.validators import (
    errores_api,
    validar_reserva
)

reservas_bp = Blueprint("reservas", __name__, url_prefix="/api")


# Cancelar reserva
@reservas_bp.route("/reservas/<int:id>/cancelar-cliente", methods=["PATCH"])
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

# Obtener mesas por estado
@reservas_bp.route("/mesas-disponibles", methods=["GET"])
def get_mesas_por_estado():

    fecha = request.args.get("fecha")
    horario = request.args.get("horario")
    cantidad_personas = request.args.get("cantidad_personas")

    if not fecha or not horario or not cantidad_personas:
        return jsonify({
            "error": "Debe seleccionar fecha, horario y cantidad de personas."
        }), 400

    try:
        cantidad_personas = int(cantidad_personas)
    except ValueError:
        return jsonify({
            "error": "Cantidad de personas debe ser un número entero."
        }), 400

    mesas = obtener_mesas_por_estado(
        fecha=fecha,
        horario=horario,
        cantidad_personas=cantidad_personas
    )

    return jsonify(mesas), 200

# Ver disponibilidad general
@reservas_bp.route("/disponibilidad", methods=["GET"])
def get_disponibilidad():

    disponibilidad = obtener_disponibilidad()

    return jsonify(disponibilidad), 200

# Crear reserva para un cliente, si no tiene cuenta, se crea automaticamente, tomando su email para saber a que id de usuario corresponde
@reservas_bp.route("/reservas", methods=["POST"])
def post_reserva():
    datos = request.get_json()

    # Validar datos de la reserva
    error = validar_reserva(datos)
    if error:
        return error

    # Buscar mesa disponible
    mesa = buscar_mesa_disponible(
        fecha=datos["fecha"],
        horario=datos["horario"],
        cantidad_personas=datos["cantidad_personas"]
    )

    if not mesa:
        return errores_api(
            code=404,
            message="NO_DISPONIBILIDAD",
            description="No hay mesas disponibles para la fecha, horario y cantidad de personas solicitados"
        )

    # Crear reserva
    nueva_reserva = crear_reserva(
        nombre=datos.get("nombre"),
        apellido=datos.get("apellido"),
        email=datos.get("email"),
        telefono=datos.get("telefono"),
        mesa_id=mesa.get("id"),
        fecha=datos.get("fecha"),
        horario=datos.get("horario"),
        cantidad_personas=datos.get("cantidad_personas"),
        notas_adicionales=datos.get("notas_adicionales", "")
    )

    if not nueva_reserva:
        return errores_api(
            code=500,
            message="RESERVA_NO_CREADA",
            description="No se pudo crear la reserva"
        )

    return jsonify(nueva_reserva), 201