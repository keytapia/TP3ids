from db import obtener_conexion


def obtener_configuracion():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM configuracion
        LIMIT 1
    """)

    configuracion = cursor.fetchone()

    cursor.close()
    conexion.close()

    return configuracion


def actualizar_configuracion(
    nombre,
    email,
    telefono,
    ubicacion,
    dias,
    horario
):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE configuracion
        SET
            nombre = %s,
            email = %s,
            telefono = %s,
            ubicacion = %s,
            dias = %s,
            horario = %s
        WHERE id = 1
    """, (
        nombre,
        email,
        telefono,
        ubicacion,
        dias,
        horario
    ))

    conexion.commit()

    cursor.close()
    conexion.close()