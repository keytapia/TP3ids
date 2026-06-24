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

# **Naza - Restaurante**

"Naza" es una aplicación web gastronómica orientada a la gestión de reservas online para su restaurante.

El sistema permitirá a los usuarios visualizar información del establecimiento, consultar el menú, realizar reservas y recibir confirmaciones mediante correo electrónico y códigos QR.

Además, contará con un panel administrativo para la gestión de reservas, menú, reseñas, servicios y estadísticas.

## **Arquitectura**

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

## **Estructura del Repositorio**

- `backend/`  → API RESTful, lógica de negocio y conexión con MySQL.
- `docs/`     → Documentación, backlog y mockup del proyecto.
- `frontend/` → Aplicación frontend desarrollada con Flask y Jinja.
- `docker-compose.yml` → Unión de los contenedores Frontend, Backend y MySQL para usar con Docker

### **Estructura del Frontend**

```
frontend/
├── routes/                             # Rutas Flask que renderizan los templates
│   ├── admin/                              # Rutas del panel de administración
│   │   ├── configuracion.py                    # Gestión de la configuración general del restaurante
│   │   ├── dashboard.py                        # Dashboard principal del administrador
│   │   ├── estadisticas.py                     # Vista de estadísticas y métricas
│   │   ├── menu.py                             # Gestión visual del menú
│   │   ├── resenas.py                          # Gestión visual de reseñas
│   │   ├── reservas.py                         # Gestión visual de reservas
│   │   └── servicios.py                        # Gestión visual de servicios
│   └── public/                             # Rutas públicas del sitio web
│       ├── contacto.py                         # Página de contacto
│       ├── inicio.py                           # Página principal (Home)
│       ├── login.py                            # Inicio de sesión de administrador
│       ├── menu.py                             # Menú del restaurante
│       ├── nosotros.py                         # Información institucional
│       ├── resenas.py                          # Visualización de reseñas
│       └── reservas.py                         # Proceso de reservas online
├── services/                           # Comunicación con la API Backend
│   ├── configuracion.py                    # Consumo de endpoints de configuración del restaurante
│   ├── dashboard.py                        # Consumo de endpoints del dashboard
│   ├── estadisticas.py                     # Consumo de endpoints de estadísticas
│   ├── login.py                            # Consumo de endpoints de autenticación
│   ├── menu.py                             # Consumo de endpoints del menú
│   ├── resenas.py                          # Consumo de endpoints de reseñas
│   ├── reservas.py                         # Consumo de endpoints de reservas
│   └── servicios.py                        # Consumo de endpoints de servicios
├── static/                             # Archivos estáticos
│   ├── images/                             # Imágenes utilizadas por la aplicación
│   │   ├── favicon.ico                         # Ícono del sitio web
│   │   └── ...                                 # Imágenes de platos, banners, etc.
│   ├── scripts/                            # Scripts JavaScript
│   │   ├── estadisticas.js                     # Gráficos y métricas del administrador
│   │   ├── renesas.js                          # Funcionalidades dinámicas para creación y visualización de reseñas
│   │   └── script.js                           # Funcionalidades generales del sitio
│   └── styles/                             # Hojas de estilo CSS
│       ├── admin.css                           # Estilos del panel administrador
│       └── public.css                          # Estilos del sitio público
├── templates/                          # Plantillas HTML renderizadas por Flask
│   ├── admin/                              # Templates del administrador
│   │   ├── agregar_plato.html                  # Formulario para agregar nuevos platos al menú
│   │   ├── agregar_servicio.html               # Formulario para agregar nuevos servicios
│   │   ├── base.html                           # Layout base del administrador
│   │   ├── configuracion.html                  # Gestión de la configuración del restaurante
│   │   ├── dashboard.html                      # Dashboard principal
│   │   ├── editar_plato.html                   # Formulario para editar platos existentes
│   │   ├── editar_servicio.html                # Formulario para editar servicios existentes
│   │   ├── estadisticas.html                   # Vista de estadísticas
│   │   ├── menu.html                           # Gestión del menú
│   │   ├── resenas.html                        # Gestión de reseñas
│   │   ├── reservas.html                       # Gestión de reservas
│   │   └── servicios.html                      # Gestión de servicios
│   └── public/                             # Templates públicos
│       ├── base.html                           # Layout base público
│       ├── cancelar_reserva.html               # Confirmación de cancelación de una reserva
│       ├── contacto.html                       # Página de contacto
│       ├── crear_resena.html                   # Formulario para crear una reseña
│       ├── index.html                          # Página principal
│       ├── login_administrador.html            # Formulario de inicio de sesión para administradores
│       ├── login_cliente.html                  # Formulario de inicio de sesión para clientes
│       ├── login_exitoso.html                  # Confirmación de login exitoso
│       ├── menu.html                           # Menú del restaurante
│       ├── mis_reservas.html                   # Consulta y gestión de reservas del usuario autenticado
│       ├── nosotros.html                       # Página institucional
│       ├── registrar_cuenta.html               # Formulario de registro de nuevos usuarios
│       ├── resenas.html                        # Página de reseñas
│       └── reservas.html                       # Página de reservas
├── utils/
│   └── auth.py                             # Decoradores y utilidades de autenticación y control de acceso
├── .dockerignore
├── app.py                              # Punto de entrada de la aplicación Flask
├── Dockerfile                          # Definición de la imagen Docker del frontend
├── requirements.txt                    # Dependencias del proyecto
└── setup_virtualenv.sh                 # Script de instalación y configuración
```

### **Estructura del Backend**

```
backend/
├── database/                      # Scripts SQL de creación e inicialización de la base de datos
│   └── restaurante_db.sql            # Estructura y datos iniciales de la base de datos
├── repositories/                  # Acceso a datos y consultas SQL
│   ├── auth.py                       # Queries relacionadas con autenticación
│   ├── configuracion.py              # Queries de configuración general del restaurante
│   ├── dashboard.py                  # Queries para estadísticas y dashboard
│   ├── estadisticas.py               # Queries para generación de estadísticas y métricas
│   ├── menu.py                       # Queries de platos y categorías
│   ├── resenas.py                    # Queries de creación, consulta y administración de reseñas
│   ├── reservas.py                   # Queries de reservas y mesas
│   ├── servicios.py                  # Queries de servicios ofrecidos
│   └── usuarios.py                   # Queries de usuarios
├── routes/                        # Endpoints y blueprints de la API
│   ├── admin/                        # Rutas exclusivas para administradores
│   │   ├── configuracion.py              # Endpoints para administración de la configuración del restaurante
│   │   ├── dashboard.py                  # Endpoints del dashboard administrativo
│   │   ├── estadisticas.py               # Endpoints de estadísticas
│   │   ├── menu.py                       # Gestión administrativa del menú
│   │   ├── resenas.py                    # Gestión administrativa de reseñas
│   │   ├── reservas.py                   # Gestión administrativa de reservas
│   │   └── servicios.py                  # Gestión administrativa de servicios
│   └── public/                       # Rutas accesibles para clientes y público general
│       ├── auth.py                       # Inicio de sesión y autenticación
│       ├── menu.py                       # Consulta del menú
│       ├── resenas.py                    # Consulta y creación de reseñas
│       ├── reservas.py                   # Creación y consulta de reservas
│       ├── servicios.py                  # Consulta de servicios del restaurante
│       └── usuarios.py                   # Operaciones relacionadas con usuarios
├── services/                      # Lógica de negocio de la aplicación
│   ├── auth.py                       # Procesamiento de autenticación
│   ├── configuracion.py              # Lógica de negocio de configuración del restaurante
│   ├── dashboard.py                  # Procesamiento de estadísticas
│   ├── email.py                      # Envío de correos electrónicos
│   ├── estadisticas.py               # Procesamiento y cálculo de estadísticas
│   ├── menu.py                       # Lógica de gestión del menú
│   ├── qr.py                         # Generación de códigos QR
│   ├── resenas.py                    # Lógica de negocio de reseñas
│   ├── reservas.py                   # Lógica de reservas y disponibilidad
│   ├── scheduler.py                  # Programación de tareas automáticas periódicas. (*)
│   ├── servicios.py                  # Lógica de gestión de servicios
│   └── usuarios.py                   # Lógica de gestión de usuarios
├── utils/                         # Utilidades y componentes auxiliares
│   ├── constants.py                  # Constantes globales de la aplicación
│   └── validators.py                 # Validaciones y reglas de negocio reutilizables
├── .dockerignore                  # Archivos y directorios excluidos del contexto de construcción Docker
├── app.py                         # Punto de entrada principal de la aplicación Flask (puerto 5000)
├── db.py                          # Configuración y conexión a MySQL
├── Dockerfile                     # Definición de la imagen Docker del backend
├── requirements.txt               # Dependencias de Python del proyecto
└── setup_virtualenv.sh            # Script de instalación y configuración automática

(*) scheduler.py → Ejecuta automáticamente cada cierto tiempo (puesto cada 1 minuto de ejemplo) la finalización de reservas vencidas y el envío de correos para solicitar reseñas.
```

## **Requisitos Previos**

- Python 3.10+
- Docker (opcional)

## **Configuración y Ejecución del Proyecto**

### 1. Variables de entorno

#### **Ejecución Local**
Si correrá el proyecto localmente por terminal deberá crear los siguientes archivos:

- En `TP3ids/backend` un archivo `.env`

```bash
cd TP3ids/backend
touch .env
```

y dentro del mismo debe copiar el siguiente código:

```
# ===============================================
# Flask
# ===============================================

SECRET_KEY=Nazarestaurante


# ===============================================
# Base de datos (usa estas variables el backend)
# ===============================================

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=<SU CONTRASEÑA MYSQL DEL USUARIO ROOT>
MYSQL_DB=restaurante_db


# ===============================================
# Email
# ===============================================

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=<SU CORREO DE GMAIL>
EMAIL_PASSWORD=<SU CONTRASEÑA DE APLICACIÓN DE GMAIL>

```

Donde deberá reemplazar los siguientes campos:

`<SU CONTRASEÑA MYSQL DEL USUARIO ROOT>` por la contraseña de su usuario `root` de MySQL.  
`<SU CORREO DE GMAIL>` por una cuenta de Gmail válida desde la cual se enviarán los correos electrónicos del sistema.  
`<SU CONTRASEÑA DE APLICACIÓN DE GMAIL>` por una contraseña de aplicación generada desde su cuenta de Google. (ver [Cómo obtener una contraseña de aplicación de Gmail](#cómo-obtener-una-contraseña-de-aplicación-de-gmail))  

- En `TP3ids/frontend` un archivo `.env`

```bash
cd TP3ids/frontend
touch .env
```

Y copiar dentro del mismo lo siguiente:

```
# ==========================================
# URL del Backend para utilizar localmente
# ==========================================

API_BACKEND_URL=http://localhost:5000
```

#### **Ejecución con Docker**
Si se levantará el proyecto utilizando Docker, deberá crear los siguientes archivos:

- En `TP3ids/backend` un archivo `.env.docker` → Variables de entorno utilizadas por el contenedor Backend cuando el proyecto se ejecuta mediante Docker.

```bash
cd TP3ids/backend
touch .env.docker
```

```
# ===============================================
# Flask
# ===============================================

SECRET_KEY=Nazarestaurante


# ===============================================
# Base de datos (usa estas variables el backend)
# ===============================================

MYSQL_HOST=mysql
MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_DB=restaurante_db


# ===============================================
# Email
# ===============================================

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=<SU CORREO DE GMAIL>
EMAIL_PASSWORD=<SU CONTRASEÑA DE APLICACIÓN DE GMAIL>
```

Donde deberá reemplazar los siguientes campos:

`<SU CORREO DE GMAIL>` por una cuenta de Gmail válida.  
`<SU CONTRASEÑA DE APLICACIÓN DE GMAIL>` por una contraseña de aplicación generada desde su cuenta de Google (ver [Cómo obtener una contraseña de aplicación de Gmail](#cómo-obtener-una-contraseña-de-aplicación-de-gmail)).  

- En `TP3ids/backend` un archivo `.mysql-env` → Variables de entorno utilizadas exclusivamente por la imagen oficial de MySQL para crear e inicializar la base de datos dentro del contenedor Docker.

```bash
cd TP3ids/backend
touch .mysql-env
```

```
# ====================================================
# Variables que usa la imagen oficial MySQL de Docker
# ====================================================

MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=restaurante_db
```

- En `TP3ids/frontend` un archivo `.env.docker` → Variables de entorno utilizadas por el contenedor Frontend cuando el proyecto se ejecuta mediante Docker.

```bash
cd TP3ids/frontend
touch .env.docker
```

```
# ==========================================
# URL del Backend para utilizar en Docker
# ==========================================

API_BACKEND_URL=http://backend:5000
```

> **Nota:**  
> Los archivos `.env.docker` y `.mysql-env` son utilizados únicamente cuando el proyecto se ejecuta mediante Docker Compose. Para la ejecución local se utilizarán los archivos `.env`.  
> La contraseña `root` utilizada en la configuración Docker corresponde únicamente al servidor MySQL creado dentro del contenedor y no afecta ninguna instalación local de MySQL presente en el sistema del usuario.

### 2. Instalación y Ejecución

#### **Ejecución Local**

Una vez creados los archivos `.env`, deberá ejecutar scripts de setup que el proyecto incluye para el backend y para el frontend. Los mismos ejecutan todo lo necesario para crear y levantar cada aplicación.

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

#### **Ejecución con Docker**

Una vez creados los archivos `.env.docker` y `.mysql-env`, desde la raíz del proyecto ejecutar:

```bash
docker compose up --build
```

Este comando:

- Construye las imágenes del Frontend y Backend.
- Descarga la imagen oficial de MySQL (si no existe localmente).
- Crea y levanta los contenedores necesarios.
- Inicializa automáticamente la base de datos utilizando el script ubicado en `backend/database/restaurante_db.sql`.

Una vez finalizado el proceso, la aplicación quedará disponible en:

- Frontend: http://localhost:8080
- Backend: http://localhost:5000

Luego podrá ejecutar los comandos de Docker (ver [Comandos útiles de Docker](#comandos-útiles-de-docker))  

## Endpoints

Los endpoints estan divididos en `admin` y `public`

- `admin`

Se encuentran bajo el prefijo `/api/admin`. Las respuestas son JSON.
 
| Metodo | Endpoint                                  | Descripcion                                                                      |
|--------|-------------------------------------------|----------------------------------------------------------------------------------|
| GET    | `/configuracion`                          | Obtener la configuración general del restaurante                                 |
| PUT    | `/configuracion`                          | Modificar la configuración general del restaurante                               |
| GET    | `/dashboard`                              | Dashboard General (resumen, próximas reservas, cancelaciones de hoy, reseñas)    |
| GET    | `/estadisticas`                           | Obtener estadísticas                                                             |
| GET    | `/menu`                                   | Listar el menú completo                                                          |
| GET    | `/menu/<int:id>`                          | Obtener un plato específico por id                                               |
| POST   | `/menu`                                   | Crear un plato del menú                                                          |
| PUT    | `/menu/<int:id>`                          | Modificar un plato del menú                                                      |
| DELETE | `/menu/<int:id>`                          | Modificar un plato del menú                                                      |
| GET    | `/resenas`                                | Obtener todas las reseñas                                                        |
| GET    | `/resenas/<int:id>`                       | Obtener una reseña específica por id                                             |
| PATCH  | `/resenas/<int:id>`                       | Cambiar el estado de una reseña (mostrar/oculta)                                 |
| DELETE | `/resenas/<int:id>`                       | Eliminar una reseña por id                                                       |
| GET    | `/reservas`                               | Visualizar las reservas                                                          |
| GET    | `/reservas/estado/<estado>`               | Visualizar el estado de las reservas (filtra por estado)                         |
| PATCH  | `/reservas/cancelar/<int:reserva_id>`     | Cancelar una reserva por id cambiando su estado a "cancelada"                    |
| GET    | `/servicios`                              | Listar todos los servicios                                                       |
| GET    | `/servicios/<int:id>`                     | Obtener un servicio específico por id                                            |
| POST   | `/servicios`                              | Crear un servicio                                                                |
| PUT    | `/servicios/<int:id>`                     | Modificar un servicio                                                            |
| DELETE | `/servicios/<int:id>`                     | Eliminar un servicio                                                             |

- `public`

Se encuentran bajo el prefijo `/api`. Las respuestas son JSON.

| Metodo | Endpoint                                  | Descripcion                                                                      |
|--------|-------------------------------------------|----------------------------------------------------------------------------------|
| POST   | `/auth/login`                             | Login para el administrador                                                      |
| GET    | `/menu`                                   | Filtrar menu completo o por categoria                                            |
| GET    | `/menu/<int:plato_id`                     | Filtrar un plato especifico por numero id                                        |
| GET    | `/categorias`                             | Listar categorias disponibles                                                    |
| GET    | `/resenas`                                | Obtener todas las reseñas disponibles que el admin no oculta                     |
| GET    | `/resenas/<int:id>`                       | Obtener una reseña específica por id                                             |
| POST   | `/resenas/crear`                          | Crear una reseña asociada a una reserva                                          |
| POST   | `/resenas/crear/<int:reserva_id>`         | Crear una reseña utilizando una reserva específica                               |
| GET    | `/resenas/promedio`                       | Obtener la puntuación promedio de las reseñas                                    |
| PATCH  | `/reservas/<int:id>/cancelar-cliente`     | Cancelar reserva                                                                 |
| GET    | `/mesas-disponibles`                      | Obtener mesas por estado                                                         |
| GET    | `/disponibilidad`                         | Ver disponibilidad general                                                       |
| POST   | `/reservas`                               | Crear reserva para un cliente                                                    |
| GET    | `/reservas/mis-reservas/<int:usuario_id>` | Obtener todas las reservas de un usuario                                         |
| GET    | `/servicios`                              | Listar todos los servicios                                                       |
| POST   | `/usuarios/registro`                      | Registrar una nueva cuenta de cliente                                            |


## Páginas

Las páginas web estan divididas en `admin` para el uso de adminitrador y `public` para la vista de los clientes y público en general.

- `admin`

Se encuentran bajo el prefijo `/admin`

| Ruta                           | Descripcion                                                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------------------------------|
| `/configuracion`               | Configuración general del restaurante                                                                          |
| `/dashboard`                   | Visualización de un dashboard con cantidad de reservas, usuarios totales, reseñas totales                      |
| `/estadisticas`                | Gráficos de reservas por horario y reservas por día                                                            |
| `/menu`                        | Menu completo con categorias y platos                                                                          |
| `/menu/agregar`                | Formulario para agregar un nuevo plato al menú                                                                 |
| `/menu/editar/<int:id>`        | Formulario para editar un plato existente                                                                      |
| `/menu/eliminar/<int:id>`      | Eliminar un plato del menú                                                                                     |
| `/resenas`                     | Vista de las reseñas de los clientes                                                                           |
| `/resenas/estado/<int:id>`     | Cambiar el estado de una reseña para que se muestre al público o se oculte                                     |
| `/resenas/eliminar/<int:id>`   | Eliminar una reseña                                                                                            |
| `/reservas`                    | Reservas totales con detalle del cliente                                                                       |
| `/reservas/cancelar/<int:id>`  | Cancelar una reserva específica                                                                                |
| `/servicios`                   | Servicios ofrecidos por el restaurante (WiFi, estacionamiento, etc)                                            |
| `/servicios/agregar`           | Formulario para agregar un nuevo servicio                                                                      |
| `/servicios/editar/<int:id>`   | Formulario para editar un servicio existente                                                                   |
| `/servicios/eliminar/<int:id>` | Eliminar un servicio                                                                                           |

- `public`

| Ruta                           | Descripcion                                                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------------------------------|
| `/contacto`                    | Formulario de contacto del restaurante                                                                         |
| `/`                            | Página de Inicio                                                                                               |
| `/login`                       | Inicio de sesión para clientes                                                                                 |
| `/login/admin`                 | Inicio de sesión para administradores                                                                          |
| `/login-exitoso`               | En caso de login exitoso se muestra un template                                                                |
| `/login/registrate`            | Registro de una nueva cuenta de cliente                                                                        |
| `/logout`                      | Cerrar sesión del usuario actual                                                                               |
| `/menu`                        | Vista del menú con opción de filtrar por categoría                                                             |
| `/nosotros`                    | Información historia del restaurante y servicios que se ofrece                                                 |
| `/resenas`                     | Reseñas de los clientes                                                                                        |
| `/resenas/crear`               | Formulario para crear una reseña                                                                               |
| `/reservas`                    | Página para realizar reservas                                                                                  |
| `/reservas/<int:id>/cancelar`  | Confirmación de cancelación de una reserva                                                                     |
| `/reservas/mis-reservas`       | Visualización de todas las reservas realizadas por el usuario autenticado                                      |


## Anexos

### Cómo obtener una contraseña de aplicación de Gmail

El sistema utiliza Gmail para enviar correos electrónicos de confirmación de reservas, cancelaciones y solicitudes de reseñas. Google no permite utilizar la contraseña normal de la cuenta para este tipo de aplicaciones, por lo que es necesario generar una contraseña de aplicación.

1. Inicie sesión en su cuenta de Google.
2. Active la **Verificación en dos pasos** desde la configuración de seguridad de su cuenta.
3. Acceda a la página de contraseñas de aplicación:

   https://myaccount.google.com/apppasswords

4. En el campo de nombre de la aplicación, escriba un identificador descriptivo (por ejemplo: `TP3 IDS Restaurante`).
5. Google generará una clave de 16 caracteres.
6. Copie esa clave y utilícela como valor de `EMAIL_PASSWORD`, eliminando los espacios que Google muestra únicamente para facilitar la lectura.

Ejemplo:

```env
EMAIL_USER=ejemplo@gmail.com
EMAIL_PASSWORD=abcdefghijklmnop
```

> **Importante:** Nunca utilice la contraseña normal de su cuenta de Gmail. Debe utilizar exclusivamente una contraseña de aplicación generada por Google.

### Comandos útiles de Docker

Detener los contenedores sin eliminarlos:

```bash
docker compose stop
```

Volver a iniciarlos:

```bash
docker compose start
```

Detener y eliminar los contenedores (sin eliminar los datos de la base de datos):

```bash
docker compose down
```

Detener y eliminar los contenedores (eliminando los datos de la base de datos):

```bash
docker compose down -v
```

Reconstruir las imágenes luego de realizar cambios:

```bash
docker compose up --build
```

Ver los logs de todos los servicios:

```bash
docker compose logs -f
```

Ver los contenedores en ejecución:

```bash
docker compose ps
```