from backend.db import obtener_conexion


def obtener_mesas_con_estado(fecha=None, horario=None, cantidad_personas=None):
    conexion = obtener_conexion()

    try:
        cursor = conexion.cursor(dictionary= True)
        cursor.execute("""
                SELECT 
                    id,
                    numero,
                    capacidad,
                    ubicacion,
                    estado
                FROM mesas
                ORDER BY numero ASC
            """)

        mesas = cursor.fetchall()

        mesas_reservadas = []

        if fecha and horario:
                cursor.execute("""
                    SELECT mesa_id
                    FROM reservas
                    WHERE fecha = %s
                    AND horario = %s
                    AND estado = 'confirmada'
                """, (fecha, horario))

                resultado = cursor.fetchall()
                mesas_reservadas = [fila["mesa_id"] for fila in resultado]

        for mesa in mesas:
                mesa["reservada"] = mesa["id"] in mesas_reservadas

                if cantidad_personas:
                    mesa["capacidad_suficiente"] = mesa["capacidad"] >= int(cantidad_personas)
                else:
                    mesa["capacidad_suficiente"] = True

                mesa["seleccionable"] = (
                    mesa["estado"] == "disponible"
                    and not mesa["reservada"]
                    and mesa["capacidad_suficiente"]
                )

        return mesas

    finally:
        conexion.close()