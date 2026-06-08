import os
import mysql.connector

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENV_PATH = os.path.join(BASE_DIR, ".env")

# override=True fuerza a usar lo que dice el .env actual
load_dotenv(ENV_PATH, override=True)

# Creamos variables asignando los valores de las variables de entorno cargadas
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_PORT = os.getenv("MYSQL_PORT", 3306)

# Esta función crea y devuelve una conexión a MySQL
def obtener_conexion():

    conexion = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        port=int(MYSQL_PORT)
    )

    return conexion