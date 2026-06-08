from flask import request, jsonify, Blueprint

from services.dashboard_service import (
    obtener_estadisticas_generales, 
    obtener_historial_reservas, 
    obtener_usuarios_cancelaciones, 
    obtener_platos_populares, 
    obtener_horarios_populares
)

from services.reservas_service import (
    listar_reservas,
    listar_reservas_por_estado,
    cancelar_reserva
)

from services.menu_service import (
    listar_menu,
    listar_menu_por_categoria, 
    obtener_plato_id,
    modificar_plato,
    eliminar_plato,
    crear_plato
)

from services.servicios_service import (
    listar_servicios,
    modificar_servicio,
    crear_servicio,
    eliminar_servicio
)

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')



# -------------------------------- DASHBOARD -------------------------------- #

# Estadísticas Generales (cantidad de reservas, usuarios totales, reseñas totales)
@admin_bp.route('/dashboard', methods=['GET'])
def estadisticas_generales():
    
    return obtener_estadisticas_generales(), 200


# Historial de reservas
@admin_bp.route('/dashboard/historial-reservas', methods=['GET'])
def historial_reservas():
    
    return obtener_historial_reservas(), 200


# Usuarios con cancelaciones
@admin_bp.route('/dashboard/usuarios-cancelaciones', methods=['GET'])
def usuarios_cancelaciones():
    
    return obtener_usuarios_cancelaciones(), 200


# Platos mas populares
@admin_bp.route('/dashboard/platos-populares', methods=['GET'])
def platos_populares():
    
    return obtener_platos_populares(), 200


# Horarios mas solicitados
@admin_bp.route('/dashboard/horarios-populares', methods=['GET'])
def horarios_populares():
    
    return obtener_horarios_populares(), 200


# -------------------------------- RESERVAS -------------------------------- #

# Visualizar las reservas
@admin_bp.route('/reservas', methods=['GET'])
def get_reservas():
    
    reservas = listar_reservas()
    
    return jsonify(reservas), 200


# Visualizar el estado de las reservas (filtra por estado)
@admin_bp.route('/reservas/estado/<estado>', methods=['GET'])
def get_reservas_por_estado(estado):
    
    reservas = listar_reservas_por_estado(estado)
    
    return jsonify(reservas), 200


# Cancelar una reserva por id cambiando su estado a "cancelada"
@admin_bp.route('/reservas/cancelar/<int:reserva_id>', methods=['PATCH'])
def delete_reserva(reserva_id):
    
    resultado = cancelar_reserva(reserva_id)
    
    if resultado:
        return jsonify({"mensaje": "Reserva cancelada exitosamente"}), 200
    else:
        return jsonify({"mensaje": "No se pudo cancelar la reserva"}), 400


# -------------------------------- MENÚ -------------------------------- #

# Listar menú (completo o por categorias)
@admin_bp.route("/menu", methods=["GET"])
def get_menu():
    categoria = request.args.get('categoria')

    if categoria:
        categoria = categoria.lower()
        menu = listar_menu_por_categoria(categoria)
        if not menu:
            return jsonify({"message":"No hay ningún plato en esa categoria"}), 404
        return jsonify(menu),200
    menu = listar_menu()
    return jsonify(menu), 200


# Filtrar un plato especifico por numero id
@admin_bp.route('/menu/<int:id>', methods=['GET'])
def get_plato(id):
    plato = obtener_plato_id(id)

    if not plato:
        return jsonify({"message": "EL plato no pudo ser encontrado"}), 404
    
    return jsonify(plato), 200

# Crear un plato del menú
@admin_bp.route("/menu", methods=["POST"])
def post_plato():

    data = request.get_json()

    categoria_id = data.get("categoria_id")
    nombre = data.get("nombre")
    precio = data.get("precio")
    imagen = data.get("imagen")

    descripcion = data.get("descripcion")
    restricciones = data.get("restricciones_alimentarias")

    if not categoria_id or not nombre or precio is None:
        return jsonify({
            "error": "categoria_id, nombre y precio son obligatorios"
        }), 400

    try:
        precio = float(precio)
    except:
        return jsonify({"error": "Precio inválido"}), 400

    if precio < 0:
        return jsonify({"error": "El precio no puede ser negativo"}), 400

    id = crear_plato(
        categoria_id=categoria_id,
        nombre=nombre,
        precio=precio,
        imagen=imagen,
        descripcion=descripcion,
        restricciones_alimentarias=restricciones
    )

    return jsonify({
        "mensaje": "Plato creado correctamente",
        "id": id
    }), 201

# Modificar un plato del menú
@admin_bp.route("/menu/<int:id>", methods=["PUT"])
def put_plato(id):

    data = request.get_json()

    if modificar_plato(id, data) == 0:
        return jsonify({"error": "Plato no encontrado"}), 404

    return jsonify({"mensaje": "Plato modificado exitosamente"}), 200


# Eliminar un plato del menú
@admin_bp.route("/menu/<int:id>", methods=["DELETE"])
def delete_plato(id):

    if eliminar_plato(id) == 0:
        return jsonify({"error": "Plato no encontrado"}), 404

    return jsonify({"mensaje": "Plato eliminado exitosamente"}), 200


# -------------------------------- RESEÑAS -------------------------------- #

# Eliminar una reseña por id
@admin_bp.route("/reseñas/<int:id>", methods=["DELETE"])
def delete_reseña(id):

    # Acá va la función del servicio para eliminar la reseña
    # (O capaz poner una columna a la tabla 'resenas' donde diga estado='publica' u 'oculta', y hacer un patch en vez de eliminar para actualizar el estado)
    # resultado = eliminar_reseña(id)

    # if resultado:
    #     return jsonify({"mensaje": "Reseña eliminada exitosamente"}), 200
    # else:
    #     return jsonify({"mensaje": "No se pudo eliminar la reseña"}), 400
    return jsonify({"mensaje": "Falta hacer función de eliminar reseña"}), 200


# -------------------------------- SERVICIOS -------------------------------- #

# Listar todos los servicios
@admin_bp.route('/servicios', methods=['GET'])
def get_servicios():
    
    servicios = listar_servicios()
    
    return jsonify(servicios), 200


# Crear un servicio
@admin_bp.route('/servicios', methods=['POST'])
def post_servicio():
    
    data = request.get_json()

    nombre = data.get("nombre")
    descripcion = data.get("descripcion")

    if not nombre:
        return jsonify({"mensaje": "El nombre es obligatorio"}), 400

    servicio = crear_servicio(nombre, descripcion)

    return jsonify({"mensaje": "Servicio creado correctamente"}), 201


# Modificar un servicio
@admin_bp.route('/servicios/<int:id>', methods=['PUT'])
def put_servicio(id):

    data = request.get_json()

    nombre = data.get("nombre")
    descripcion = data.get("descripcion")

    actualizado = modificar_servicio(nombre, descripcion, id)

    if not actualizado:
        return jsonify({"mensaje": "No se pudo modificar el servicio"}), 404

    return jsonify({"mensaje": "Servicio actualizado correctamente"}), 200


# Eliminar un servicio
@admin_bp.route('/servicios/<int:id>', methods=['DELETE'])
def delete_servicio(id):

    eliminado = eliminar_servicio(id)

    if not eliminado:
        return jsonify({"mensaje": "No se pudo eliminar el servicio"}), 404

    return jsonify({"mensaje": "Servicio eliminado correctamente"}), 200

