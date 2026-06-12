from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from datetime import date, datetime
from services.reservas import (
    crear_reserva as crear_reserva_service,
    obtener_mesas_por_estado as obtener_mesas_con_estado
)

reservas_bp = Blueprint("reservas", __name__)


@reservas_bp.route("/reservas", methods=["GET", "POST"])
def reservas():

    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        email = request.form.get("email")
        telefono = request.form.get("telefono")
        fecha = request.form.get("fecha")
        horario = request.form.get("horario")
        cantidad_personas = request.form.get("cantidad_personas")
        notas_adicionales = request.form.get("notas_adicionales")
        mesa_id = request.form.get("mesa_id")

        if not nombre or not apellido or not email or not telefono or not fecha or not horario or not cantidad_personas:
            flash("Completá todos los campos obligatorios.")
            return redirect(url_for("reservas.reservas"))

        if not mesa_id:
            flash("Tenés que seleccionar una mesa disponible.")
            return redirect(url_for("reservas.reservas", fecha=fecha, horario=horario, cantidad_personas=cantidad_personas))

        try:
            cantidad_personas = int(cantidad_personas)
            mesa_id = int(mesa_id)
        except ValueError:
            flash("Los datos de la reserva no son válidos.")
            return redirect(url_for("reservas.reservas"))

        resultado_mesas = obtener_mesas_con_estado(
            fecha=fecha,
            horario=horario,
            cantidad_personas=cantidad_personas
        )

        if not resultado_mesas.get("ok"):
            flash("Error al verificar la disponibilidad de mesas.")
            return redirect(url_for("reservas.reservas"))
        
        mesas = resultado_mesas.get("data", [])
        mesa_elegida = None

        for mesa in mesas:
            if mesa["id"] == mesa_id:
                mesa_elegida = mesa
                break

        if not mesa_elegida:
            flash("La mesa seleccionada no existe.")
            return redirect(url_for("reservas.reservas", fecha=fecha, horario=horario, cantidad_personas=cantidad_personas))

        if not mesa_elegida["seleccionable"]:
            flash("La mesa seleccionada no está disponible para esa fecha, horario o cantidad de personas.")
            return redirect(url_for("reservas.reservas", fecha=fecha, horario=horario, cantidad_personas=cantidad_personas))

        resultado = crear_reserva_service(
            nombre,
            apellido,
            email,
            telefono,
            cantidad_personas,
            fecha,
            horario,
            notas_adicionales,
            mesa_id
        )

        if resultado.get("ok"):
            return redirect(
                url_for(
                    "reservas.reservas",
                    mensaje="¡Reserva creada con éxito, revisa tu email!"
                )
            )

        return redirect(
            url_for(
                "reservas.reservas",
                mensaje="¡Error al crear la reserva!"
            )
        )

    mensaje = request.args.get("mensaje")

    fecha = request.args.get("fecha")
    horario = request.args.get("horario")
    cantidad_personas = request.args.get("cantidad_personas")

    mesas=[]
    if fecha and horario and cantidad_personas:
        resultado = obtener_mesas_con_estado(
            fecha=fecha,
            horario=horario,
            cantidad_personas=cantidad_personas
        )
        if resultado.get("ok"):
            mesas = resultado.get("data", [])
        else:
            flash("Error al verificar la disponibilidad de mesas.")
    
    return render_template(
        "public/reservas.html",
        mensaje=mensaje,
        mesas=mesas,
        fecha=fecha,
        horario=horario,
        cantidad_personas=cantidad_personas,
        fecha_actual=date.today().isoformat(),
        hora_actual=datetime.now().strftime("%H:%M")
    )