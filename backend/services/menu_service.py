from db import obtener_conexion


# Obtener todos los platos del menú 
def listar_menu():
    con = obtener_conexion()

    try:
        with con.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM platos")
            menu = cursor.fetchall()
            return menu
    finally:
        con.close()

# Obtener un plato por id
def obtener_plato_id(plato_id):
    con = obtener_conexion()

    try:
        with con.cursor(dictionary=True) as cursor:

            cursor.execute("SELECT * FROM platos WHERE id = %s", (plato_id,))

            plato = cursor.fetchone()
            return plato
    finally:
        con.close()

# Obtener platos por categoria
def listar_menu_por_categoria(categoria):

    con = obtener_conexion()

    try:
        with con.cursor(dictionary=True) as cursor:
            query = """SELECT platos.*, categorias_platos.nombre AS categoria FROM platos 
                    JOIN categorias_platos ON platos.categoria_id = categorias_platos.id 
                    WHERE LOWER(categorias_platos.nombre) = %s"""
            cursor.execute(query,(categoria,))

            menu = cursor.fetchall()
            return menu
    finally:
        con.close()

# Modificar un plato 
def modificar_plato(id, data):
    con = obtener_conexion()

    try:
        with con.cursor(dictionary=True) as cursor:
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

# Eliminar un plato
def eliminar_plato(id):
    con = obtener_conexion()

    try:
        with con.cursor(dictionary=True) as cursor:
            cursor.execute(
                "DELETE FROM platos WHERE id = %s",
                (id,)
            )

            con.commit()

            return cursor.rowcount

    finally:
        con.close()

def listar_categorias():
    con = obtener_conexion()
    
    try: 
        with con.cursor(dictionary=True) as cursor:
            cursor.execute( """SELECT * FROM categorias_platos """)
            categorias = cursor.fetchall()
            return categorias
        
    finally: 
        con.close()

def crear_plato(categoria_id, nombre, precio, imagen,
                descripcion=None,
                restricciones_alimentarias=None,
                disponible=True):

    con = obtener_conexion()

    try:
        with con.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO platos (
                    categoria_id,
                    nombre,
                    descripcion,
                    precio,
                    restricciones_alimentarias,
                    imagen,
                    disponible
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    categoria_id,
                    nombre,
                    descripcion,
                    precio,
                    restricciones_alimentarias,
                    imagen,
                    disponible
                )
            )

            con.commit()
            return cursor.lastrowid

    finally:
        con.close()