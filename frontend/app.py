from flask import Flask
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

# Rutas Públicas
from routes.inicio import inicio_bp
from routes.menu import menu_bp
from routes.reservas import reservas_bp
from routes.resenas import resenas_bp
from routes.nosotros import nosotros_bp
from routes.contacto import contacto_bp
from routes.login import login_bp

# Rutas del Administrador


from routes.admin.dashboard import dashboard_bp
from routes.admin.reservas import admin_reservas_bp
from routes.admin.menu import admin_menu_bp
from routes.admin.resenas import admin_resenas_bp
from routes.admin.servicios import servicios_bp
from routes.admin.estadisticas import estadisticas_bp
from routes.admin.configuracion import configuracion_bp


app = Flask(__name__)

# Blueprints para rutas públicas
app.register_blueprint(inicio_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(resenas_bp)
app.register_blueprint(nosotros_bp)
app.register_blueprint(contacto_bp)
app.register_blueprint(login_bp)

# Blueprints para rutas del administrador

app.register_blueprint(dashboard_bp)
app.register_blueprint(admin_reservas_bp)
app.register_blueprint(admin_menu_bp)
app.register_blueprint(admin_resenas_bp)
app.register_blueprint(servicios_bp)
app.register_blueprint(estadisticas_bp)
app.register_blueprint(configuracion_bp)


if __name__ == "__main__":
  app.run(port=8080, debug=True)
