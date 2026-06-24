from apscheduler.schedulers.background import BackgroundScheduler

from services.reservas import enviar_emails_resena_pendientes

def iniciar_scheduler():
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        func=enviar_emails_resena_pendientes,
        trigger="interval",
        minutes=30
    )

    scheduler.start()

    return scheduler
#aca le decimos al scheduler cada cuanto revisar solamente
#para cambiar el tiempo de envio, no es solo aca, tambien en repositories/resenas.py
#dentro de la funcion obtener_reservas_para_email_resena_db()
#en la linea 160 (15/6/2026)