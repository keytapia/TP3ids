from flask import request, jsonify, Blueprint

from services.usuarios import ( 
    buscar_usuario_por_email, 
    crear_usuario_cliente
)

usuarios_bp = Blueprint('usuarios', __name__, url_prefix="/api")

@usuarios_bp.route("/usuarios/registro", methods=["POST"])
def registro():

    data = request.get_json()

    nombre = data.get("nombre")
    apellido = data.get("apellido")
    email = data.get("email")
    telefono = data.get("telefono")
    contrasena = data.get("contrasena")

    if buscar_usuario_por_email(email):
        return jsonify({
            "error": "Ya existe una cuenta con ese email"
        }), 400

    usuario = crear_usuario_cliente(
        nombre,
        apellido,
        email,
        telefono,
        contrasena
    )

    return jsonify(usuario), 201