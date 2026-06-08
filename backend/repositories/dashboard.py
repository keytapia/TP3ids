from db import obtener_conexion


def obtener_resumen_dashboard_db():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        (
            SELECT COUNT(*)
            FROM reservas
            WHERE fecha = CURDATE()
            AND estado = 'confirmada'
        ) AS reservas_hoy,

        (
            SELECT COUNT(*)
            FROM reservas
            WHERE fecha = CURDATE()
            AND estado = 'cancelada'
        ) AS cancelaciones_hoy
    """

    cursor.execute(consulta)

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado


def obtener_proximas_reservas_db():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        reservas.id,
        usuarios.nombre,
        usuarios.apellido,

        DATE_FORMAT(reservas.fecha, '%d/%m/%Y') AS fecha,

        TIME_FORMAT(reservas.horario, '%H:%i') AS horario,

        reservas.cantidad_personas

    FROM reservas

    JOIN usuarios
        ON usuarios.id = reservas.usuario_id

    WHERE reservas.estado = 'confirmada'
    AND reservas.fecha >= CURDATE()

    ORDER BY reservas.fecha ASC,
            reservas.horario ASC

    LIMIT 3
    """

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultado


def obtener_cancelaciones_hoy_db():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        usuarios.nombre,
        usuarios.apellido,

        DATE_FORMAT(reservas.fecha, '%d/%m/%Y') AS fecha,

        TIME_FORMAT(reservas.horario, '%H:%i') AS horario,
        
        reservas.cantidad_personas

    FROM reservas

    JOIN usuarios
        ON usuarios.id = reservas.usuario_id

    WHERE reservas.estado = 'cancelada'
    AND reservas.fecha = CURDATE()

    ORDER BY reservas.horario ASC
    """

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultado


def obtener_ultimas_reseñas_db():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        usuarios.nombre,
        usuarios.apellido,
        resenas.comentario,
        resenas.puntuacion

    FROM resenas

    JOIN usuarios
        ON usuarios.id = resenas.usuario_id

    ORDER BY resenas.fecha_publicacion DESC

    LIMIT 3
    """

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultado