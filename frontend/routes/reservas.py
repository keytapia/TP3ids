from flask import Blueprint, render_template, request, redirect, url_for

from services.reservas import (
    crear_reserva
)

reservas_bp = Blueprint("reservas", __name__)


@reservas_bp.route("/reservas", methods=["GET", "POST"])
def reservas():

    if request.method == "POST":

        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        fecha = request.form["fecha"]
        horario = request.form["horario"]
        cantidad_personas = int(request.form["cantidad_personas"])
        notas_adicionales = request.form["notas_adicionales"]

        resultado = crear_reserva(
            nombre,
            apellido,
            email,
            telefono,
            cantidad_personas,
            fecha,
            horario,
            notas_adicionales
        )

        # Si se pudo crear la reserva
        if resultado.get("id"):

            return redirect(
                url_for(
                    "reservas.reservas",
                    mensaje="¡Reserva creada con éxito!"
                )
            )

        # Si no se pudo crear la reserva
        return redirect(
            url_for(
                "reservas.reservas",
                mensaje="¡Error al crear la reserva!"
            )
        )

    mensaje = request.args.get("mensaje")

    return render_template(
        "reservas.html",
        mensaje=mensaje
    )