from repositories.menu import (
    obtener_todos_los_platos,
    obtener_plato_por_id,
    obtener_platos_por_categoria,
    actualizar_plato,
    eliminar_plato_por_id,
    obtener_categorias
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