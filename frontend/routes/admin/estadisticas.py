from flask import Blueprint, render_template

estadisticas_bp = Blueprint("estadisticas", __name__)


@estadisticas_bp.route("/admin/estadisticas")
def estadisticas():
    return render_template("admin/estadisticas.html")