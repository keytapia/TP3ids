from flask import request, jsonify, Blueprint

from services.resenas import (
    listar_resenas,
    buscar_resena_por_id,
    obtener_cantidad_total_y_promedio_de_resenas,
    crear_resena_libre,
    crear_resena_con_reserva
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


@resenas_bp.route("/resenas/crear", methods=["POST"])
def post_resena_libre():

    datos = request.get_json()

    resultado = crear_resena_libre(
        nombre=datos.get("nombre"),
        apellido=datos.get("apellido"),
        comentario=datos.get("comentario"),
        puntuacion=datos.get("puntuacion")
    )

    if resultado["ok"]:
        return jsonify(resultado), 201

    return jsonify(resultado), 400


@resenas_bp.route("/resenas/crear/<int:reserva_id>", methods=["POST"])
def post_resena_con_reserva(reserva_id):

    datos = request.get_json()

    resultado = crear_resena_con_reserva(
        reserva_id=reserva_id,
        nombre=datos.get("nombre"),
        apellido=datos.get("apellido"),
        comentario=datos.get("comentario"),
        puntuacion=datos.get("puntuacion")
    )

    if resultado["ok"]:
        return jsonify(resultado), 201

    return jsonify(resultado), 400


@resenas_bp.route("/resenas/promedio", methods=["GET"])
def get_promedio_resenas():

    resultado = obtener_cantidad_total_y_promedio_de_resenas()

    return jsonify(resultado), 200