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


def obtener_platos_disponibles():

    conexion = obtener_conexion()

    try:
        with conexion.cursor(dictionary=True) as cursor:

            cursor.execute("""
                SELECT *
                FROM platos
                WHERE disponible = TRUE
            """)

            return cursor.fetchall()

    finally:
        conexion.close()


def obtener_platos_disponibles_por_categoria(categoria):

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
                AND platos.disponible = TRUE
            """, (categoria,))

            return cursor.fetchall()

    finally:
        conexion.close()


def actualizar_plato(plato_id, data):

    conexion = obtener_conexion()

    try:
        with conexion.cursor(dictionary=True) as cursor:

            # Verificar que exista el plato
            cursor.execute(
                "SELECT id FROM platos WHERE id = %s",
                (plato_id,)
            )

            if cursor.fetchone() is None:
                return None

            cursor.execute("""
                UPDATE platos
                SET categoria_id = %s,
                    nombre = %s,
                    descripcion = %s,
                    restricciones_alimentarias = %s,
                    precio = %s,
                    imagen = %s,
                    disponible = %s
                WHERE id = %s
            """, (
                data.get("categoria_id"),
                data.get("nombre"),
                data.get("descripcion"),
                data.get("restricciones_alimentarias"),
                data.get("precio"),
                data.get("imagen"),
                data.get("disponible"),
                plato_id
            ))

            conexion.commit()

            return True

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


def crear_plato (categoria_id, nombre, precio, imagen,
                descripcion=None,
                restricciones_alimentarias=None,
                disponible=True):

    con = obtener_conexion()

    try:
        with con.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO platos (
                    categoria_id,
                    nombre,
                    descripcion,
                    precio,
                    restricciones_alimentarias,
                    imagen,
                    disponible
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    categoria_id,
                    nombre,
                    descripcion,
                    precio,
                    restricciones_alimentarias,
                    imagen,
                    disponible
                )
            )

            con.commit()
            return cursor.lastrowid

    finally:
        con.close()