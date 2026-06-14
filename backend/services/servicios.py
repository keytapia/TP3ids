from repositories.servicios import (
    listar_servicios_db,
    crear_servicio_db,
    modificar_servicio_db,
    eliminar_servicio_db
)


# Listar todos los servicios
def listar_servicios():

    return listar_servicios_db()


# Crear un servicio
def crear_servicio(
    nombre,
    disponible
):

    return crear_servicio_db(
        nombre,
        disponible
    )


# Modificar un servicio
def modificar_servicio(
    nombre,
    disponible,
    servicio_id
):

    return modificar_servicio_db(
        nombre,
        disponible,
        servicio_id
    )


# Eliminar un servicio
def eliminar_servicio(servicio_id):

    return eliminar_servicio_db(
        servicio_id
    )