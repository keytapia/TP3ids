from flask import Flask, jsonify, Blueprint, request
from db import get_connection
import re
from datetime import datetime


#Obtener todos los platos del menú 
def listar_menu():
    con = get_connection()

    try:
        with con.cursor() as cursor:
            cursor.excute("SELECT * FROM platos")
            menu = cursor.fetchall()
            return menu
    finally:
        con.close()


#Obtener un plato por id
def obtener_plato_id(plato_id):
    con = get_connection()

    try:
        with con.cursor() as cursor:

            cursor.excute("SELECT * FROM platos WHERE id = %s", (plato_id,))

            plato = cursor.fetchone()
            return plato
    finally:
        con.close()


#Obtener platos por categoria
def listar_menu_por_categoria(categoria):

    con = get_connection()

    try:
        with con.cursor() as cursor:
            query = """SELECT platos.*, categorias_platos.nombre AS categoria FROM platos 
                    JOIN categorias_platos ON platos.categoria_id = categorias_platos.id 
                    WHERE categorias_platos.nombre = %s"""
            cursor.execute(query,(categoria,))

            menu = cursor.fetchall()
            return menu
    finally:
        con.close()
        
def modificar_plato(id, data):
    con = get_connection()

    try:
        with con.cursor() as cursor:
            cursor.execute(
                """
                UPDATE platos
                SET categoria_id = %s,
                    nombre = %s,
                    descripcion = %s,
                    precio = %s,
                    imagen = %s,
                    disponible = %s
                WHERE id = %s
                """,
                (
                    data.get("categoria_id"),
                    data.get("nombre"),
                    data.get("descripcion"),
                    data.get("precio"),
                    data.get("imagen"),
                    data.get("disponible"),
                    id
                )
            )

            con.commit()

            return cursor.rowcount

    finally:
        con.close()


def eliminar_plato(id):
    con = get_connection()

    try:
        with con.cursor() as cursor:
            cursor.execute(
                "DELETE FROM platos WHERE id = %s",
                (id,)
            )

            con.commit()

            return cursor.rowcount

    finally:
        con.close()