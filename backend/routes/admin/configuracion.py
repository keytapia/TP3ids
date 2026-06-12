from flask import Blueprint, jsonify, request

from services.configuracion import (
    obtener_datos_configuracion,
    guardar_configuracion
)

configuracion_admin_bp = Blueprint("configuracion_admin", __name__, url_prefix="/api/admin")


@configuracion_admin_bp.route("/configuracion", methods=["GET"])
def obtener_configuracion():

    config = obtener_datos_configuracion()

    return jsonify(config)


@configuracion_admin_bp.route("/configuracion", methods=["PUT"])
def actualizar_configuracion():

    data = request.get_json()

    resultado = guardar_configuracion(data)

    return jsonify(resultado)