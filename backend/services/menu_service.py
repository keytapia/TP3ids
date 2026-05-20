from flask import Flask, jsonify, Blueprint, request
from db import get_connection
import re
from datetime import datetime


#Obtener todos los platos del menú 
def listar_menu():
    con = get_connection()

    try:
        with con.cursor() as cursor:
            query= "SELECT * FROM platos"
            cursor.excute(query)
            menu = cursor.fetchall()
            return menu
    finally:
        con.close()


#Obtener un plato por id
def obtener_plato_id(id):
    con = get_connection()

    try:
        with con.cursor() as cursor:

            query = "SELECT * FROM platos WHERE id = %s"
            cursor.excute(query, (id,))

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
        