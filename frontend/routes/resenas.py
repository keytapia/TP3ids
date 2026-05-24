from flask import Flask, render_template, Blueprint

reservas_bp = Blueprint('resenas', __name__)

# Reseñas
@resenas_bp.route("/resenas")
def resenas():
    return render_template("resenas.html")