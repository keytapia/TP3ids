from flask import Flask, render_template, Blueprint

nosotros_bp = Blueprint('nosotros', __name__)

# Nosotros
@nosotros_bp.route("/nosotros")
def nosotros():
    return render_template("public/nosotros.html")