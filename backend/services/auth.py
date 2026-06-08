from repositories.auth import (
    buscar_usuario_por_email_y_contrasena
)


def login_usuario(email, contrasena):

    usuario = buscar_usuario_por_email_y_contrasena(
        email,
        contrasena
    )

    if not usuario:
        return None

    return usuario