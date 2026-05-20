from flask import Flask, jsonify, Blueprint, request
from db import get_connection
import re


# Funcion para listar todos los servicios
def listar_servicios():
	con = get_connection()
	try:
	     with con.cursor() as cursor:
		cursor.execute("SELECT * FROM servicios")
		servicios = cursor.fetchall()
		return servicios
	finally:
		con.close()



# Funcion para modificar servicio
def modificar_servicio(nombre, descripcion, id):
	con = get_connection()
	try:
	     with con.cursor() as cursor:
	     	cursor.execute("UPDATE servicios SET nombre = %s, descripcion = %s WHERE id = %s", (nombre, descripcion, id))
		con.commit()
		return cursor.rowcount > 0  # Devuelce True si se actualizó al menos una fila
	finally:
		con.close()



# Funcion para crear un servicio
def crear_servicio(nombre, descripcion):
	con = get_connection()
	try:
	    with con.cursor() as cursor:
		cursor.execute("INSERT INTO servicios (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
		con.commit()
		return nuevo_servicio
	finally:
		con.close()



# Funcion para eliminar un servicio
def eliminar_servicio(id):
	con = get_connection()
	try:
	     with con.cursor() as cursor:
		cursor.execute("DELETE FROM servicios WHERE id = %s", (id))
		con.commit()
	finally:
		con.close()