from flask import render_template, Blueprint

from services.servicios import (
    obtener_servicios
)

nosotros_bp = Blueprint("nosotros", __name__)


@nosotros_bp.route("/nosotros")
def nosotros():

    resultado = obtener_servicios()

    if resultado["ok"]:
        servicios = resultado["data"]
    else:
        servicios = []

    return render_template("public/nosotros.html", servicios=servicios)