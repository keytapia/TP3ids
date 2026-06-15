from flask import Blueprint, render_template, redirect
from utils.auth import requiere_admin
servicios_bp = Blueprint("servicios", __name__)


@servicios_bp.route("/admin/servicios")
@requiere_admin
def servicios():
    return render_template("admin/servicios.html")