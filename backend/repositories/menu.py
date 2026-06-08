from db import obtener_conexion


def obtener_todos_los_platos():

    conexion = obtener_conexion()

    try:
        with conexion.cursor(dictionary=True) as cursor:

            cursor.execute("""
                SELECT *
                FROM platos
            """)

            return cursor.fetchall()

    finally:
        conexion.close()


def obtener_plato_por_id(plato_id):

    conexion = obtener_conexion()

    try:
        with conexion.cursor(dictionary=True) as cursor:

            cursor.execute("""
                SELECT *
                FROM platos
                WHERE id = %s
            """, (plato_id,))

            return cursor.fetchone()

    finally:
        conexion.close()


def obtener_platos_por_categoria(categoria):

    conexion = obtener_conexion()

    try:
        with conexion.cursor(dictionary=True) as cursor:

            cursor.execute("""
                SELECT
                    platos.*,
                    categorias_platos.nombre AS categoria
                FROM platos

                JOIN categorias_platos
                ON platos.categoria_id = categorias_platos.id

                WHERE LOWER(categorias_platos.nombre) = %s
            """, (categoria,))

            return cursor.fetchall()

    finally:
        conexion.close()


def actualizar_plato(plato_id, data):

    conexion = obtener_conexion()

    try:
        with conexion.cursor(dictionary=True) as cursor:

            cursor.execute("""
                UPDATE platos
                SET categoria_id = %s,
                    nombre = %s,
                    descripcion = %s,
                    precio = %s,
                    imagen = %s,
                    disponible = %s
                WHERE id = %s
            """, (
                data.get("categoria_id"),
                data.get("nombre"),
                data.get("descripcion"),
                data.get("precio"),
                data.get("imagen"),
                data.get("disponible"),
                plato_id
            ))

            conexion.commit()

            return cursor.rowcount

    finally:
        conexion.close()


def eliminar_plato_por_id(plato_id):

    conexion = obtener_conexion()

    try:
        with conexion.cursor(dictionary=True) as cursor:

            cursor.execute("""
                DELETE FROM platos
                WHERE id = %s
            """, (plato_id,))

            conexion.commit()

            return cursor.rowcount

    finally:
        conexion.close()


def obtener_categorias():

    conexion = obtener_conexion()

    try:
        with conexion.cursor(dictionary=True) as cursor:

            cursor.execute("""
                SELECT *
                FROM categorias_platos
            """)

            return cursor.fetchall()

    finally:
        conexion.close()