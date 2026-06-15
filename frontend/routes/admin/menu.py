from flask import Blueprint, render_template, request, redirect, url_for
import requests
from utils.auth import requiere_admin
admin_menu_bp = Blueprint("admin_menu", __name__)

RUTA_A_IMG = "static/images/"
 
@admin_menu_bp.route("/admin/menu/agregar", methods=["GET", "POST"])
@requiere_admin
def menu_agregar():
    if request.method == "POST":
        data = {
            "nombre": request.form.get("nombre"),
            "precio": request.form.get("precio"),
            "categoria_id": request.form.get("categoria_id"),
            "descripcion": request.form.get("descripcion"),
            "restricciones_alimentarias": request.form.get("restricciones_alimentarias")
        }
 
        imagen = request.files.get("imagen")
 
        if imagen and imagen.filename != "":
            ruta = RUTA_A_IMG + imagen.filename
            imagen.save(ruta)
            data["imagen"] = imagen.filename
 
        requests.post("http://127.0.0.1:5000/api/admin/menu", json=data)
 
        return redirect(url_for("admin_menu.menu"))
    
    response_cat = requests.get("http://127.0.0.1:5000/api/categorias")
    categorias = response_cat.json()
    return render_template("admin/menu/agregar_plato.html", categorias=categorias)
 
@admin_menu_bp.route("/admin/menu/editar/<int:id>", methods=["GET", "POST"])
@requiere_admin
def menu_editar(id):
    if request.method == "POST":
        data = {
            "nombre": request.form.get("nombre"),
            "precio": request.form.get("precio"),
            "categoria_id": request.form.get("categoria_id"),
            "descripcion": request.form.get("descripcion"),
            "restricciones_alimentarias": request.form.get("restricciones_alimentarias"),
            "disponible": request.form.get("disponible", True)
        }

        imagen = request.files.get("imagen")
        if imagen and imagen.filename != "":
            ruta = RUTA_A_IMG + imagen.filename
            imagen.save(ruta)
            data["imagen"] = ruta
        else:
            imagen_actual = request.form.get("imagen_actual")
            data["imagen"] = imagen_actual
        
        requests.put(f"http://127.0.0.1:5000/api/admin/menu/{id}", json=data)
        return redirect(url_for("admin_menu.menu"))

    response = requests.get(f"http://127.0.0.1:5000/api/admin/menu/{id}")
    plato = response.json()
    response_cat = requests.get("http://127.0.0.1:5000/api/categorias")
    categorias = response_cat.json()
    return render_template("admin/menu/editar_plato.html", plato=plato, categorias=categorias)


@admin_menu_bp.route("/admin/menu/eliminar/<int:id>", methods=["POST"])
@requiere_admin
def menu_eliminar(id):
    requests.delete(f"http://127.0.0.1:5000/api/admin/menu/{id}")
    return redirect(url_for("admin_menu.menu")) 
 
@admin_menu_bp.route("/admin/menu")
@requiere_admin
def menu():

    categoria = request.args.get("categoria")

    response_cat = requests.get("http://127.0.0.1:5000/api/categorias")
    categorias = response_cat.json()

    url = "http://127.0.0.1:5000/api/admin/menu"
    if categoria:
        url += f"?categoria={categoria}"

    response = requests.get(url)
    platos = response.json()

    return render_template("admin/menu/menu.html", platos=platos, categorias=categorias, categoria_activa=categoria)