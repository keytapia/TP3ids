from flask import request, jsonify, Blueprint

from services.usuarios_service import ( 
    buscar_usuario_por_email, 
    registrate_usuario_cliente
)

usuarios_bp = Blueprint('usuarios', __name__, url_prefix="/api/usuarios")

@usuarios_bp.route("/registro", methods=["POST"])
def registro():

    data = request.get_json()

    nombre = data.get("nombre")
    email = data.get("email")
    contrasena = data.get("contrasena")

    if buscar_usuario_por_email(email):
        return jsonify({
            "error": "Ya existe una cuenta con ese email"
        }), 400

    usuario = registrate_usuario_cliente(
        nombre,
        email,
        contrasena
    )

    return jsonify(usuario), 201
