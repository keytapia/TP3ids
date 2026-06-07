# Introducción al Desarrollo de Software - FIUBA | Proyecto Final Integrador 2026C1

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
| 115130     | TAPIA            | Keyla                |

# Sitio web gastronómico con reserva

## **Naza - Restaurante**

"Naza" es una aplicación web gastronómica orientada a la gestión de reservas online para su restaurante.

El sistema permitirá a los usuarios visualizar información del establecimiento, consultar el menú, realizar reservas y recibir confirmaciones mediante correo electrónico y códigos QR.

Además, contará con un panel administrativo para la gestión de reservas, menú, reseñas, servicios y estadísticas.

### **Arquitectura del proyecto**

El proyecto se encuentra dividido en dos aplicaciones principales:

- **Backend**: API RESTful desarrollada utilizando Flask, encargada de la lógica de negocio, autenticación, gestión de reservas, generación de códigos QR y comunicación con la base de datos MySQL.

- **Frontend**: Aplicación desarrollada utilizando Flask y motor de plantillas Jinja, encargada de la interfaz visual del sistema y la interacción con la API backend.

Ambas aplicaciones se ejecutarán de forma independiente en distintos puertos y se comunicarán mediante solicitudes HTTP respetando una arquitectura RESTful.

La persistencia de datos se realizará utilizando una base de datos MySQL.

### **Estructura del repositorio**

- `frontend/` → Aplicación frontend desarrollada con Flask y Jinja.
- `backend/` → API RESTful, lógica de negocio y conexión con MySQL.
- `docs/` → Documentación, backlog y mockup del proyecto.

### **¿Como iniciar la app?**

Como requisito previo debera tener mysql instalado con una contraseña propia, en caso de no tener le dejamos un link informativo:
https://www.conchaalviz.com/blog/como-habilitar-contrasena-para-el-root-de-mysql-en-linux/

Para comenzar, debera crear tres entornos virtuales, uno dentro de cada una de las siguientes carpetas:
- `TP3ids/`
- `TP3ids/backend`
- `TP3ids/frontend`

  Por si no sabe como iniciarlos, aqui dejamos un pequeño instructivo:
  - Ejecute: sudo apt install python3-venv (En caso de no tenerlo)
  - Estando dentro de las respectivas carpetas ejecute;
      - python3 -m venv .venv
      - source .venv/bin/activate
    
Adentro de `TP3ids/backend` cree un archivo .env en donde debera poner lo siguiente:
- SECRET_KEY=Nazarestaurante
- 
- MYSQL_HOST=localhost
- MYSQL_USER=root
- MYSQL_PASSWORD=(**"SU CONTRASEÑA MYSQL"**)
- MYSQL_DB=restaurante_db
- 
- EMAIL_HOST=smtp.gmail.com
- EMAIL_PORT=587
- EMAIL_USER=(**"SU CORREO PERSONAL, NO LABORAL NI ESTUDIANTIL"**)
- EMAIL_PASSWORD=rzvvkjjmuziisnzc(**"SU LLAVE DE ACCESO DE GMAIL"**)

  En caso de no saber o no tener llave de acceso de Gmail, active la verificacion en dos pasos desde la configuracion de su cuenta y luego entre al siguiente enlace, escriba Gmail en donde le pregunta por la aplicacion y escriba lo que obtenga sin espacios
  https://myaccount.google.com/u/4/apppasswords?utm_source=chatgpt.com&rapt=AEjHL4OIl5GX21sg-iEXmBPEUtWimHjYyALdWBbgY-zE3XC0gnP1rAuUN1MLejo01RvpfKoElAh69YVKOB2sDo0Iij8HeAl97gp5Jc4ihXZ0aIVyfx7z3g8

**ANTES DE SEGUIR, RECUERDE QUE CADA ENTORNO DEBE EJECUTARSE EN SU DEBIDA CARPETA, EL DE BACKEND NO DEBE USARSE PARA EL DE FRONT Y VICE VERSA**
**Y PARA CERRARLOS ESCRIBA deactivate**

Teniendo eso ya en cuenta, usted solo debera ejecutar
- bash init.sh

  - hay 3 de estos, cada uno con su rspectivo entorno y carpeta:
  - Cuando usted ejecute el de `TP3ids/` se correran el backend y el frontend a la vez
  - Cuando usted ejecute el de `TP3ids/backend` correra solo el backend
  - Cuando usted ejecute el de `TP3ids/frontend` correra solo el frontend

Al ejecutarse los init.sh le solisitara su contaseña de mysql y puede o no, que tambien de su dispositivo, se intalaran los requerimientos de manera automatica y se le generara un enlace que podra usar en el navegador o una aplicacion como Postman, Bruno, etc.
