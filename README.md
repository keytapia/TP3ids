# Introducción al Desarrollo de Software - FIUBA | Proyecto Final Integrador 2026C1

> El presente proyecto de la materia Introducción al Desarrollo de Software de la Facultad de Ingeniería de la Universidad de Buenos Aires integra todos los temas aprendidos. El desarrollo del mismo contempla Backend, Frontend, Base de datos MySQL, y se encuentra versionado en este repositorio de GitHub. Se aplican buenas prácticas de programación y se utilizan metodologías ágiles para su resolución.

## Grupo N° 17 - "Naza"
### Integrantes

| **Padrón** | **Apellido**     | **Nombre**           |
|------------|------------------|----------------------|
| 115658     | KERSUL           | Celeste Briza        |
| 114292     | LICHINIZER       | Valeria Dana         |
| 115563     | MARTIN           | Miguel               |
| 112615     | NAYA NICOLAS     | Camila Rocío         |
| 115403     | NOVILLO          | Marilyn Jessenia     |
| 106820     | SCALISE          | Federico Nahuel      |
| 115130     | TAPIA            | Keyla                |


# Sitio web gastronómico con reserva

## **Naza - Restaurante**

"Naza" es una aplicación web gastronómica orientada a la gestión de reservas online para su restaurante.

El sistema permitirá a los usuarios visualizar información del establecimiento, consultar el menú, realizar reservas y recibir confirmaciones mediante correo electrónico y códigos QR.

Además, contará con un panel administrativo para la gestión de reservas, menú, reseñas, servicios y estadísticas.

### **Arquitectura**

El proyecto se encuentra dividido en dos aplicaciones principales:

- **Backend**: API RESTful desarrollada utilizando Flask, encargada de la lógica de negocio, autenticación, gestión de reservas, generación de códigos QR, envío de correo electrónico y comunicación con la base de datos MySQL.

- **Frontend**: Aplicación desarrollada utilizando Flask y motor de plantillas Jinja, encargada de la interfaz visual del sistema y la interacción con la API backend.

Ambas aplicaciones se ejecutarán de forma independiente en distintos puertos y se comunicarán mediante solicitudes HTTP respetando una arquitectura RESTful.

La persistencia de datos se realizará utilizando una base de datos MySQL.

**Flujo general del sistema:**
```
          ┌───────────────────────────┐
          │      Frontend Flask       │
          │  HTML + CSS + JS + Jinja2 │
          │      (Puerto 8080)        │
          └─────────────┬─────────────┘
                        │
                        │ HTTP (JSON)
                        ▼
          ┌───────────────────────────┐
          │       Backend Flask       │
          │        API RESTful        │
          │      (Puerto 5000)        │
          └─────────────┬─────────────┘
                        │
                ┌───────┴────────┐
                │                │
                ▼                ▼
          ┌──────────────┐  ┌─────────────────┐
          │    MySQL     │  │ Servicios Extra │
          │ (Puerto 3306)│  │  QR + Emails    │
          └──────────────┘  └─────────────────┘
```

### **Estructura del Repositorio**

- `frontend/` → Aplicación frontend desarrollada con Flask y Jinja.
- `backend/`  → API RESTful, lógica de negocio y conexión con MySQL.
- `docs/`     → Documentación, backlog y mockup del proyecto.

#### **Estructura del Frontend**

```
frontend/
├── routes/                             # Rutas Flask que renderizan los templates
│   ├── admin/                              # Rutas del panel de administración
│   │   ├── dashboard.py                        # Dashboard principal del administrador
│   │   ├── estadisticas.py                     # Vista de estadísticas y métricas
│   │   ├── menu.py                             # Gestión visual del menú
│   │   ├── reseñas.py                          # Gestión visual de reseñas
│   │   ├── reservas.py                         # Gestión visual de reservas
│   │   └── servicios.py                        # Gestión visual de servicios
│   └── public/                             # Rutas públicas del sitio web
│       ├── contacto.py                         # Página de contacto
│       ├── inicio.py                           # Página principal (Home)
│       ├── login.py                            # Inicio de sesión de administrador
│       ├── menu.py                             # Menú del restaurante
│       ├── nosotros.py                         # Información institucional
│       ├── reseñas.py                          # Visualización de reseñas
│       └── reservas.py                         # Proceso de reservas online
├── services/                           # Comunicación con la API Backend
│   ├── dashboard.py                        # Consumo de endpoints del dashboard
│   ├── estadisticas.py                     # Consumo de endpoints de estadísticas
│   ├── login.py                            # Consumo de endpoints de autenticación
│   ├── menu.py                             # Consumo de endpoints del menú
│   └── reservas.py                         # Consumo de endpoints de reservas
├── static/                             # Archivos estáticos
│   ├── images/                             # Imágenes utilizadas por la aplicación
│   │   ├── favicon.ico                         # Ícono del sitio web
│   │   └── ...                                 # Imágenes de platos, banners, etc.
│   ├── scripts/                            # Scripts JavaScript
│   │   ├── estadisticas.js                     # Gráficos y métricas del administrador
│   │   └── script.js                           # Funcionalidades generales del sitio
│   └── styles/                             # Hojas de estilo CSS
│       ├── admin.css                           # Estilos del panel administrador
│       └── public.css                          # Estilos del sitio público
├── templates/                          # Plantillas HTML renderizadas por Flask
│   ├── admin/                              # Templates del administrador
│   │   ├── base.html                           # Layout base del administrador
│   │   ├── dashboard.html                      # Dashboard principal
│   │   ├── estadisticas.html                   # Vista de estadísticas
│   │   ├── menu.html                           # Gestión del menú
│   │   ├── reseñas.html                        # Gestión de reseñas
│   │   ├── reservas.html                       # Gestión de reservas
│   │   └── servicios.html                      # Gestión de servicios
│   └── public/                             # Templates públicos
│       ├── base.html                           # Layout base público
│       ├── contacto.html                       # Página de contacto
│       ├── error.html                          # Página de error
│       ├── index.html                          # Página principal
│       ├── login_exitoso.html                  # Confirmación de login exitoso
│       ├── login.html                          # Formulario de login
│       ├── menu.html                           # Menú del restaurante
│       ├── nosotros.html                       # Página institucional
│       ├── reseñas.html                        # Página de reseñas
│       └── reservas.html                       # Página de reservas
├── app.py                              # Punto de entrada de la aplicación Flask
├── requirements.txt                    # Dependencias del proyecto
└── setup_virtualenv.sh                 # Script de instalación y configuración
```

#### **Estructura del Backend**

```
backend/
├── database/                      # Scripts SQL de creación e inicialización de la base de datos
│   └── restaurante_db.sql            # Estructura y datos iniciales de la base de datos
├── repositories/                  # Acceso a datos y consultas SQL
│   ├── auth.py                       # Queries relacionadas con autenticación
│   ├── dashboard.py                  # Queries para estadísticas y dashboard
│   ├── menu.py                       # Queries de platos y categorías
│   ├── reservas.py                   # Queries de reservas y mesas
│   ├── servicios.py                  # Queries de servicios ofrecidos
│   └── usuarios.py                   # Queries de usuarios
├── routes/                        # Endpoints y blueprints de la API
│   ├── admin/                        # Rutas exclusivas para administradores
│   │   ├── dashboard.py                  # Endpoints del dashboard administrativo
│   │   ├── estadisticas.py               # Endpoints de estadísticas
│   │   ├── menu.py                       # Gestión administrativa del menú
│   │   ├── reseñas.py                    # Gestión administrativa de reseñas
│   │   ├── reservas.py                   # Gestión administrativa de reservas
│   │   └── servicios.py                  # Gestión administrativa de servicios
│   └── public/                       # Rutas accesibles para clientes y público general
│       ├── auth.py                       # Inicio de sesión y autenticación
│       ├── menu.py                       # Consulta del menú
│       ├── reseñas.py                    # Consulta y creación de reseñas
│       ├── reservas.py                   # Creación y consulta de reservas
│       ├── servicios.py                  # Consulta de servicios del restaurante
│       └── usuarios.py                   # Operaciones relacionadas con usuarios
├── services/                      # Lógica de negocio de la aplicación
│   ├── auth.py                       # Procesamiento de autenticación
│   ├── dashboard.py                  # Procesamiento de estadísticas
│   ├── email.py                      # Envío de correos electrónicos
│   ├── menu.py                       # Lógica de gestión del menú
│   ├── qr.py                         # Generación de códigos QR
│   ├── reservas.py                   # Lógica de reservas y disponibilidad
│   ├── servicios.py                  # Lógica de gestión de servicios
│   └── usuarios.py                   # Lógica de gestión de usuarios
├── utils/                         # Utilidades y componentes auxiliares
│   ├── constants.py                  # Constantes globales de la aplicación
│   └── validators.py                 # Validaciones y reglas de negocio reutilizables
├── app.py                         # Punto de entrada principal de la aplicación Flask (puerto 5000)
├── db.py                          # Configuración y conexión a MySQL
├── requirements.txt               # Dependencias de Python del proyecto
└── setup_virtualenv.sh            # Script de instalación y configuración automática
```

### **Requisitos Previos**

- Python 3.10+

### **Configuración y Ejecución del Proyecto**

#### 1. Variables de entorno

Debe crear dentro de `TP3ids/backend` un archivo `.env`

```bash
cd TP3ids/backend
touch .env
```

y dentro del mismo debe copiar el siguiente código:

```
SECRET_KEY=Nazarestaurante

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=<SU CONTRASEÑA MYSQL>
MYSQL_DB=restaurante_db

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=<SU CORREO PERSONAL, NO LABORAL NI ESTUDIANTIL>
EMAIL_PASSWORD=rzvvkjjmuziisnzc<SU LLAVE DE ACCESO DE GMAIL>
```

Donde deberá reemplazar los siguientes campos:
- `<SU CONTRASEÑA MYSQL>` por su contraseña de su usario `root` de su servicio MySQL
- `<SU CORREO PERSONAL, NO LABORAL NI ESTUDIANTIL>` por su correo @gmail.com
- `<SU LLAVE DE ACCESO DE GMAIL>` por su llave de acceso de Google

>En caso de no saber o no tener llave de acceso de Gmail, active la verificacion en dos pasos desde la configuracion de su cuenta y luego entre al siguiente enlace, escriba Gmail en donde le pregunta por la aplicacion y escriba lo que obtenga sin espacios
>```https://myaccount.google.com/u/4/apppasswords?utm_source=chatgpt.com&rapt=AEjHL4OIl5GX21sg-iEXmBPEUtWimHjYyALdWBbgY-zE3XC0gnP1rAuUN1MLejo01RvpfKoElAh69YVKOB2sDo0Iij8HeAl97gp5Jc4ihXZ0aIVyfx7z3g8```

#### 2. Instalación y Ejecución

El proyecto incluye scripts de setup para el backend y para el frontend. Los mismos ejecutan todo lo necesario para crear y levantar cada aplicación.

- **Para la aplicación Backend**

>El script crea la base de datos MySQL, carga las tablas con información inicial, crea el entorno virtual usando virtualenv, instala las dependencias usadas en el proyecto, y levanta la aplicación en el puerto 5000.

Dentro del directorio `TP3ids/backend`, ejecutar el script `setup_virtualenv.sh`

```bash
# Linux
chmod +x setup_virtualenv.sh
./setup_virtualenv.sh
```

Durante el proceso le pedirá su clave de administrador de usuario para la instalación (sudo), y luego una vez instalado MySQL, le pedirá para ingresar, la contraseña para el usuario root (si definió una).

Una vez finalizado el proceso, la API se iniciará y estará disponible en `http://localhost:5000/`

- **Para la aplicación Frontend**

>El script crea el entorno virtual usando virtualenv, instala las dependencias usadas en el proyecto, y levanta la aplicación en el puerto 8080.

Dentro del directorio `TP3ids/frontend`, ejecutar el script `setup_virtualenv.sh`

```bash
# Linux
chmod +x setup_virtualenv.sh
./setup_virtualenv.sh
```

Durante el proceso le pedirá su clave de administrador de usuario para la instalación (sudo).

Una vez finalizado el proceso, la API se iniciará y estará disponible en `http://localhost:8080/`

### Endpoints

Los endpoints estan divididos en `admin` y `public`

- `admin`

Se encuentran bajo el prefijo `/api/admin`. Las respuestas son JSON.
 
| Metodo | Endpoint                                | Descripcion                                                                      |
|--------|-----------------------------------------|----------------------------------------------------------------------------------|
| GET    | `/dashboard`                            | Dashboard General (resumen, próximas reservas, cancelaciones de hoy, reseñas)    |
| GET    | `/estadisticas`                         | Obtener estadísticas                                                             |
| GET    | `/menu`                                 | Listar el menú completo                                                          |
| POST   | `/menu`                                 | Crear un plato del menú                                                          |
| PUT    | `/menu/<int:id>`                        | Modificar un plato del menú                                                      |
| DELETE | `/menu/<int:id>`                        | Modificar un plato del menú                                                      |
| GET    | `/reseñas`                              | Obtener todas las reseñas                                                        |
| DELETE | `/reseñas/<int:id>`                     | Eliminar una reseña por id                                                       |
| GET    | `/reservas`                             | Visualizar las reservas                                                          |
| GET    | `/reservas/estado/<estado>`             | Visualizar el estado de las reservas (filtra por estado)                         |
| GET    | `/reservas/cancelar/<int:reserva_id>`   | Cancelar una reserva por id cambiando su estado a "cancelada"                    |
| GET    | `/servicios`                            | Listar todos los servicios                                                       |
| POST   | `/servicios`                            | Crear un servicio                                                                |
| PUT    | `/servicios/<int:id>`                   | Modificar un servicio                                                            |
| DELETE | `/servicios/<int:id>`                   | Eliminar un servicio                                                             |

- `public`

Se encuentran bajo el prefijo `/api`. Las respuestas son JSON.

| Metodo | Endpoint                                | Descripcion                                                                      |
|--------|-----------------------------------------|----------------------------------------------------------------------------------|
| POST   | `/auth/login`                           | Login para el administrador                                                      |
| GET    | `/menu`                                 | Filtrar menu completo o por categoria                                            |
| GET    | `/menu/<int:plato_id`                   | Filtrar un plato especifico por numero id                                        |
| GET    | `/categorias`                           | Listar categorias disponibles                                                    |
| PATCH  | `/reservas/<int:id>/cancelar-cliente`   | Cancelar reserva                                                                 |
| GET    | `/mesas-disponibles`                    | Obtener mesas por estado                                                         |
| GET    | `/disponibilidad`                       | Ver disponibilidad general                                                       |
| POST   | `/reservas`                             | Crear reserva para un cliente                                                    |
| GET    | `/servicios`                            | Listar todos los servicios                                                       |


### Páginas

Las páginas web estan divididas en `admin` para el uso de adminitrador y `public` para la vista de los clientes y público en general.

- `admin`

Se encuentran bajo el prefijo `/admin`

| Ruta            | Descripcion                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| `/dashboard`    | Visualización de un dashboard con cantidad de reservas, usuarios totales, reseñas totales                          |
| `/estadisticas` | Gráficos de reservas por horario y reservas por día                                                                |
| `/menu`         | Menu completo con categorias y platos                                                                              |
| `/reseñas`      | Vista de las reseñas de los clientes                                                                               |
| `/reservas`     | Reservas totales con detalle del cliente                                                                           |
| `/servicios`    | Servicios ofrecidos por el restaurante (WiFi, estacionamiento, etc)                                                |

- `public`

| Ruta             | Descripcion                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------|
| `/contacto`      | Formulario de contacto del restaurante                                                                            |
| `/`              | Página de Inicio                                                                                                  |
| `/login`         | Login de sesión de administrador                                                                                  |
| `/login-exitoso` | En caso de login exitoso se muestra un template                                                                   |
| `/menu`          | Vista del menú con opción de filtrar por categoría                                                                |
| `/reseñas`       | Reseñas de los clientes                                                                                           |
| `/reservas`      | Página para realizar reservas                                                                                     |