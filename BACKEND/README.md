# Backend - Naza Restaurante

API RESTful desarrollada utilizando Flask.

## Tecnologías utilizadas

- Python
- Flask
- MySQL

## Responsabilidades

- Gestión de reservas
- Gestión de usuarios
- Generación de códigos QR
- Comunicación con la base de datos

## Estructura del directorio

- `routes/` → Define los endpoints de la API y recibe las solicitudes HTTP.
    - `__init__.py` → Inicializa el módulo de rutas
    - `admin_routes.py` → Funciones de Administrador
    - `dashboard_routes.py` → Estadísticas para el Administrador
    - `menu_routes.py` → Gestión y consulta de platos del menú
    - `reseñas_routes.py` → Creación y administración de reseñas
    - `reservas_routes.py` → Creación y gestión de reservas
    - `usuarios_routes.py` → Autenticación y gestión de usuarios

- `services/` → Contiene la lógica de negocio de la aplicación.
    - `__init__.py` → Inicializa el módulo de servicios
    - `auth_service.py` → Gestiona autenticación y validación de usuarios
    - `dashboard_service.py` → Procesa estadísticas e información del dashboard
    - `email_service.py` → Gestiona el envío de correos electrónicos
    - `qr_service.py` → Genera y administra códigos QR
    - `reservas_service.py` → Implementa la lógica relacionada con reservas

- `utils/` → Funciones y elementos auxiliares reutilizables.
    - `__init__.py` → Inicializa el módulo de utilidades
    - `constants.py` → Define constantes globales utilizadas en el sistema
    - `helpers.py` → Contiene funciones auxiliares reutilizables
    - `validators.py` → Realiza validaciones de datos y entradas

- `__init__.py` → Inicializa el paquete principal del backend.

- `app.py` → Programa principal.

- `config.py` → Define configuraciones generales del proyecto y variables de entorno.

- `database.sql` → Contiene la estructura y creación de la base de datos.

- `db.py` → Gestiona la conexión y comunicación con la base de datos MySQL.

- `requirements.txt` → Lista las dependencias y librerías necesarias para ejecutar el proyecto.

## Base de Datos

Se puede visualizar las tablas y su relación en el siguiente [link](https://dbdiagram.io/d/Naza_Restaurante_db-6a0cea2b9f1f8ec47b57c250)

## Puerto de ejecución

5000