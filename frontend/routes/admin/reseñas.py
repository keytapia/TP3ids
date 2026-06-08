from flask import Blueprint, render_template

reseñas_admin_bp = Blueprint("reseñas_admin", __name__, url_prefix="/admin")


@reseñas_admin_bp.route("/reseñas")
def reseñas():
    return render_template("admin/reseñas.html")