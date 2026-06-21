from flask import Blueprint, render_template

from utils.auth import requiere_admin

from services.estadisticas import obtener_estadisticas

estadisticas_admin_bp = Blueprint("estadisticas_admin", __name__, url_prefix="/admin")


@estadisticas_admin_bp.route("/estadisticas")
@requiere_admin
def estadisticas():

    resultado = obtener_estadisticas()

    if not resultado["ok"]:
        return render_template(
            "admin/estadisticas.html",
            error=resultado["error"]
        )

    return render_template(
        "admin/estadisticas.html",
        estadisticas=resultado["data"]
    )