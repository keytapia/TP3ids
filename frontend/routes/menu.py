from flask import request, render_template, Blueprint
import requests

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/menu")
def menu():
    categoria = request.args.get("categoria")

    response_cat = requests.get("http://127.0.0.1:5000/api/categorias")
    categorias = response_cat.json()

    if not categoria and categorias:
        from flask import redirect, url_for
        return redirect(url_for('menu.menu', categoria=categorias[0]['nombre']))

    url = "http://127.0.0.1:5000/api/menu"
    if categoria:
        url += f"?categoria={categoria}"

    response = requests.get(url)
    platos = response.json()

    return render_template("menu.html", platos=platos, categorias=categorias, categoria_activa=categoria)