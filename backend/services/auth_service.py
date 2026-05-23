from flask import Flask, jsonify, Blueprint, request
from db import get_connection
from datetime import datetime


# Función para iniciar sesión
def login_usuario(email, contraseña):

    con = get_connection()

    try:
        with con.cursor() as cursor:

            sql = """
                SELECT id, nombre, apellido, email, rol
                FROM usuarios
                WHERE email = %s AND contraseña = %s
            """

            cursor.execute(sql, (email, contraseña))

            usuario = cursor.fetchone()

            return usuario

    finally:
        con.close()