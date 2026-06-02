from flask import jsonify

from db import obtener_conexion

from datetime import date, timedelta
from services.usuarios_service import buscar_usuario_por_email, crear_usuario_cliente
from utils.validators import errores_api

# Mostrar todas las reservas
def listar_reservas():
    
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT * FROM reservas
    """
    
    cursor.execute(consulta)

    reservas = cursor.fetchall()
    
    for reserva in reservas:
        if reserva.get("fecha"):
            reserva["fecha"]=str(reserva["fecha"])
        if reserva.get("horario"):
            reserva["horario"]=str(reserva["horario"])
    
    cursor.close()
    conexion.close()

    return reservas


# Mostrar reservas por estado ("confirmada", "cancelada")
def listar_reservas_por_estado(estado):
    
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT * FROM reservas
        WHERE estado = %s
    """

    cursor.execute(consulta, (estado,))
    
    reservas = cursor.fetchall()
    
    for reserva in reservas:
        if reserva.get("fecha"):
            reserva["fecha"] = str(reserva["fecha"])
        if reserva.get("horario"):
            reserva["horario"] = str(reserva["horario"])

    cursor.close()
    conexion.close()

    return reservas


# Mostrar reserva por ID
def buscar_reserva_por_id(reserva_id):
    
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT
            id,
            usuario_id,
            mesa_id,
            fecha,
            horario,
            cantidad_personas,
            notas_adicionales,
            estado
        FROM reservas
        WHERE id = %s
    """

    cursor.execute(consulta, (reserva_id,))
        
    reserva = cursor.fetchone()

    cursor.close()
    conexion.close()

    return reserva


# Disponibilidad de reservas
def obtener_disponibilidad():
    
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    horarios_posibles = [
        "11:00",
        "11:30",
        "12:00",
        "12:30",
        "13:00",
        "13:30",
        "14:00",
        "14:30",
        "15:00",
        "15:30",
        "16:00",
        "16:30",
        "17:00",
        "17:30",
        "18:00",
        "18:30",
        "19:00",
        "19:30",
        "20:00",
        "20:30",
        "21:00",
        "21:30",
        "22:00",
        "22:30",
        "23:00"
    ]

    dias_a_mostrar = 28
    disponibilidad = []

    for i in range(dias_a_mostrar):
        fecha_actual = date.today() + timedelta(days=i)

        horarios_disponibles = []

        for horario in horarios_posibles:
            mesa_disponible = buscar_mesa_disponible_para_horario(
                cursor,
                fecha_actual,
                horario
            )

            if (mesa_disponible and mesa_disponible["capacidad_maxima"] is not None):
                capacidad_maxima = mesa_disponible["capacidad_maxima"]

                horarios_disponibles.append({
                    "horario": horario,
                    "capacidad_maxima_personas_por_mesa_disponibles": list(range(1, capacidad_maxima + 1))
                })

        if horarios_disponibles:
            disponibilidad.append({
                "fecha": fecha_actual.strftime("%Y-%m-%d"),
                "horarios": horarios_disponibles
            })

    cursor.close()
    conexion.close()

    return disponibilidad


# Buscar mesa disponible para una fecha, horario y cantidad de personas
def buscar_mesa_disponible(fecha, horario, cantidad_personas):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT *
        FROM mesas

        WHERE estado = 'disponible'
        AND capacidad >= %s

        AND id NOT IN (
            SELECT mesa_id
            FROM reservas
            WHERE fecha = %s
            AND horario = %s
            AND estado = 'confirmada'
        )

        ORDER BY capacidad ASC
        LIMIT 1
    """

    cursor.execute(
        consulta,
        (cantidad_personas, fecha, horario)
    )

    mesa = cursor.fetchone()

    cursor.close()
    conexion.close()

    return mesa


# Buscar una mesa disponible para un horario específico
def buscar_mesa_disponible_para_horario(cursor, fecha, horario):
    
    consulta = """
        SELECT MAX(mesas.capacidad) AS capacidad_maxima
        FROM mesas
        
        WHERE mesas.estado = 'disponible'
        AND mesas.id NOT IN (
            SELECT reservas.mesa_id
            FROM reservas
            WHERE reservas.fecha = %s
            AND reservas.horario = %s
            AND reservas.estado = 'confirmada'
        )
    """

    cursor.execute(consulta, (fecha, horario))
    resultado = cursor.fetchone()

    return resultado


# Cancelar reserva
def cancelar_reserva(reserva_id):
    
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta_actualizar = """
        UPDATE reservas
        SET estado = %s
        WHERE id = %s
    """

    cursor.execute(consulta_actualizar, ("cancelada", reserva_id))
    
    conexion.commit()

    filas_modificadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_modificadas > 0


# Crear reserva
def crear_reserva(
        nombre,
        apellido,
        email,
        telefono,
        mesa_id,
        fecha,
        horario,
        cantidad_personas,
        notas_adicionales=""
):

    usuario = buscar_usuario_por_email(email)
    if not usuario:
            usuario = crear_usuario_cliente(
                nombre="nombre",
                apellido="apellido",
                email="email",
                telefono="telefono"
            )
    if not usuario:
        return None
        
    usuario_id = usuario["id"]

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        consulta = """
         INSERT INTO reservas (
            usuario_id,
            mesa_id,
            fecha,
            horario,
            cantidad_personas,
            notas_adicionales,
            estado
          )
          VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
          consulta,
          (
            usuario_id,
            mesa_id,
            fecha,
            horario,
            cantidad_personas,
            notas_adicionales,
            "confirmada"
          )
        )

        conexion.commit()

        nuevo_id = cursor.lastrowid

        return {
            "id": nuevo_id,
            "usuario_id": usuario_id,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "telefono": telefono,
            "mesa_id": mesa_id,
            "fecha": fecha,
            "horario": horario,
            "cantidad_personas": cantidad_personas,
            "notas_adicionales": notas_adicionales,
            "estado": "confirmada"
        }
    except Exception as error:
        print("Error al crear reserva", error)
        conexion.rollback()
        return None
    
    finally:
        cursor.close()
        conexion.close()