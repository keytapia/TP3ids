from flask import Blueprint, render_template

configuracion_bp = Blueprint("configuracion", __name__)


@configuracion_bp.route("/admin/configuracion")
def configuracion():
    return render_template("admin/configuracion.html")