from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from services.resenas import (
    obtener_resenas,
    crear_resena
)

resenas_bp = Blueprint("resenas", __name__)

# Reseñas
@resenas_bp.route("/resenas", methods=["GET", "POST"])
def resenas():

    if request.method == "POST":

        nombre_usuario = request.form.get("nombre_usuario")
        reserva_id = request.form.get("reserva_id")
        comentario = request.form.get("comentario")
        puntuacion = request.form.get("puntuacion")

        resultado = crear_resena(
            nombre_usuario,
            reserva_id,
            comentario,
            puntuacion
        )

        if resultado.get("ok"):

            flash("Reseña creada correctamente")

            return redirect(
                url_for("resenas.resenas")
            )

        flash("Error al crear la reseña")

        return redirect(
            url_for("resenas.resenas")
        )

    resultado = obtener_resenas()

    lista_resenas = []

    if resultado.get("ok"):
        lista_resenas = resultado.get("data")

    return render_template(
        "resenas.html",
        resenas=lista_resenas
    )


@resenas_bp.route("/crear-resena")
def form_resena():
    return render_template("crear_resena.html")