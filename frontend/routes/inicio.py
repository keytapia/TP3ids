from flask import Flask, render_template, Blueprint

inicio_bp = Blueprint('inicio', __name__)

# Inicio
@inicio_bp.route("/")
def index():
    return render_template("index.html")