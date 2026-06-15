from flask import Blueprint, render_template, redirect
from utils.auth import requiere_admin
admin_resenas_bp = Blueprint("admin_resenas", __name__)


@admin_resenas_bp.route("/admin/resenas")
@requiere_admin
def resenas():
    return render_template("admin/resenas.html")