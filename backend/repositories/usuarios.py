from db import obtener_conexion


def buscar_usuario_por_email_db(email):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT *
            FROM usuarios
            WHERE email = %s
            """,
            (email,)
        )

        return cursor.fetchone()

    finally:
        cursor.close()
        conexion.close()


def crear_usuario_cliente_db(
    nombre,
    apellido,
    email,
    telefono,
    contrasena
):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            INSERT INTO usuarios (
                nombre,
                apellido,
                email,
                telefono,
                contrasena,
                rol
            )
            VALUES (%s, %s, %s, %s, %s, 'cliente')
            """,
            (
                nombre,
                apellido,
                email,
                telefono,
                contrasena
            )
        )

        conexion.commit()

        return {
            "id": cursor.lastrowid
        }

    except Exception:
        conexion.rollback()
        raise

    finally:
        cursor.close()
        conexion.close()