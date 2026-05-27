from flask import Blueprint, render_template

admin_menu_bp = Blueprint("admin_menu", __name__)


@admin_menu_bp.route("/admin/menu")
def menu():
    return render_template("admin/menu.html")