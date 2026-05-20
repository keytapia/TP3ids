import mysql.connector

from config import (
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DB
)

# Esta función crea y devuelve una conexión a la base de datos MySQL
def obtener_conexion():
    conexion = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

    return conexion