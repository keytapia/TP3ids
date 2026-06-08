from db import obtener_conexion


def listar_servicios_db():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT *
            FROM servicios
            """
        )

        return cursor.fetchall()

    finally:
        cursor.close()
        conexion.close()


def crear_servicio_db(nombre, descripcion):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            INSERT INTO servicios (
                nombre,
                descripcion
            )
            VALUES (%s, %s)
            """,
            (
                nombre,
                descripcion
            )
        )

        conexion.commit()

        nuevo_id = cursor.lastrowid

        cursor.execute(
            """
            SELECT *
            FROM servicios
            WHERE id = %s
            """,
            (nuevo_id,)
        )

        return cursor.fetchone()

    except Exception:
        conexion.rollback()
        raise

    finally:
        cursor.close()
        conexion.close()


def modificar_servicio_db(
    nombre,
    descripcion,
    servicio_id
):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            UPDATE servicios
            SET
                nombre = %s,
                descripcion = %s
            WHERE id = %s
            """,
            (
                nombre,
                descripcion,
                servicio_id
            )
        )

        conexion.commit()

        return cursor.rowcount > 0

    except Exception:
        conexion.rollback()
        raise

    finally:
        cursor.close()
        conexion.close()


def eliminar_servicio_db(servicio_id):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            DELETE FROM servicios
            WHERE id = %s
            """,
            (servicio_id,)
        )

        conexion.commit()

        return cursor.rowcount > 0

    except Exception:
        conexion.rollback()
        raise

    finally:
        cursor.close()
        conexion.close()