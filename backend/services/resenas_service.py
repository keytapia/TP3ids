from db import obtener_conexion

def obtener_resenas():

    con = obtener_conexion()
    try:
        with con.cursor() as cursor:

            sql = """
            SELECT
                r.id,
                u.nombre,
                r.comentario,
                r.puntuacion,
                r.fecha_publicacion
            FROM resenas r
            INNER JOIN usuarios u
                ON r.usuario_id = u.id
            ORDER BY r.fecha_publicacion DESC
            """

            cursor.execute(sql)

            return cursor.fetchall()

    finally:
        con.close()

def obtener_resena_por_id(id_resena):

    con = obtener_conexion()

    try:
        with con.cursor() as cursor:

            sql = """
            SELECT
                r.id,
                u.nombre,
                r.comentario,
                r.puntuacion,
                r.fecha_publicacion
            FROM resenas r
            INNER JOIN usuarios u
                ON r.usuario_id = u.id
            WHERE r.id = %s
            """

            cursor.execute(sql, (id_resena,))

            return cursor.fetchone()

    finally:
        con.close()


def crear_resena(
    usuario_id,
    reserva_id,
    comentario,
    puntuacion
):

    con = obtener_conexion()

    try:
        with con.cursor() as cursor:

            sql_verificar = """
            SELECT *
            FROM reservas
            WHERE id = %s
            AND usuario_id = %s
            """

            cursor.execute(
                sql_verificar,
                (reserva_id, usuario_id)
            )

            reserva = cursor.fetchone()

            if not reserva:

                return {
                    "ok": False,
                    "error": "La reserva no existe para ese usuario"
                }

            sql_insert = """
            INSERT INTO resenas
            (
                usuario_id,
                reserva_id,
                comentario,
                puntuacion
            )
            VALUES
            (%s,%s,%s,%s)
            """

            cursor.execute(
                sql_insert,
                (
                    usuario_id,
                    reserva_id,
                    comentario,
                    puntuacion
                )
            )

            con.commit()

            return {
                "ok": True,
                "mensaje": "Reseña creada correctamente"
            }

    finally:
        con.close()