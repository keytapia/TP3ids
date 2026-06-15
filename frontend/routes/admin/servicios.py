from flask import (Blueprint, render_template, request, redirect, url_for)

from services.servicios import (
    obtener_servicios,
    obtener_servicio_por_id,
    crear_servicio,
    editar_servicio,
    eliminar_servicio
)

servicios_admin_bp = Blueprint(
    "servicios_admin",
    __name__,
    url_prefix="/admin"
)


@servicios_admin_bp.route("/servicios")
def servicios():

    resultado = obtener_servicios()

    if not resultado["ok"]:
        return render_template("admin/servicios.html", error=resultado["error"])

    return render_template("admin/servicios.html", servicios=resultado["data"])


@servicios_admin_bp.route("/servicios/agregar", methods=["GET", "POST"])
def agregar_servicio():

    if request.method == "POST":

        nombre = request.form.get("nombre")
        disponible = request.form.get("disponible")

        resultado = crear_servicio(nombre, disponible)

        if resultado["ok"]:
            return redirect(url_for("servicios_admin.servicios"))

        return render_template("admin/agregar_servicio.html", error=resultado["error"])

    return render_template("admin/agregar_servicio.html")


@servicios_admin_bp.route("/servicios/editar/<int:id>", methods=["GET", "POST"])
def put_servicio(id):

    if request.method == "POST":

        nombre = request.form.get("nombre")
        disponible = request.form.get("disponible")

        resultado = editar_servicio(id, nombre, disponible)

        if resultado["ok"]:
            return redirect(url_for("servicios_admin.servicios"))

        resultado_servicio = obtener_servicio_por_id(id)

        return render_template(
            "admin/editar_servicio.html",
            servicio=resultado_servicio["data"],
            error=resultado["error"]
        )

    resultado = obtener_servicio_por_id(id)

    if not resultado["ok"]:
        return redirect(url_for("servicios_admin.servicios"))

    return render_template(
        "admin/editar_servicio.html",
        servicio=resultado["data"]
    )


@servicios_admin_bp.route("/servicios/eliminar/<int:id>", methods=["POST"])
def delete_servicio(id):

    eliminar_servicio(id)

    return redirect(url_for("servicios_admin.servicios"))