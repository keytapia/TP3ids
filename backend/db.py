import os
import mysql.connector

from dotenv import (
    load_dotenv
)


# Función que carga las variables de entorno desde el archivo .env
load_dotenv()

# Creamos variables asignando los valores de las variables de entorno cargadas
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

# Esta función crea y devuelve una conexión a MySQL
def obtener_conexion():

    conexion = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

    return conexion