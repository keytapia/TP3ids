from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from datetime import date, datetime

from services.reservas import (
    crear_reserva as crear_reserva_service,
    obtener_mesas_por_estado as obtener_mesas_con_estado,
    cancelar_reserva as cancelar_reserva_service,
    obtener_reservas_por_usuario
)

reservas_bp = Blueprint("reservas", __name__)


@reservas_bp.route("/reservas", methods=["GET", "POST"])
def reservas():

    if request.method == "POST":

        usuario = session.get("usuario")

        if usuario:

            nombre = usuario.get("nombre")
            apellido = usuario.get("apellido")
            email = usuario.get("email")
            telefono = usuario.get("telefono")

        else:

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
            flash("Completá todos los campos obligatorios.", "error")
            return redirect(url_for("reservas.reservas"))

        if not mesa_id:
            flash("Tenés que seleccionar una mesa disponible.", "error")
            return redirect(url_for("reservas.reservas", fecha=fecha, horario=horario, cantidad_personas=cantidad_personas))

        try:
            cantidad_personas = int(cantidad_personas)
            mesa_id = int(mesa_id)
        except ValueError:
            flash("Los datos de la reserva no son válidos.", "error")
            return redirect(url_for("reservas.reservas"))

        resultado_mesas = obtener_mesas_con_estado(
            fecha=fecha,
            horario=horario,
            cantidad_personas=cantidad_personas
        )

        if not resultado_mesas.get("ok"):
            flash("Error al verificar la disponibilidad de mesas.", "error")
            return redirect(url_for("reservas.reservas"))
        
        mesas = resultado_mesas.get("data", [])
        mesa_elegida = None

        for mesa in mesas:
            if mesa["id"] == mesa_id:
                mesa_elegida = mesa
                break

        if not mesa_elegida:
            flash("La mesa seleccionada no existe.", "error")
            return redirect(url_for("reservas.reservas", fecha=fecha, horario=horario, cantidad_personas=cantidad_personas))

        if not mesa_elegida["seleccionable"]:
            flash("La mesa seleccionada no está disponible para esa fecha, horario o cantidad de personas.", "error")
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
            flash("¡Reserva creada con éxito, revisá tu email!", "exito")
            return redirect(url_for("reservas.reservas"))

        flash("¡Error al crear la reserva!", "error")
        return redirect(url_for("reservas.reservas"))

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
            flash("Error al verificar la disponibilidad de mesas.", "error")
    
    
    return render_template(
        "public/reservas.html",
        mesas=mesas,
        fecha=fecha,
        horario=horario,
        cantidad_personas=cantidad_personas,
        fecha_actual=date.today().isoformat(),
        hora_actual=datetime.now().strftime("%H:%M")
    )


@reservas_bp.route("/reservas/<int:id>/cancelar", methods=["GET", "POST"])
def cancelar_reserva_cliente(id):
    if request.method == "POST":
        decision = request.form.get("decision")
        if decision == "si":
            cancelar_reserva_service(id)

        flash("Reserva cancelada con éxito!", "exito")
        return redirect(url_for("inicio.inicio"))
    return render_template(
        "public/cancelar_reserva.html",
        id=id
    )


@reservas_bp.route("/reservas/mis-reservas")
def mis_reservas():

    usuario = session.get("usuario")

    estado_activo = request.args.get("estado", "todas")

    if not usuario:
        return redirect(url_for("login.login_cliente"))

    reservas = obtener_reservas_por_usuario(
        usuario["id"]
    )

    if estado_activo != "todas":
        reservas = [
            reserva
            for reserva in reservas
            if reserva["estado"] == estado_activo
        ]

    return render_template(
        "public/mis_reservas.html",
        reservas=reservas,
        estado_activo=estado_activo
    )