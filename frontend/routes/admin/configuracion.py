from flask import Blueprint, render_template, request, redirect, url_for

from services.configuracion import (
    obtener_configuracion,
    actualizar_configuracion
)

configuracion_admin_bp = Blueprint("configuracion_admin", __name__)


@configuracion_admin_bp.route("/admin/configuracion", methods=["GET", "POST"])
def configuracion():

    if request.method == "POST":

        data = {
            "nombre":request.form.get("nombre"),
            "email":request.form.get("email"),
            "telefono":request.form.get("telefono"),
            "ubicacion":request.form.get("ubicacion"),
            "horario":request.form.get("horario")
        }

        actualizar_configuracion(data)

        return redirect(url_for("configuracion_admin.configuracion"))

    config = obtener_configuracion()

    return render_template("admin/configuracion.html", config=config)