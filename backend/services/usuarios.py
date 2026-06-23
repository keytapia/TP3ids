from repositories.usuarios import (
    buscar_usuario_por_email_db,
    crear_usuario_cliente_db
)


# Buscar usuario por email
def buscar_usuario_por_email(email):

    return buscar_usuario_por_email_db(email)


# Crear usuario cliente
def crear_usuario_cliente(
    nombre,
    apellido,
    email,
    telefono,
    contrasena=None
):

    nuevo_usuario = crear_usuario_cliente_db(
        nombre,
        apellido,
        email,
        telefono,
        contrasena
    )

    return {
        "id": nuevo_usuario["id"],
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "telefono": telefono,
        "contrasena": contrasena,
        "rol": "cliente"
    }