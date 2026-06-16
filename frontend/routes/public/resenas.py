from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash

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
        flash("No se pudieron cargar las reseñas")

    return render_template(
        "public/resenas.html",
        resenas=listar_resenas
    )

@resenas_bp.route("/resenas/crear", methods=["GET", "POST"])
def crear_resena_form():

    if request.method == "POST":

        reserva_id=request.form.get("reserva_id")
        nombre=request.form.get("nombre")
        apellido=request.form.get("apellido")
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
            flash("Reseña creada exitosamente")
            return redirect(url_for("resenas.resenas"))
        
        flash("No se pudo crear la reseña")
        return redirect(url_for("resenas.crear_resena_form"))
    
    reserva_id = request.args.get("reserva_id")

    return render_template (
        "public/crear_resena.html",
        reserva_id=reserva_id
    )