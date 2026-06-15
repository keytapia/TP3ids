from flask import Blueprint, render_template, redirect
from utils.auth import requiere_admin
admin_reservas_bp = Blueprint("admin_reservas", __name__)


@admin_reservas_bp.route("/admin/reservas")
@requiere_admin
def reservas():
    return render_template("admin/reservas.html")