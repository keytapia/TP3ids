from flask import Blueprint, render_template, redirect
from utils.auth import requiere_admin
estadisticas_bp = Blueprint("estadisticas", __name__)


@estadisticas_bp.route("/admin/estadisticas")
@requiere_admin
def estadisticas():
    return render_template("admin/estadisticas.html")