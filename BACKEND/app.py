from flask import Flask

from routes.menu_routes import menu_bp
from routes.reservas_routes import reservas_bp

app = Flask(__name__)

app.config.from_pyfile("config.py")

app.register_blueprint(admin_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(reseñas_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(usuarios_bp)

@app.route("/")
def prueba():
    return "todo ok"

if __name__ == "__main__":
  app.run(port=5000, debug=True)
