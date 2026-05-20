from flask import Blueprint

from services.dashboard_service import (
    obtener_estadisticas_generales, 
    obtener_historial_reservas, 
    obtener_usuarios_cancelaciones, 
    obtener_platos_populares, 
    obtener_horarios_populares
)

dashboard_bp = Blueprint('dashboard', __name__)

# Estadísticas Generales (cantidad de reservas, usuarios totales, reseñas totales)
@dashboard_bp.route('/api/admin/dashboard', methods=['GET'])
def estadisticas_generales():
    return obtener_estadisticas_generales()

# Historial de reservas
@dashboard_bp.route('/api/admin/dashboard/historial-reservas', methods=['GET'])
def historial_reservas():
    return obtener_historial_reservas()

# Usuarios con cancelaciones
@dashboard_bp.route('/api/admin/dashboard/usuarios-cancelaciones', methods=['GET'])
def usuarios_cancelaciones():
    return obtener_usuarios_cancelaciones()

# Platos mas populares
@dashboard_bp.route('/api/admin/dashboard/platos-populares', methods=['GET'])
def platos_populares():
    return obtener_platos_populares()

# Horarios mas solicitados
@dashboard_bp.route('/api/admin/dashboard/horarios-populares', methods=['GET'])
def horarios_populares():
    return obtener_horarios_populares()

