from flask import request, render_template, Blueprint, redirect, url_for

from services.menu import (
    obtener_categorias,
    obtener_menu_publico
)

menu_bp = Blueprint("menu", __name__)


@menu_bp.route("/menu")
def menu():

    categoria = request.args.get("categoria")

    resp_categorias = obtener_categorias()
    categorias = resp_categorias["data"] if resp_categorias["ok"] else []

    if not categorias:
        return render_template(
            "public/menu.html",
            platos=[],
            categorias=[],
            categoria_activa=None
        )

    if not categoria:
        return redirect(
            url_for(
                "menu.menu",
                categoria=categorias[0]["nombre"]
            )
        )

    resp_menu = obtener_menu_publico(categoria)
    platos = resp_menu["data"] if resp_menu["ok"] else []

    return render_template(
        "public/menu.html",
        platos=platos,
        categorias=categorias,
        categoria_activa=categoria
    )