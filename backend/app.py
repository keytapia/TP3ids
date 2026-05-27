from flask import Flask

# Rutas Públicas
from routes.admin_routes import admin_bp
from routes.menu_routes import menu_bp
# from routes.reseñas_routes import reseñas_bp    <--- FALTA IMPLEMENTAR
from routes.reservas_routes import reservas_bp
# from routes.usuarios_routes import usuarios_bp    <--- FALTA IMPLEMENTAR
from routes.servicios_routes import servicios_bp
from routes.auth_routes import auth_bp

# Rutas del Administrador
# from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)

# Blueprints para rutas públicas
app.register_blueprint(admin_bp)
app.register_blueprint(menu_bp)
# app.register_blueprint(reseñas_bp)   <--- FALTA IMPLEMENTAR
app.register_blueprint(reservas_bp)
# app.register_blueprint(usuarios_bp)  <--- FALTA IMPLEMENTAR
app.register_blueprint(servicios_bp)
app.register_blueprint(auth_bp)

# Blueprints para rutas del administrador
# app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(port=5000,debug=True)