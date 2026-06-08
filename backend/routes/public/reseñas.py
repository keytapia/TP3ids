from flask import request, jsonify, Blueprint

reseñas_bp = Blueprint('reseñas', __name__, url_prefix='/api')
