from repositories.dashboard import (
    obtener_resumen_dashboard_db,
    obtener_proximas_reservas_db,
    obtener_cancelaciones_hoy_db,
    obtener_ultimas_reseñas_db
)


def obtener_resumen_dashboard():

    return obtener_resumen_dashboard_db()


def obtener_proximas_reservas():

    return obtener_proximas_reservas_db()


def obtener_cancelaciones_hoy():

    return obtener_cancelaciones_hoy_db()


def obtener_ultimas_reseñas():

    return obtener_ultimas_reseñas_db()