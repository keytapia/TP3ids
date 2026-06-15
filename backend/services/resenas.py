from repositories.resenas import (
    obtener_resenas_db,
    obtener_resena_por_id_db,
    obtener_reserva_para_resena_db,
    obtener_resena_por_reserva_db,
    crear_resena_db
)
from services.reservas import (
    finalizar_reservas_vencidas
)

def listar_resenas():
    resenas = obtener_resenas_db()

    for resena in resenas:
        if resena.get("fecha_publicacion"):
            resena["fecha_publicacion"] = str(resena["fecha_publicacion"])
    
    return resenas


def buscar_resena_por_id(id):
    resena = obtener_resena_por_id_db(id)

    if resena and resena.get("fecha_publicacion"):
        resena["fecha_publicacion"] = str(resena["fecha_publicacion"])

    return resena


def crear_resena(reserva_id, nombre, apellido, comentario, puntuacion):

    finalizar_reservas_vencidas()
    
    if not reserva_id or not nombre or not apellido or not comentario or not puntuacion:
        
        return {
            "ok": False,
            "mensaje": "Faltan datos obligatorios"
        }
    
    try:
        reserva_id = int(reserva_id)
        puntuacion = int(puntuacion)
    
    except ValueError:
        return {
            "ok": False,
            "mensaje": "Reserva o puntuacion invalida"
        }
    
    if puntuacion < 1 or puntuacion > 5:

        return {
            "ok": False,
            "mensaje": "La puntuacion debe estar entre 1 y 5"
        }
    
    if reserva_id < 0:

        return {
            "ok": False,
            "mensaje": "¿Perdon? ¿Desde cuando hay reservas negativas?"
        }
    
    reserva = obtener_reserva_para_resena_db(reserva_id)

    if not reserva:

        return {
            "ok": False,
            "mensaje": "La reserva no existe"
        }
    
    if reserva["estado"] != "finalizada":

        return {
            "ok": False,
            "mensaje": "Solo se pueden reseñar reservas finalizadas"
        }
    
    if reserva["nombre"].strip().lower() != nombre.strip().lower():

        return {
            "ok": False,
            "mensaje": "El nombre no coincide con el de la reserva"
        }
    
    if reserva["apellido"].strip().lower() != apellido.strip().lower():

        return {
            "ok": False,
            "mensaje": "El apellido no coincide con el de la reserva"
        }
    
    resena_existente = obtener_resena_por_reserva_db(reserva_id)

    if resena_existente:

        return {
            "ok": False,
            "mensaje": "La reseña de esa reserva ya existe"
        }
    
    nueva_resena = crear_resena_db(
        usuario_id=reserva["usuario_id"],
        reserva_id=reserva_id,
        comentario=comentario,
        puntuacion=puntuacion
    )

    return {
        "ok": False,
        "mensaje": "Reseña creada exitosamente!",
        "resena": nueva_resena
    }