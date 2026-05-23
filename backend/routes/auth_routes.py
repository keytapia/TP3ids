from flask import Blueprint, request, jsonify
from services.auth_service import login_usuario

auth_bp = Blueprint('auth_bp', __name__)

# Login
@auth_bp.route('/api/auth/login', methods=['POST'])
def login():

    data = request.get_json()

    email = data.get('email')
    contraseña = data.get('contraseña')
   
    usuario = login_usuario(email, contraseña)

    if usuario:
        return jsonify(usuario), 200

    return jsonify({
        "error": "Email o contraseña incorrectos"
    }), 401