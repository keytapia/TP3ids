from db import obtener_conexion
import os
from io import BytesIO
import qrcode

# Función para crear el QR de una reserva

def crear_qr_reserva(reserva):
    qr_data = (
        f"Reserva N°: {reserva['id']}\n" +
        f"Cliente: {reserva['nombre']} {reserva['apellido']}\n" +
        f"Fecha: {reserva['fecha']}\n" +
        f"Horario: {reserva['horario']}\n" +
        f"Cantidad de personas: {reserva['cantidad_personas']}\n" +
        f"Mesa: {reserva['mesa_id']}\n" +
        f"Notas adicionales: {reserva['notas_adicionales']}"
    )

    qr = qrcode.make(qr_data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer