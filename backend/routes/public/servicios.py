from flask import Flask, request, jsonify, Blueprint

servicios_bp = Blueprint('servicios', __name__, url_prefix='/api')

from services.servicios import (
	listar_servicios
)

# Listar todos los servicios
@servicios_bp.route('/servicios', methods=['GET'])
def get_servicios():
    
    servicios = listar_servicios()
    
    return jsonify(servicios), 200