from flask import Flask, request, jsonify, Blueprint

servicios_bp = Blueprint('servicios', __name__)

from services.servicios_service import (
	listar_servicios, 
	modificar_servicio, 
	crear_servicio, 
	eliminar_servicio
)


# Listar todos los servicios
@servicios_bp.route('/api/servicios', methods=['GET'])
def get_servicios():
    
    servicios = listar_servicios()
    
    return jsonify(servicios), 200