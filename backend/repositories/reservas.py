from db import obtener_conexion
from datetime import datetime

def obtener_todas_las_reservas_db():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT 
                r.id,
                r.usuario_id,
                r.mesa_id,
                r.fecha,
                r.horario,
                r.cantidad_personas,
                r.notas_adicionales,
                r.estado,
                u.nombre,
                u.apellido,
                u.email,
                u.telefono
            FROM reservas r
            INNER JOIN usuarios u
                ON r.usuario_id = u.id
            ORDER BY r.fecha DESC, r.horario DESC
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        conexion.close()


def obtener_reservas_por_estado_db(estado):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT 
                r.id,
                r.usuario_id,
                r.mesa_id,
                r.fecha,
                r.horario,
                r.cantidad_personas,
                r.notas_adicionales,
                r.estado,
                u.nombre,
                u.apellido,
                u.email,
                u.telefono
            FROM reservas r
            INNER JOIN usuarios u
                ON r.usuario_id = u.id
            WHERE r.estado = %s
            ORDER BY r.fecha DESC, r.horario DESC
            """,
            (estado,)
        )

        return cursor.fetchall()

    finally:
        cursor.close()
        conexion.close()


def obtener_reserva_por_id_db(reserva_id):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
                r.id,
                r.usuario_id,
                r.mesa_id,
                r.fecha,
                r.horario,
                r.cantidad_personas,
                r.notas_adicionales,
                r.estado,
                u.nombre,
                u.apellido,
                u.email,
                u.telefono
            FROM reservas r
            INNER JOIN usuarios u
                ON r.usuario_id = u.id
            WHERE r.id = %s
            """,
            (reserva_id,)
        )

        return cursor.fetchone()

    finally:
        cursor.close()
        conexion.close()


def obtener_reservas_por_usuario_db(usuario_id):

    conexion = obtener_conexion()

    try:
        with conexion.cursor(dictionary=True) as cursor:

            consulta = """
                SELECT
                    id,
                    usuario_id,
                    mesa_id,
                    fecha,
                    horario,
                    cantidad_personas,
                    notas_adicionales,
                    estado
                FROM reservas
                WHERE usuario_id = %s
                ORDER BY fecha DESC, horario DESC
            """

            cursor.execute(
                consulta,
                (usuario_id,)
            )

            return cursor.fetchall()

    finally:
        conexion.close()


def buscar_mesa_disponible_db(
    fecha,
    horario,
    cantidad_personas
):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT *
            FROM mesas
            WHERE estado = 'disponible'
            AND capacidad >= %s
            AND id NOT IN (
                SELECT mesa_id
                FROM reservas
                WHERE fecha = %s
                AND horario = %s
                AND estado = 'confirmada'
            )
            ORDER BY capacidad ASC
            LIMIT 1
            """,
            (
                cantidad_personas,
                fecha,
                horario
            )
        )

        return cursor.fetchone()

    finally:
        cursor.close()
        conexion.close()


def buscar_mesa_disponible_para_horario_db(
    fecha,
    horario
):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
                MAX(mesas.capacidad) AS capacidad_maxima
            FROM mesas
            WHERE mesas.estado = 'disponible'
            AND mesas.id NOT IN (
                SELECT reservas.mesa_id
                FROM reservas
                WHERE reservas.fecha = %s
                AND reservas.horario = %s
                AND reservas.estado = 'confirmada'
            )
            """,
            (
                fecha,
                horario
            )
        )

        return cursor.fetchone()

    finally:
        cursor.close()
        conexion.close()


def obtener_mesas_por_estado_db(
    fecha,
    horario,
    cantidad_personas
):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
                m.id,
                m.numero,
                m.capacidad,
                m.estado,

                CASE
                    WHEN r.id IS NOT NULL THEN TRUE
                    ELSE FALSE
                END AS reservada,

                CASE
                    WHEN r.id IS NULL THEN TRUE
                    ELSE FALSE
                END AS seleccionable,

                CASE
                    WHEN m.capacidad >= %s THEN TRUE
                    ELSE FALSE
                END AS capacidad_suficiente

            FROM mesas m

            LEFT JOIN reservas r
                ON r.mesa_id = m.id
                AND r.fecha = %s
                AND r.horario = %s
                AND r.estado = 'confirmada'

            ORDER BY m.numero ASC
            """,
            (
                cantidad_personas,
                fecha,
                horario
            )
        )

        return cursor.fetchall()

    finally:
        cursor.close()
        conexion.close()


def cancelar_reserva_db(reserva_id):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            UPDATE reservas
            SET estado = %s
            WHERE id = %s
            """,
            (
                "cancelada",
                reserva_id
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


def crear_reserva_db(
    usuario_id,
    mesa_id,
    fecha,
    horario,
    cantidad_personas,
    notas_adicionales=""
):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:

        fecha_reserva = datetime.strptime(fecha, "%Y-%m-%d").date()
        fecha_actual = datetime.now().date()
        if fecha_reserva < fecha_actual:
            raise ValueError("La fecha de la reserva no puede ser anterior a la fecha actual")
        
        cursor.execute(
            """
            INSERT INTO reservas (
                usuario_id,
                mesa_id,
                fecha,
                horario,
                cantidad_personas,
                notas_adicionales,
                estado
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                usuario_id,
                mesa_id,
                fecha,
                horario,
                cantidad_personas,
                notas_adicionales,
                "confirmada"
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


def finalizar_reservas_vencidas_db():
    
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            UPDATE reservas
            SET estado = 'finalizada'
            WHERE estado = 'confirmada'
            AND TIMESTAMP(fecha,horario) < NOW()
            """
        )

        conexion.commit()

        return cursor.rowcount
    
    except Exception:
        conexion.rollback()
        raise

    finally:
        cursor.close()
        conexion.close()