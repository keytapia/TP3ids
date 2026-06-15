from repositories.servicios import (
    listar_servicios_db,
    listar_servicio_por_id_db,
    crear_servicio_db,
    modificar_servicio_db,
    eliminar_servicio_db
)


# Listar todos los servicios
def listar_servicios():

    return listar_servicios_db()


# Listar un servicio por id
def listar_servicio_por_id(id):
    
    return listar_servicio_por_id_db(id)


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