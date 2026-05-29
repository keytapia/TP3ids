from flask import request, jsonify, Blueprint

from services.auth_service import (
    login_usuario
)

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/api/auth')


# Login
@auth_bp.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    email = data.get('email')
    contrasena = data.get('contrasena')
   
    usuario = login_usuario(email, contrasena)

    if usuario:
        return jsonify(usuario), 200

    return jsonify({"error": "Email o contraseña incorrectos"}), 401