from flask import Flask, jsonify, Blueprint, request
from db import obtener_conexion
import re
from datetime import datetime

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