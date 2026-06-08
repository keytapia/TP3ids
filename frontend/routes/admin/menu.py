from flask import Blueprint, render_template

menu_admin_bp = Blueprint("menu_admin", __name__, url_prefix="/admin")


@menu_admin_bp.route("/menu")
def menu():
    return render_template("admin/menu.html")