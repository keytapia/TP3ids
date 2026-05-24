from flask import Flask, render_template, Blueprint

reservas_bp = Blueprint('reservas', __name__)

# Reservas
@reservas_bp.route("/reservas")
def reservas():
    return render_template("reservas.html")