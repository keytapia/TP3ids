from db import obtener_conexion

def obtener_resenas_db():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                resenas.id,
                resenas.reserva_id,
                resenas.comentario,
                resenas.puntuacion,
                resenas.fecha_publicacion,
                usuarios.nombre,
                usuarios.apellido
            FROM resenas
            INNER JOIN usuarios
                ON resenas.usuario_id = usuarios.id
            ORDER BY resenas.fecha_publicacion DESC
        """)

        return cursor.fetchall()
    
    finally:
        cursor.close()
        conexion.close()


def obtener_resena_por_id_db(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                resenas.id,
                resenas.reserva_id,
                resenas.comentario,
                resenas.puntuacion,
                resenas.fecha_publicacion,
                usuarios.nombre,
                usuarios.apellido
            FROM resenas
            INNER JOIN usuarios
                ON resenas.usuario_id = usuarios.id
            WHERE resenas.id = %s
        """, (id,))

        return cursor.fetchone()
    
    finally:
        cursor.close()
        conexion.close()


def obtener_resena_por_reserva_db(reserva_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT *
            FROM resenas
            WHERE reserva_id = %s
        """, (reserva_id,))

        return cursor.fetchall()
    
    finally:
        cursor.close()
        conexion.close()


def obtener_reserva_para_resena_db(reserva_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                reservas.id AS reserva_id,
                reservas.usuario_id,
                reservas.estado,
                usuarios.nombre,
                usuarios.apellido,
                usuarios.email
            FROM reservas
            INNER JOIN usuarios
                ON reservas.usuario_id = usuarios.id
            WHERE reservas.id = %s
        """, (reserva_id,))

        return cursor.fetchone()
    
    finally:
        cursor.close()
        conexion.close()


def crear_resena_db(usuario_id, reserva_id, comentario, puntuacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute("""
            INSERT INTO resenas (
                usuario_id,
                reserva_id,
                comentario,
                puntuacion
            )
            VALUES (%s, %s, %s, %s)
        """, (
            usuario_id,
            reserva_id,
            comentario,
            puntuacion
        ))

        conexion.commit()

        return {
            "id": cursor.lastrowid
        }
    
    except Exception:
        conexion.rollback()
        raise

    finally:
        cursor.close()
        conexion.close()


def obtener_reservas_para_email_resena_db():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                reservas.id,
                reservas.usuario_id,
                reservas.mesa_id,
                reservas.fecha,
                reservas.horario,
                reservas.cantidad_personas,
                reservas.notas_adicionales,
                reservas.estado,
                usuarios.nombre,
                usuarios.apellido,
                usuarios.email,
                usuarios.telefono
            FROM reservas
            INNER JOIN usuarios
                ON reservas.usuario_id = usuarios.id
            WHERE reservas.estado = 'finalizada'
            AND reservas.email_resena_enviado = FALSE
            AND TIMESTAMP(reservas.fecha, reservas.horario) + INTERVAL 1 MINUTE <= NOW()
            AND reservas.id NOT IN (
                SELECT reserva_id
                FROM resenas
            )
        """)

        return cursor.fetchall()
    
    finally:
        cursor.close()
        conexion.close()

def marcar_email_resena_enviado_db(reserva_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        cursor.execute("""
            UPDATE reservas
            SET email_resena_enviado = TRUE
            WHERE id = %s
        """, (reserva_id,))

        conexion.commit()

        return cursor.rowcount > 0
    
    except Exception:
        conexion.rollback()
        raise
    
    finally:
        cursor.close()
        conexion.close()