from flask import Blueprint, render_template, redirect, url_for, request

from services.resenas import (
    obtener_resenas_admin,
    ocultar_mostrar_resena,
    eliminar_resena
)

resenas_admin_bp = Blueprint("resenas_admin", __name__, url_prefix="/admin")


@resenas_admin_bp.route("/resenas")
def resenas():

    filtro = request.args.get("filtro", "todas")

    resultado = obtener_resenas_admin()

    if not resultado["ok"]:

        return render_template(
            "admin/resenas.html",
            resenas=[],
            filtro=filtro
        )

    resenas = resultado["data"]

    if filtro == "publica":
        resenas = [r for r in resenas if r["disponible"]]

    elif filtro == "oculta":
        resenas = [r for r in resenas if not r["disponible"]]

    return render_template(
        "admin/resenas.html",
        resenas=resenas,
        filtro=filtro
    )


@resenas_admin_bp.route("/resenas/estado/<int:id>", methods=["POST"])
def cambiar_estado_resena(id):

    ocultar_mostrar_resena(id)

    return redirect(url_for("resenas_admin.resenas"))


@resenas_admin_bp.route("/resenas/eliminar/<int:id>", methods=["POST"])
def borrar_resena(id):

    eliminar_resena(id)

    return redirect(url_for("resenas_admin.resenas"))