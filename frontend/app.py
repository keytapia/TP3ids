from flask import Flask

# Rutas Públicas
from routes.inicio import inicio_bp
from routes.menu import menu_bp
from routes.reservas import reservas_bp
from routes.resenas import resenas_bp
from routes.nosotros import nosotros_bp
from routes.contacto import contacto_bp

# Rutas del Administrador
from routes.login import login_bp
from routes.admin.dashboard import dashboard_bp

app = Flask(__name__)

# Blueprints para rutas públicas
app.register_blueprint(inicio_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(resenas_bp)
app.register_blueprint(nosotros_bp)
app.register_blueprint(contacto_bp)

# Blueprints para rutas del administrador
app.register_blueprint(login_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
  app.run(port=8080, debug=True)
