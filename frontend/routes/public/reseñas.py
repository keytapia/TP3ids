from flask import Flask, render_template, Blueprint

reseñas_bp = Blueprint('reseñas', __name__)

# Reseñas
@reseñas_bp.route("/reseñas")
def reseñas():
    return render_template("public/reseñas.html")