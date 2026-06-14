from flask import Blueprint, render_template

servicios_admin_bp = Blueprint("servicios_admin", __name__, url_prefix="/admin")


@servicios_admin_bp.route("/servicios")
def servicios():

    resultado = obtener_servicios()

    if not resultado["ok"]:
        return render_template("admin/servicios.html", error=resultado["error"])

    return render_template("admin/servicios.html", servicios=resultado["data"])


@servicios_admin_bp.route("/servicios/agregar", methods=["GET", "POST"])
def agregar_servicio():

    resultado = crear_servicio()

    if not resultado["ok"]:
        return render_template("admin/servicios.html", error=resultado["error"])

    return render_template("admin/agregar_servicio.html", servicios=resultado["data"])


@servicios_admin_bp.route("/servicios/editar/<int:id>", methods=["GET", "POST"])
def editar_servicio(id):
    return render_template("admin/editar_servicio.html", id=id)


@servicios_admin_bp.route("/servicios/eliminar/<int:id>", methods=["POST"])
def eliminar_servicio(id):


    eliminar_servicio(id)

    return redirect(url_for("servicios_admin.servicios"))



