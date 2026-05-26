from flask import Flask, jsonify, Blueprint, request
from db import obtener_conexion
import re


# Listar todos los servicios
def listar_servicios():
    con = obtener_conexion()
    try:
        with con.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM servicios")
            servicios = cursor.fetchall()
            return servicios
    finally:
        con.close()


# Crear un servicio
def crear_servicio(nombre, descripcion):
	con = obtener_conexion()
	try:
		with con.cursor(dictionary=True) as cursor:
			cursor.execute("INSERT INTO servicios (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
			con.commit()
			nuevo_id = cursor.lastrowid
			cursor.execute("SELECT * FROM servicios WHERE id=%s", (nuevo_id,))
			nuevo_servicio = cursor.fetchone()
			return nuevo_servicio
	finally:
		con.close()


# Modificar un servicio
def modificar_servicio(nombre, descripcion, id):
	con = obtener_conexion()
	try:
		with con.cursor(dictionary=True) as cursor:
			cursor.execute("UPDATE servicios SET nombre = %s, descripcion = %s WHERE id = %s", (nombre, descripcion, id))
			con.commit()
			return cursor.rowcount > 0  # Devuelve True si se actualizó al menos una fila
	finally:
		con.close()


# Eliminar un servicio
def eliminar_servicio(id):
	con = obtener_conexion()
	try:
		with con.cursor(dictionary=True) as cursor:
			cursor.execute("DELETE FROM servicios WHERE id = %s", (id,))
			con.commit()
			return cursor.rowcount > 0 # Devuelve True si se eliminó al menos una fila
	finally:
		con.close()