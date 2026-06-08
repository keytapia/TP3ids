from flask import Blueprint, render_template

configuracion_admin_bp = Blueprint("configuracion_admin", __name__)


@configuracion_admin_bp.route("/admin/configuracion")
def configuracion():
    return render_template("admin/configuracion.html")