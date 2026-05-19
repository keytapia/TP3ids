from flask import Flask

from routes.admin_routes import admin_bp
from routes.menu_routes import menu_bp
from routes.reseñas_routes import reseñas_bp
from routes.reservas_routes import reservas_bp
from routes.usuarios_routes import usuarios_bp

app = Flask(__name__)

app.config.from_pyfile("config.py")

app.register_blueprint(admin_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(reseñas_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(usuarios_bp)


if __name__ == "__main__":
  app.run(port=5000, debug=True)
