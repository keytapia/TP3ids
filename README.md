# Proyecto Final Integrador 2026C1 - Introducción al Desarrollo de Software

El presente proyecto de la materia Introducción al Desarrollo de Software de la Facultad de Ingeniería de la Universidad de Buenos Aires integra todos los temas aprendidos.

El desarrollo del mismo contempla Backend, Frontend, Base de datos MySQL, y se encuentra versionado en este repositorio de GitHub. Se aplican buenas prácticas de programación y se utilizan metodologías ágiles para su resolución.

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
| 112048     | SILVA            | Franco Gabriel       |
| 115130     | TAPIA            | Keyla                |

# Sitio web gastronómico con reserva

## Naza - Restaurante

"Naza" es una aplicación web gastronómica orientada a la gestión de reservas online para su restaurante.

El sistema permitirá a los usuarios visualizar información del establecimiento, consultar el menú, realizar reservas y recibir confirmaciones mediante correo electrónico y códigos QR.

Además, contará con un panel administrativo para la gestión de reservas, menú, reseñas, servicios y estadísticas.

### Arquitectura del proyecto

El proyecto se encuentra dividido en dos aplicaciones principales:

- **Backend**: API RESTful desarrollada utilizando Flask, encargada de la lógica de negocio, autenticación, gestión de reservas, generación de códigos QR y comunicación con la base de datos MySQL.

- **Frontend**: Aplicación desarrollada utilizando Flask y motor de plantillas Jinja, encargada de la interfaz visual del sistema y la interacción con la API backend.

Ambas aplicaciones se ejecutarán de forma independiente en distintos puertos y se comunicarán mediante solicitudes HTTP respetando una arquitectura RESTful.

La persistencia de datos se realizará utilizando una base de datos MySQL.

### Estructura del repositorio

- `Frontend/` → Aplicación frontend desarrollada con Flask y Jinja.
- `Backend/` → API RESTful, lógica de negocio y conexión con MySQL.
- `docs/` → Documentación, backlog y mockup del proyecto.