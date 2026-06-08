from flask import Blueprint, jsonify

from services.dashboard import (
    obtener_resumen_dashboard,
    obtener_proximas_reservas,
    obtener_cancelaciones_hoy,
    obtener_ultimas_reseñas
)

dashboard_admin_bp = Blueprint('dashboard_admin', __name__, url_prefix="/api/admin")


@dashboard_admin_bp.route("/dashboard", methods=["GET"])
def dashboard():

    return jsonify({
        "resumen": obtener_resumen_dashboard(),
        "proximas_reservas": obtener_proximas_reservas(),
        "cancelaciones_hoy": obtener_cancelaciones_hoy(),
        "ultimas_reseñas": obtener_ultimas_reseñas()
    })