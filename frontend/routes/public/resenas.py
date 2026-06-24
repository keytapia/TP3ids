from flask import render_template, Blueprint, request, redirect, url_for, flash, session

from services.resenas import (
    obtener_resenas,
    crear_resena
)

resenas_bp = Blueprint('resenas', __name__)

# Reseñas
@resenas_bp.route("/resenas", methods=["GET"])
def resenas():

    resultado = obtener_resenas()

    listar_resenas = []

    if resultado.get("ok"):
        listar_resenas = resultado.get("data", [])

    else:
        flash("No se pudieron cargar las reseñas", "error")

    return render_template(
        "public/resenas.html",
        resenas=listar_resenas
    )

@resenas_bp.route("/resenas/crear", methods=["GET", "POST"])
@resenas_bp.route("/resenas/crear/<int:reserva_id>", methods=["GET", "POST"])
def crear_resena_form(reserva_id=None):

    if request.method == "POST":

        usuario = session.get("usuario")

        if usuario:

            nombre = usuario.get("nombre")
            apellido = usuario.get("apellido")

        else:
            
            nombre=request.form.get("nombre")
            apellido=request.form.get("apellido")

        reserva_id=reserva_id or request.form.get("reserva_id")
        comentario=request.form.get("comentario")
        puntuacion=request.form.get("puntuacion")

        resultado = crear_resena(
            reserva_id=reserva_id,
            nombre=nombre,
            apellido=apellido,
            comentario=comentario,
            puntuacion=puntuacion
        )

        if resultado.get("ok"):
            flash("Reseña creada con éxito!", "exito")
            return redirect(url_for("resenas.resenas"))
        
        flash("No se pudo crear la reseña", "error")
        return redirect(url_for("resenas.crear_resena_form"))
    
    reserva_id = reserva_id or request.args.get("reserva_id")

    return render_template (
        "public/crear_resena.html",
        reserva_id=reserva_id
    )