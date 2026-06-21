from flask import Blueprint, render_template

from utils.auth import requiere_admin

from services.dashboard import obtener_dashboard

dashboard_admin_bp = Blueprint("dashboard_admin", __name__, url_prefix="/admin")


@dashboard_admin_bp.route("/dashboard")
@requiere_admin
def dashboard():

    resultado = obtener_dashboard()

    if not resultado["ok"]:
        return render_template(
            "admin/dashboard.html",
            error=resultado["error"]
        )

    return render_template(
        "admin/dashboard.html",
        dashboard=resultado["data"]
    )