from flask import Flask, render_template, Blueprint

dashboard_bp = Blueprint('dashboard', __name__)

# Dashboard
@dashboard_bp.route("/admin/dashboard")
def dashboard():
    mis_estadisticas = {
        "reservas_hoy": 35,
        "comensales_total": 89,
        "cancelaciones_hoy": 7,
        "calificacion_promedio": 5.0
    }

    mis_reservas_proximas = [
        {"horario": "20:00", "fecha": "15/06/2026", "nombre": "Juan", "apellido": "Perez", "cantidad_personas": 4},
        {"horario": "21:00", "fecha": "15/06/2026", "nombre": "Brenda", "apellido": "Lopez", "cantidad_personas": 2},
        {"horario": "21:30", "fecha": "15/06/2026", "nombre": "Pedro", "apellido": "Garcia", "cantidad_personas": 6}
    ]

    mis_cancelaciones = [
        {"horario": "20:00", "fecha": "14/06/2026", "nombre": "Maria", "apellido": "Diaz", "cantidad_personas": 3},
        {"horario": "20:00", "fecha": "14/06/2026", "nombre": "Maria", "apellido": "Diaz", "cantidad_personas": 3},
    ]

    mis_resenas = [
        {"nombre": "Juan", "estrellas": 5, "comentario": "Excelente atención"},
        {"nombre": "Brenda", "estrellas": 4, "comentario": "Muy rica la comida"},
        {"nombre": "Pedro", "estrellas": 1, "comentario": "El lugar es horrible"},
    ]

    return render_template("admin/dashboard.html", stats=mis_estadisticas, reservas_proximas=mis_reservas_proximas, ultimas_resenas=mis_resenas, ultimas_cancelaciones=mis_cancelaciones)