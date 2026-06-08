from repositories.menu import (
    obtener_todos_los_platos,
    obtener_plato_por_id,
    obtener_platos_por_categoria,
    actualizar_plato,
    eliminar_plato_por_id,
    obtener_categorias,
    crear_plato
)


# Obtener todos los platos del menú
def listar_menu():

    return obtener_todos_los_platos()


# Obtener un plato por id
def obtener_plato_id(plato_id):

    return obtener_plato_por_id(plato_id)


# Obtener platos por categoria
def listar_menu_por_categoria(categoria):

    return obtener_platos_por_categoria(categoria)


# Modificar un plato
def modificar_plato(id, data):

    return actualizar_plato(id, data)


# Eliminar un plato
def eliminar_plato(id):

    return eliminar_plato_por_id(id)


# Listar categorías
def listar_categorias():

    return obtener_categorias()


# Crear plato
def agregar_plato(
    categoria_id,
    nombre,
    precio,
    imagen,
    descripcion=None,
    restricciones_alimentarias=None,
    disponible=True
):

    if not nombre:
        return {
            "ok": False,
            "mensaje": "El nombre del plato es obligatorio."
        }

    if precio <= 0:
        return {
            "ok": False,
            "mensaje": "El precio debe ser mayor a cero."
        }

    try:

        plato_id = crear_plato(
            categoria_id=categoria_id,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            restricciones_alimentarias=restricciones_alimentarias,
            imagen=imagen,
            disponible=disponible
        )

        return {
            "ok": True,
            "mensaje": "Plato creado correctamente.",
            "id": plato_id
        }

    except Exception as e:

        return {
            "ok": False,
            "mensaje": str(e)
        }