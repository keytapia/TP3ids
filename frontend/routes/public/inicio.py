from flask import Blueprint, render_template

inicio_bp = Blueprint('inicio', __name__)

# Inicio
@inicio_bp.route("/")
def inicio():

    return render_template("public/index.html")