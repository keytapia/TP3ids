from flask import Flask, render_template, Blueprint

contacto_bp = Blueprint('contacto', __name__)

# Contacto
@contacto_bp.route("/contacto")
def contacto():
    return render_template("contacto.html")