import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
load_dotenv()

# Función para enviar un correo electrónico
def enviar_email_confirmacion(reserva, qr_buffer):
    try:
        email_host = os.getenv("EMAIL_HOST")
        email_port = int(os.getenv("EMAIL_PORT"))
        email_user = os.getenv("EMAIL_USER")
        email_password = os.getenv("EMAIL_PASSWORD")

        if not email_host or not email_port or not email_user or not email_password:
            return False
        
        email_port = int(email_port)

        msg = EmailMessage()
        msg['Subject'] = 'Tu resserva en "NAZA" ha sido confirmada'
        msg['From'] = email_user
        msg['To'] = reserva["email"]

        cuerpo = f"""Hola {reserva["nombre"]}, tu reserva esta confirmada con los siguientes detalles:
        Reserva N°: {reserva["id"]},
        Fecha: {reserva["fecha"]},
        Horario: {reserva["horario"]},
        Cantidad de personas: {reserva["cantidad_personas"]},
        Mesa: {reserva["mesa_id"]},
        Notas adicionales: {reserva["notas_adicionales"]}

        Adjuntamos su QR para que pueda mostrarlo al llegar al restaurante.
        Saludos, NAZA Restaurante
        """
        msg.set_content(cuerpo)

        qr_buffer.seek(0)

        msg.add_attachment(
            qr_buffer.read(),
            maintype='image',
            subtype='png',
            filename=f"reserva_{reserva['id']}_qr.png"
        )
        with smtplib.SMTP(email_host, email_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.send_message(msg)
        return True
    except Exception as error:
        print("Error al enviar email de confirmación", error)
        return False