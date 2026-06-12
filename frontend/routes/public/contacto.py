from flask import Blueprint, render_template

contacto_bp = Blueprint('contacto', __name__)

# Contacto
@contacto_bp.route("/contacto")
def contacto():
    
    return render_template("public/contacto.html")