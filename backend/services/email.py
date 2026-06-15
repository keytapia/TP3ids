import os
import smtplib

from email.message import EmailMessage

from dotenv import load_dotenv

from services.configuracion import (
    obtener_configuracion
)


load_dotenv()


# Función para enviar un correo electrónico
def enviar_email_confirmacion(reserva, qr_buffer):

    datos_del_restaurante = obtener_configuracion()
    nombre_restaurante = datos_del_restaurante.get("nombre")
    ubicacion_restaurante = datos_del_restaurante.get("ubicacion")
    telefono_restaurante = datos_del_restaurante.get("telefono")

    try:
        email_host = os.getenv("EMAIL_HOST")
        email_port = os.getenv("EMAIL_PORT")
        email_user = os.getenv("EMAIL_USER")
        email_password = os.getenv("EMAIL_PASSWORD")

        if not all([
            email_host,
            email_port,
            email_user,
            email_password
        ]):
            return False


        mensaje = EmailMessage()

        mensaje["Subject"] = (f'Tu reserva en "{nombre_restaurante}" ha sido confirmada')
        mensaje["From"] = email_user
        mensaje["To"] = reserva["email"]

        url_cancelacion = f"http://127.0.0.1:8080/reservas/{reserva['id']}/cancelar"

        cuerpo = f"""
Hola {reserva["nombre"]} {reserva["apellido"]}, tu reserva está confirmada con los siguientes detalles:

Reserva N°: {reserva["id"]}
Fecha: {reserva["fecha"]}
Horario: {reserva["horario"]}
Cantidad de personas: {reserva["cantidad_personas"]}
Mesa: {reserva["mesa_id"]}
Notas adicionales: {reserva["notas_adicionales"]}

Adjuntamos tu QR para que puedas mostrarlo al llegar al restaurante y un link de cancelación.

{url_cancelacion}

Saludos,
{nombre_restaurante}
{ubicacion_restaurante}
{telefono_restaurante}
"""

        mensaje.set_content(cuerpo)

        qr_buffer.seek(0)

        mensaje.add_attachment(
            qr_buffer.read(),
            maintype="image",
            subtype="png",
            filename=f"reserva_{reserva['id']}_qr.png"
        )

        with smtplib.SMTP(
            email_host,
            int(email_port)
        ) as server:

            server.starttls()

            server.login(
                email_user,
                email_password
            )

            server.send_message(mensaje)

        return True

    except Exception as error:

        print(
            "Error al enviar email de confirmación:",
            error
        )

        return False
    
def enviar_email_cancelacion(reserva):

    datos_del_restaurante = obtener_configuracion()
    nombre_restaurante = datos_del_restaurante.get("nombre")
    ubicacion_restaurante = datos_del_restaurante.get("ubicacion")
    telefono_restaurante = datos_del_restaurante.get("telefono")

    try:
        email_host = os.getenv("EMAIL_HOST")
        email_port = os.getenv("EMAIL_PORT")
        email_user = os.getenv("EMAIL_USER")
        email_password = os.getenv("EMAIL_PASSWORD")

        if not all([
            email_host,
            email_port,
            email_user,
            email_password
        ]):
            return False


        mensaje = EmailMessage()

        mensaje["Subject"] = (f'Tu reserva en "{nombre_restaurante}" ha sido cancelada')
        mensaje["From"] = email_user
        mensaje["To"] = reserva["email"]

        cuerpo = f"""
Buen dia {reserva["nombre"]} {reserva["apellido"]},

Le informamos que su reserva fue cancelada, para consultar puede enviar un mensaje al número {telefono_restaurante}

Detalles de la reserva:
Reserva N°: {reserva["id"]}
Fecha: {reserva["fecha"]}
Horario: {reserva["horario"]}
Cantidad de personas: {reserva["cantidad_personas"]}
Mesa: {reserva["mesa_id"]}

Saludos,
{nombre_restaurante}
{ubicacion_restaurante}
{telefono_restaurante}
"""
        mensaje.set_content(cuerpo)

        with smtplib.SMTP(
            email_host,
            int(email_port)
        ) as server:

            server.starttls()

            server.login(
                email_user,
                email_password
            )

            server.send_message(mensaje)
        return True
    
    except Exception:
        return False
    

def enviar_email_pedir_resena(reserva):

    datos_del_restaurante = obtener_configuracion()
    nombre_restaurante = datos_del_restaurante.get("nombre")
    ubicacion_restaurante = datos_del_restaurante.get("ubicacion")
    telefono_restaurante = datos_del_restaurante.get("telefono")

    try:
        email_host = os.getenv("EMAIL_HOST")
        email_port = os.getenv("EMAIL_PORT")
        email_user = os.getenv("EMAIL_USER")
        email_password = os.getenv("EMAIL_PASSWORD")

        if not all([
            email_host,
            email_port,
            email_user,
            email_password
        ]):
            return False


        mensaje = EmailMessage()

        mensaje["Subject"] = (f'Contanos como fue tu experiencia en "{nombre_restaurante}".')
        mensaje["From"] = email_user
        mensaje["To"] = reserva["email"]

        url_resena = f"http://127.0.0.1:8080/resenas/crear/{reserva['id']}"

        cuerpo = f"""
Hola {reserva["nombre"]} {reserva["apellido"]}

Gracias por visitar {nombre_restaurante}!
Nos gustaria saber como fue tu experiencia.
Podes dejar tu reseña ingresando al siguiente link:

{url_resena}

Saludos,
{nombre_restaurante}
{ubicacion_restaurante}
{telefono_restaurante}
"""
        mensaje.set_content(cuerpo)

        with smtplib.SMTP(
            email_host,
            int(email_port)
        ) as server:

            server.starttls()

            server.login(
                email_user,
                email_password
            )

            server.send_message(mensaje)
        return True
    
    except Exception as error:
        print("Error al enviar email de reseña:", error)
        return False