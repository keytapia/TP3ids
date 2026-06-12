from flask import jsonify, Blueprint

resenas_admin_bp = Blueprint('resenas_admin', __name__, url_prefix='/api/admin')


# Obtener todas las reseñas
@resenas_admin_bp.route("/resenas", methods=["GET"])
def get_resenas():
    # Acá va la función del servicio para obtener todas las reseñas
    # resultado = obtener_reseñas()

    # if resultado:
    #     return jsonify(resultado), 200
    # else:
    #     return jsonify({"mensaje": "No se pudieron obtener las reseñas"}), 400
    return jsonify({"mensaje": "Falta hacer función de obtener reseñas"}), 200


# Eliminar una reseña por id
@resenas_admin_bp.route("/resenas/<int:id>", methods=["DELETE"])
def delete_resena(id):

    # Acá va la función del servicio para eliminar la reseña
    # (O capaz poner una columna a la tabla 'resenas' donde diga estado='publica' u 'oculta', y hacer un patch en vez de eliminar para actualizar el estado)
    # resultado = eliminar_reseña(id)

    # if resultado:
    #     return jsonify({"mensaje": "Reseña eliminada exitosamente"}), 200
    # else:
    #     return jsonify({"mensaje": "No se pudo eliminar la reseña"}), 400
    return jsonify({"mensaje": "Falta hacer función de eliminar reseña"}), 200