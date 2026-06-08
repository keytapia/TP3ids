from flask import Blueprint, render_template

reservas_admin_bp = Blueprint("reservas_admin", __name__, url_prefix="/admin")


@reservas_admin_bp.route("/reservas")
def reservas():
    return render_template("admin/reservas.html")