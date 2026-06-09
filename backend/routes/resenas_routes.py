from flask import Blueprint, request, jsonify

from services.resenas_service import (
    obtener_resenas,
    obtener_resena_por_id,
    crear_resena
)

resenas_bp = Blueprint("resenas_bp", __name__)


# Mostrar todas las reseñas
@resenas_bp.route("/api/resenas", methods=["GET"])
def get_resenas():

    resenas = obtener_resenas()

    return jsonify(resenas), 200


# Mostrar una reseña por id
@resenas_bp.route("/api/resenas/<int:id_resena>", methods=["GET"])
def get_resena_por_id(id_resena):

    resena = obtener_resena_por_id(id_resena)

    if not resena:
        return jsonify({
            "error": "Reseña no encontrada"
        }), 404

    return jsonify(resena), 200


# Crear reseña
@resenas_bp.route("/api/resenas", methods=["POST"])
def post_resena():

    data = request.get_json()

    nombre_usuario = data.get("nombre_usuario")
    reserva_id = data.get("reserva_id")
    comentario = data.get("comentario")
    puntuacion = data.get("puntuacion")

    resultado = crear_resena(
        nombre_usuario,
        reserva_id,
        comentario,
        puntuacion
    )

    if resultado["ok"]:
        return jsonify(resultado), 201

    return jsonify(resultado), 400


