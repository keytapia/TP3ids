from repositories.estadisticas import (
    obtener_reservas_totales_db,
    obtener_cancelaciones_mes_db,
    obtener_reservas_por_horario_db,
    obtener_reservas_por_dia_db
)


def obtener_estadisticas():

    reservas_totales = obtener_reservas_totales_db()
    cancelaciones_mes = obtener_cancelaciones_mes_db()

    return {
        "reservas_totales": reservas_totales["reservas_totales"],
        "cancelaciones_mes": cancelaciones_mes["cancelaciones_mes"],
        "reservas_por_horario": obtener_reservas_por_horario_db(),
        "reservas_por_dia": obtener_reservas_por_dia_db()
    }