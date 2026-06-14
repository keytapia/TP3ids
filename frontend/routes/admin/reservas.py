from flask import Blueprint, render_template, request, redirect, url_for
from services.reservas import (
    obtener_reservas,
    obtener_reservas_por_estado,
    cancelar_reserva_admin
)

reservas_admin_bp = Blueprint("reservas_admin", __name__, url_prefix="/admin")

@reservas_admin_bp.route("/reservas")
def reservas():

    estado = request.args.get("estado", "todas")

    if estado == "todas":
        resultado = obtener_reservas()

    else:
        resultado = obtener_reservas_por_estado(estado)

    reservas = []

    if resultado["ok"]:
        reservas = resultado["data"]

    return render_template(
        "admin/reservas.html",
        reservas=reservas,
        estado_activo=estado
    )

@reservas_admin_bp.route("/reservas/cancelar/<int:id>", methods=["POST"])
def cancelar_reserva_admin_route(id):
    cancelar_reserva_admin(id)

    return redirect(url_for("reservas_admin.reservas"))