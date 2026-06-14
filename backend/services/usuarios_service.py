from db import obtener_conexion


# Buscar usuario por email
def buscar_usuario_por_email(email):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT *
        FROM usuarios
        WHERE email = %s
    """

    cursor.execute(consulta, (email,))
    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    return usuario


# Crear usuario cliente
def crear_usuario_cliente(nombre, apellido, email, telefono):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        INSERT INTO usuarios (
            nombre,
            apellido,
            email,
            telefono,
            rol
        )
        VALUES (%s, %s, %s, %s, 'cliente')
    """

    cursor.execute(
        consulta,
        (
            nombre,
            apellido,
            email,
            telefono
        )
    )

    conexion.commit()

    nuevo_id = cursor.lastrowid

    cursor.close()
    conexion.close()

    return {
        "id": nuevo_id,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "telefono": telefono,
        "rol": "cliente"
    }

#crear cliente en registrate
def registrate_usuario_cliente(nombre, email, contrasena):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        INSERT INTO usuarios (
            nombre,
            email,
            contrasena,
            rol
        )
        VALUES (%s, %s, %s, 'cliente')
    """

    cursor.execute(
        consulta,
        (
            nombre,
            email,
            contrasena
        )
    )

    conexion.commit()

    nuevo_id = cursor.lastrowid

    cursor.close()
    conexion.close()

    return {
        "id": nuevo_id,
        "nombre": nombre,
        "email": email,
        "contrasena": contrasena,
        "rol": "cliente"
    }