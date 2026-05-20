from flask import jsonify

from db import obtener_conexion

# Estadísticas Generales (cantidad de: reservas totales, reservas canceladas, usuarios totales, reseñas totales)
def obtener_estadisticas_generales():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        (SELECT COUNT(*) FROM reservas) AS reservas_totales,

        (SELECT COUNT(*) FROM reservas
        WHERE estado='cancelada') AS reservas_canceladas,

        (SELECT COUNT(*) FROM usuarios) AS usuarios_totales,

        (SELECT COUNT(*) FROM resenas) AS resenas_totales
    """

    cursor.execute(consulta)

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return jsonify(resultado)

# Historial de reservas
def obtener_historial_reservas():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        reservas.id,
        usuarios.nombre,
        usuarios.apellido,
        reservas.fecha,
        reservas.horario,
        reservas.cantidad_personas,
        reservas.estado

    FROM reservas

    JOIN usuarios
    ON reservas.usuario_id = usuarios.id

    ORDER BY reservas.fecha DESC, reservas.horario DESC
    """

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(resultado)

# Usuarios con cancelaciones
def obtener_usuarios_cancelaciones():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        usuarios.id,
        usuarios.nombre,
        usuarios.apellido,
        usuarios.email,
        COUNT(*) AS cantidad_cancelaciones
    
    FROM usuarios

    JOIN reservas
    ON usuarios.id = reservas.usuario_id

    WHERE estado='cancelada'

    GROUP BY usuarios.id

    ORDER BY cantidad_cancelaciones DESC
    """

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(resultado)

# Platos mas populares
def obtener_platos_populares():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        platos.nombre,
        COUNT(*) AS veces_pedido

    FROM platos

    GROUP BY platos.id

    ORDER BY veces_pedido DESC
    """

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(resultado)

# Horarios mas solicitados
def obtener_horarios_populares():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT
        reservas.horario,
        COUNT(*) AS cantidad

    FROM reservas

    GROUP BY reservas.horario

    ORDER BY cantidad DESC
    """

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(resultado)

