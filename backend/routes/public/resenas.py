from flask import request, jsonify, Blueprint

from services.resenas import (
    listar_resenas,
    buscar_resena_por_id,
    crear_resena
)

resenas_bp = Blueprint('resenas', __name__, url_prefix='/api')

@resenas_bp.route("/resenas", methods=["GET"])
def get_resenas():

    resenas = listar_resenas()

    return jsonify(resenas), 200


@resenas_bp.route("/resenas/<int:id>", methods=["GET"])
def get_resena_por_id(id):

    resena = buscar_resena_por_id(id)

    if not resena:
        return jsonify({
            "mensaje": "Reseña no encontrada"
        }), 404

    return jsonify(resena), 200


@resenas_bp.route("/resenas", methods=["POST"])
def post_resenas():

    datos = request.get_json()

    resultado = crear_resena(
        reserva_id=datos.get("reserva_id"),
        nombre=datos.get("nombre"),
        apellido=datos.get("apellido"),
        comentario=datos.get("comentario"),
        puntuacion=datos.get("puntuacion")
    )

    if resultado["ok"]:
        return jsonify({resultado}), 201

    return jsonify(resultado), 400