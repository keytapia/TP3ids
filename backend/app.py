import os

from flask import Flask
from flask_cors import CORS

from dotenv import (
    load_dotenv
)

# Rutas Públicas
from routes.menu_routes import menu_bp
from routes.reservas_routes import reservas_bp
from routes.servicios_routes import servicios_bp
from routes.auth_routes import auth_bp
# from routes.reseñas_routes import reseñas_bp    <--- FALTA IMPLEMENTAR
# from routes.usuarios_routes import usuarios_bp    <--- FALTA IMPLEMENTAR

# Rutas del Administrador
from routes.admin_routes import admin_bp



# ---------- APP PRINCIPAL ----------

# Carga las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") # La clave que vamos a usar para mantener la sesión del usuario

# Blueprints para rutas públicas
app.register_blueprint(menu_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(servicios_bp)
app.register_blueprint(auth_bp)
# app.register_blueprint(reseñas_bp)   <--- FALTA IMPLEMENTAR
# app.register_blueprint(usuarios_bp)  <--- FALTA IMPLEMENTAR

# Blueprints para rutas del administrador
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)