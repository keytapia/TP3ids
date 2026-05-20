from flask import Flask, request, jsonify, Blueprint

servicios_bp = Blueprint('servicios', __name__)

from backend.services import servicios_service

# Visualizar los servicios
@app.route('/api/servicios', methods=['GET'])
def get_servicios():
	servicios = servicios_service.listar_servicios()
	return jsonify(servicios)