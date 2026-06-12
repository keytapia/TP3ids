from flask import Blueprint, render_template

resenas_admin_bp = Blueprint("resenas_admin", __name__, url_prefix="/admin")


@resenas_admin_bp.route("/resenas")
def resenas():
    return render_template("admin/resenas.html")