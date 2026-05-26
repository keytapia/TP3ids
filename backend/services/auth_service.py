from flask import Flask, jsonify, Blueprint, request
from db import obtener_conexion
from datetime import datetime


# Función para iniciar sesión
def login_usuario(email, contrasena):

    con = obtener_conexion()

    try:
        with con.cursor(dictionary=True) as cursor:

            sql = """
                SELECT id, nombre, apellido, email, rol
                FROM usuarios
                WHERE email = %s AND contrasena = %s
            """

            cursor.execute(sql, (email, contrasena))

            usuario = cursor.fetchone()

            return usuario

    finally:
        con.close()