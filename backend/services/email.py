import os
import smtplib

from email.message import EmailMessage

from dotenv import load_dotenv


load_dotenv()


# Función para enviar un correo electrónico
def enviar_email_confirmacion(reserva, qr_buffer):

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

        mensaje["Subject"] = 'Tu reserva en "NAZA Restaurante" ha sido confirmada'
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

Adjuntamos tu QR para que puedas mostrarlo al llegar al restaurante y un boton de cancelacion.

{url_cancelacion}

Saludos,
NAZA Restaurante
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

        mensaje["Subject"] = 'Tu reserva en "NAZA Restaurante" ha sido cancelada'
        mensaje["From"] = email_user
        mensaje["To"] = reserva["email"]

        cuerpo = f"""
Buen dia {reserva["nombre"]} {reserva["apellido"]},

Le informamos que su reserva fue cancelada, para consultar puede enviar un mensaje al numero de contacto de nuestra pagina

Detalles de la reserva:
Reserva N°: {reserva["id"]}
Fecha: {reserva["fecha"]}
Horario: {reserva["horario"]}
Cantidad de personas: {reserva["cantidad_personas"]}
Mesa: {reserva["mesa_id"]}

Saludos,
NAZA Restaurante
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

        mensaje["Subject"] = 'Contanos como fue tu experiencia en "NAZA Restaurante".'
        mensaje["From"] = email_user
        mensaje["To"] = reserva["email"]

        url_resena = f"http://127.0.0.1:8080/resenas/crear/{resena['id']}"

        cuerpo = f"""
Hola {reserva["nombre"]} {reserva["apellido"]}

Gracias por visitar NAZA Restaurante!
Nos gustaria saber como fue tu experiencia.
Podes dejar tu reseña ingresando al siguiente link:

{url_resena}

Saludos,
NAZA Restaurante
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