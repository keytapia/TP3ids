from db import obtener_conexion
from flask_jwt_extended import create_access_token

# Función para iniciar sesión
def login_usuario(email, contrasena):

    con = obtener_conexion()

    try:
        with con.cursor(dictionary=True) as cursor:

            sql = """
                SELECT id, nombre, apellido, email, rol
                FROM usuarios
                WHERE email = %s AND contrasena = %s
            """

            cursor.execute(sql, (email, contrasena))

            usuario = cursor.fetchone()

            if usuario:

                token = create_access_token(
                    identity=str(usuario["id"]),
                    additional_claims={
                        "rol": usuario["rol"]
                    }
                )

                return {
                    "token": token,
                    "usuario": usuario
                }

            return None

    finally:
        con.close()