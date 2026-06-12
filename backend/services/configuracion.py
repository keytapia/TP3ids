from repositories.configuracion import (
    obtener_configuracion,
    actualizar_configuracion
)


def obtener_datos_configuracion():

    return obtener_configuracion()


def guardar_configuracion(data):

    actualizar_configuracion(
        nombre=data.get("nombre"),
        email=data.get("email"),
        telefono=data.get("telefono"),
        ubicacion=data.get("ubicacion"),
        horario=data.get("horario")
    )

    return {
        "mensaje": "Configuración actualizada correctamente."
    }