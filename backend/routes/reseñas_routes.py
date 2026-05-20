from flask import Flask, request, jsonify, Blueprint
from datetime import datetime



reseñas_bp = Blueprint('reseñas', __name__)