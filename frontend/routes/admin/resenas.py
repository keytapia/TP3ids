from flask import Blueprint, render_template

admin_resenas_bp = Blueprint("admin_resenas", __name__)


@admin_resenas_bp.route("/admin/resenas")
def resenas():
    return render_template("admin/resenas.html")