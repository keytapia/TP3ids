from apscheduler.schedulers.background import BackgroundScheduler

from services.reservas import enviar_emails_resena_pendientes

def iniciar_scheduler():
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        func=enviar_emails_resena_pendientes,
        trigger="interval",
        minutes=1
    )

    scheduler.start()

    return scheduler