from flask import Flask
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

# Rutas Públicas
from routes.public.contacto import contacto_bp
from routes.public.inicio import inicio_bp
from routes.public.login import login_bp
from routes.public.menu import menu_bp
from routes.public.nosotros import nosotros_bp
from routes.public.reseñas import reseñas_bp
from routes.public.reservas import reservas_bp

# Rutas del Administrador
from routes.admin.dashboard import dashboard_admin_bp
from routes.admin.estadisticas import estadisticas_admin_bp
from routes.admin.menu import menu_admin_bp
from routes.admin.reseñas import reseñas_admin_bp
from routes.admin.reservas import reservas_admin_bp
from routes.admin.servicios import servicios_admin_bp
from routes.admin.configuracion import configuracion_admin_bp


app = Flask(__name__)
app.secret_key = "Nazarestaurante"

# Blueprints para rutas públicas
app.register_blueprint(inicio_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(reseñas_bp)
app.register_blueprint(nosotros_bp)
app.register_blueprint(contacto_bp)
app.register_blueprint(login_bp)

# Blueprints para rutas del administrador
app.register_blueprint(dashboard_admin_bp)
app.register_blueprint(reservas_admin_bp)
app.register_blueprint(menu_admin_bp)
app.register_blueprint(reseñas_admin_bp)
app.register_blueprint(servicios_admin_bp)
app.register_blueprint(estadisticas_admin_bp)
app.register_blueprint(configuracion_admin_bp)


if __name__ == "__main__":
  app.run(port=8080, debug=True)
