from flask import Blueprint, jsonify

from services.estadisticas import (
    obtener_estadisticas
)

estadisticas_admin_bp = Blueprint('estadisticas_admin', __name__, url_prefix="/api/admin")


@estadisticas_admin_bp.route("/estadisticas", methods=["GET"])
def estadisticas():

    return jsonify(obtener_estadisticas())