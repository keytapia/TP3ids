from flask import Flask, jsonify, Blueprint, request
from db import obtener_conexion
import re
from datetime import datetime


#posibles errores de reserva

def construir_error_api(code: str, message: str, description: str, level: str = "error") -> dict:
    return {
        "errors": [{
            "code": code,
            "message": message,
            "level": level,
            "description": description
        }]
    }


#Disponibilidad de reservas que ve el cliente

def obtener_disponibilidad():
    conexion = obtener_conexion()
    cursor = None

    try:
        cursor = conexion.cursor(dictionary=True)

        horarios_posibles = [
            "11:00",
            "12:00",
            "13:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00"
        ]

        dias_a_mostrar = 14
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

                if mesa_disponible:
                    capacidad_maxima = mesa_disponible["capacidad_maxima"]

                    horarios_disponibles.append({
                        "horario": horario,
                        "cantidad_personas_disponibles": list(range(1, capacidad_maxima + 1))
                    })

            if horarios_disponibles:
                disponibilidad.append({
                    "fecha": fecha_actual.strftime("%Y-%m-%d"),
                    "horarios": horarios_disponibles
                })

        return disponibilidad

    except Exception as error:
        print("Error al obtener disponibilidad:", error)
        return None

    finally:
        if cursor:
            cursor.close()

        conexion.close()

def buscar_mesa_disponible_para_horario(cursor, fecha, horario):
    consulta = """
        SELECT MAX(m.capacidad) AS capacidad_maxima
        FROM mesas m
        WHERE m.estado = 'disponible'
        AND m.id NOT IN (
            SELECT r.mesa_id
            FROM reservas r
            WHERE r.fecha = %s
            AND r.horario = %s
            AND r.estado = 'confirmada'
        )
    """

    cursor.execute(consulta, (fecha, horario))
    resultado = cursor.fetchone()

    if not resultado:
        return None

    if resultado["capacidad_maxima"] is None:
        return None

    return resultado


#Listar reservas por ID
def buscar_reserva_por_id(reserva_id):
    conexion = obtener_conexion()
    cursor = None

    try:
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

        return reserva

    except Exception as error:
        print("Error al buscar reserva por ID:", error)
        return None

    finally:
        if cursor:
            cursor.close()

        conexion.close()

#cancelar reserva por parte del cliente
def cancelar_reserva_cliente(reserva_id):
    conexion = obtener_conexion()
    cursor = None

    try:
        cursor = conexion.cursor(dictionary=True)

        consulta_actualizar = """
            UPDATE reservas
            SET estado = %s
            WHERE id = %s
        """

        cursor.execute(consulta_actualizar, ("cancelada", reserva_id))
        conexion.commit()

        return buscar_reserva_por_id(reserva_id)

    except Exception as error:
        print("Error al cancelar reserva desde cliente:", error)
        conexion.rollback()
        return None

    finally:
        if cursor:
            cursor.close()

        conexion.close()

# Función para listar todas las reservas
def listar_reservas():
    con = obtener_conexion()
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM reservas")
            reservas = cursor.fetchall()
            return reservas
    finally:        con.close()

# Función para listar reservas por estado
def listar_reservas_por_estado(estado):
    con = obtener_conexion()
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM reservas WHERE estado = %s", (estado,))
            reservas = cursor.fetchall()
            return reservas
    finally:
        con.close()

# Función para cancelar una reserva por id cambiando su estado a "cancelada"
def cancelar_reserva(reserva_id):
    con = obtener_conexion()
    try:
        with con.cursor() as cursor:
            cursor.execute("UPDATE reservas SET estado = 'cancelada' WHERE id = %s", (reserva_id,))
            con.commit()
            return cursor.rowcount > 0  # Devuelce True si se actualizó al menos una fila
    finally:
        con.close()
