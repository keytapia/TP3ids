from flask import Blueprint, render_template

servicios_admin_bp = Blueprint("servicios_admin", __name__, url_prefix="/admin")


@servicios_admin_bp.route("/servicios")
def servicios():

    servicios_prueba = [
        {"servicio": 'WIFI', "id":1},
        {"servicio": 'Pet Friendly', "id":2},
        {"servicio": 'Estacionamiento', "id":3},

    ]

    return render_template("admin/servicios.html", servicios=servicios_prueba)




@servicios_admin_bp.route("/servicios/agregar", methods=["GET", "POST"])
def agregar_servicio():
    return render_template("admin/agregar_servicio.html")



@servicios_admin_bp.route("/servicios/editar", methods=["GET", "POST"])
def editar_servicio():
    return render_template("admin/editar_servicio.html")