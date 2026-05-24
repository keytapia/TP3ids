from flask import Flask, render_template, Blueprint

menu_bp = Blueprint('menu', __name__)

# Menu
@menu_bp.route("/menu")
def menu():
    return render_template("menu.html")