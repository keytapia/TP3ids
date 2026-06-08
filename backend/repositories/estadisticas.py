from db import obtener_conexion


def obtener_reservas_totales_db():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT COUNT(*) AS reservas_totales
    FROM reservas
    """

    cursor.execute(consulta)

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado


def obtener_cancelaciones_mes_db():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT COUNT(*) AS cancelaciones_mes
    FROM reservas
    WHERE estado = 'cancelada'
    AND fecha >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
    """

    cursor.execute(consulta)

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado


def obtener_reservas_por_horario_db():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        TIME_FORMAT(horario, '%H:%i') AS horario,
        COUNT(*) AS cantidad

    FROM reservas

    GROUP BY horario

    ORDER BY horario
    """

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultado


def obtener_reservas_por_dia_db():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        DATE_FORMAT(fecha, '%d/%m') AS fecha,
        COUNT(*) AS cantidad

    FROM reservas

    GROUP BY fecha

    ORDER BY fecha
    """

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultado