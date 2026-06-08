from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from services.menu import (
    obtener_menu,
    obtener_plato,
    crear_plato,
    editar_plato,
    eliminar_plato,
    obtener_categorias
)

menu_admin_bp = Blueprint("menu_admin", __name__, url_prefix="/admin")

RUTA_A_IMG = "static/images/"


@menu_admin_bp.route("/menu")
def menu():

    categoria = request.args.get("categoria")

    resultado_menu = obtener_menu(categoria)
    resultado_categorias = obtener_categorias()

    platos = resultado_menu.get("data", [])
    categorias = resultado_categorias.get("data", [])

    return render_template(
        "admin/menu.html",
        platos=platos,
        categorias=categorias,
        categoria_activa=categoria
    )


@menu_admin_bp.route("/menu/agregar", methods=["GET", "POST"])
def menu_agregar():

    if request.method == "POST":

        data = {
            "categoria_id": int(request.form.get("categoria_id")),
            "nombre": request.form.get("nombre"),
            "precio": float(request.form.get("precio")),
            "descripcion": request.form.get("descripcion"),
            "restricciones_alimentarias": request.form.get(
                "restricciones_alimentarias"
            ),
            "disponible": True
        }

        imagen = request.files.get("imagen")

        if imagen and imagen.filename:

            ruta = RUTA_A_IMG + imagen.filename
            imagen.save(ruta)

            data["imagen"] = imagen.filename

        resultado = crear_plato(data)

        if resultado["ok"]:
            return redirect(
                url_for("menu_admin.menu")
            )

        return resultado["error"]

    resultado_categorias = obtener_categorias()

    return render_template(
        "admin/agregar_plato.html",
        categorias=resultado_categorias["data"]
    )


@menu_admin_bp.route("/menu/editar/<int:id>", methods=["GET", "POST"])
def menu_editar(id):

    if request.method == "POST":

        data = {
            "categoria_id": int(request.form.get("categoria_id")),
            "nombre": request.form.get("nombre"),
            "precio": float(request.form.get("precio")),
            "descripcion": request.form.get("descripcion"),
            "restricciones_alimentarias": request.form.get(
                "restricciones_alimentarias"
            ),
            "disponible": (
                request.form.get("disponible") == "on"
            )
        }

        imagen = request.files.get("imagen")

        if imagen and imagen.filename:

            ruta = RUTA_A_IMG + imagen.filename
            imagen.save(ruta)

            data["imagen"] = imagen.filename

        else:

            data["imagen"] = request.form.get(
                "imagen_actual"
            )

        resultado = editar_plato(id, data)

        if resultado["ok"]:
            return redirect(
                url_for("admin_menu.menu")
            )

        return resultado["error"]

    resultado_plato = obtener_plato(id)
    resultado_categorias = obtener_categorias()

    return render_template(
        "admin/editar_plato.html",
        plato=resultado_plato["data"],
        categorias=resultado_categorias["data"]
    )


@menu_admin_bp.route("/menu/eliminar/<int:id>", methods=["POST"])
def menu_eliminar(id):

    eliminar_plato(id)

    return redirect(
        url_for("menu_admin.menu")
    )