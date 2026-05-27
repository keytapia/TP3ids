from flask import Blueprint, render_template

admin_reservas_bp = Blueprint("admin_reservas", __name__)


@admin_reservas_bp.route("/admin/reservas")
def reservas():
    return render_template("admin/reservas.html")