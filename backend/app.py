import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from utils.constants import (
    APP_PUERTO,
    MODO_DEBUG
)


# Rutas públicas
from routes.public.auth import auth_bp
from routes.public.menu import menu_bp
from TP3ids.backend.routes.public.resenas import resenas_bp
from routes.public.reservas import reservas_bp
from routes.public.servicios import servicios_bp
from routes.public.usuarios import usuarios_bp

# Rutas administrador
from routes.admin.dashboard import dashboard_admin_bp
from routes.admin.estadisticas import estadisticas_admin_bp
from routes.admin.menu import menu_admin_bp
from routes.admin.resenas import resenas_admin_bp
from routes.admin.reservas import reservas_admin_bp
from routes.admin.servicios import servicios_admin_bp


load_dotenv()


def create_app():

    app = Flask(__name__)

    CORS(app)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Públicas
    app.register_blueprint(auth_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(reservas_bp)
    app.register_blueprint(servicios_bp)
    app.register_blueprint(resenas_bp)
    app.register_blueprint(usuarios_bp)

    # Administrador
    app.register_blueprint(dashboard_admin_bp)
    app.register_blueprint(estadisticas_admin_bp)
    app.register_blueprint(menu_admin_bp)
    app.register_blueprint(resenas_admin_bp)
    app.register_blueprint(reservas_admin_bp)
    app.register_blueprint(servicios_admin_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(port=APP_PUERTO, debug=MODO_DEBUG)