from flask import Blueprint, render_template, redirect
from utils.auth import requiere_admin
configuracion_bp = Blueprint("configuracion", __name__)


@configuracion_bp.route("/admin/configuracion")
@requiere_admin
def configuracion():
    return render_template("admin/configuracion.html")