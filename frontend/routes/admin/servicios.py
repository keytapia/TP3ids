from flask import Blueprint, render_template

servicios_admin_bp = Blueprint("servicios_admin", __name__, url_prefix="/admin")


@servicios_admin_bp.route("/servicios")
def servicios():
    return render_template("admin/servicios.html")