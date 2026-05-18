from flask import Flask, request, jsonify, Blueprint
from datetime import datetime


usuarios_bp = Blueprint('usuarios', __name__)