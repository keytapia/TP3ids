from flask import Blueprint, render_template

from services.resenas import (
    obtener_promedio_resenas
)

inicio_bp = Blueprint('inicio', __name__)

# Inicio
@inicio_bp.route("/")
def inicio():

    resultado = obtener_promedio_resenas()

    cantidad_resenas = 0
    promedio = 0

    if resultado["ok"]:
        cantidad_resenas = resultado["data"]["cantidad_resenas"]
        promedio = round(float(resultado["data"]["promedio_estrellas"]))

    return render_template("public/index.html", cantidad_resenas=cantidad_resenas, promedio=promedio)