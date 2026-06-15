from flask import jsonify, Blueprint

from services.resenas import (
    listar_resenas,
    buscar_resena_por_id,
    modificar_resena,
    eliminar_resena
)

resenas_admin_bp = Blueprint('resenas_admin', __name__, url_prefix='/api/admin')


# Obtener todas las reseñas
@resenas_admin_bp.route("/resenas", methods=["GET"])
def get_resenas():

    resultado = listar_resenas()

    if resultado:
        return jsonify(resultado), 200
    else:
        return jsonify({"mensaje": "No se pudieron obtener las reseñas"}), 400


# Obtener reseña por id
@resenas_admin_bp.route("/resenas/<int:id>", methods=["GET"])
def get_resena_por_id(id):

    resultado = buscar_resena_por_id(id)

    if resultado:
        return jsonify(resultado), 200
    else:
        return jsonify({"mensaje": f"No se pudo obtener la reseña con id {id}"}), 404


# Modificar el estado de la reseña por id
@resenas_admin_bp.route("/resenas/<int:id>", methods=["PATCH"])
def put_resena(id):

    resultado = modificar_resena(id)

    if resultado:
        return jsonify({"mensaje": "Reseña modificada exitosamente"}), 200

    return jsonify({"mensaje": f"No se pudo obtener la reseña con id {id}"}), 404


# Eliminar una reseña por id
@resenas_admin_bp.route("/resenas/<int:id>", methods=["DELETE"])
def delete_resena(id):

    resultado = eliminar_resena(id)

    if resultado:
        return jsonify({"mensaje": "Reseña eliminada exitosamente"}), 200
    else:
        return jsonify({"mensaje": "No se pudo eliminar la reseña"}), 400