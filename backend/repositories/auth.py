from db import obtener_conexion


def buscar_usuario_por_email_y_contrasena(email, contrasena):

    conexion = obtener_conexion()

    try:
        with conexion.cursor(dictionary=True) as cursor:

            consulta = """
                SELECT
                    id,
                    nombre,
                    apellido,
                    email,
                    telefono,
                    rol
                FROM usuarios
                WHERE email = %s
                AND contrasena = %s
            """

            cursor.execute(
                consulta,
                (email, contrasena)
            )

            return cursor.fetchone()

    finally:
        conexion.close()