from flask import Flask
from db import mysql

from routes.admin_routes import admin_bp
from routes.menu_routes import menu_bp
from routes.reseñas_routes import reseñas_bp
from routes.reservas_routes import reservas_bp
from routes.usuarios_routes import usuarios_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Patata2026"
app.config["MYSQL_DB"] = "restaurante_db"

mysql.init_app(app)

app.register_blueprint(admin_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(reseñas_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
  app.run(port=5000, debug=True)
