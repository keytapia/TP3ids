# Naza - Restaurante


## Hipótesis y supuestos

- Se asume que cada cliente utilizará un email válido para recibir confirmaciones de reserva.

- Las reseñas solo podrán ser realizadas por clientes que hayan efectuado una reserva.

- El sistema no incluirá pagos online.

- El administrador será responsable de mantener actualizado el menú y los horarios disponibles.

- El sistema permitirá reservas únicamente dentro de los horarios configurados por el administrador.

---

## Alcance

El presente proyecto consiste en el desarrollo de una aplicación web orientada a la gestión de reservas para un restaurante, permitiendo tanto la interacción de los clientes como la administración interna del negocio. El sistema tendrá como objetivo principal optimizar el proceso de reservas, organización de mesas y administración de información relacionada con clientes, platos y reseñas.
La aplicación contará con dos tipos de usuarios principales:
Clientes, quienes podrán registrarse e iniciar sesión para realizar reservas, consultar el menú disponible y dejar reseñas sobre su experiencia.
Administradores, quienes tendrán acceso a un panel de gestión para administrar reservas, usuarios, menú y estadísticas generales del sistema.
Funcionalidades incluidas en el alcance

1. Gestión de usuarios

El sistema permitirá el registro e inicio de sesión de clientes mediante correo electrónico y contraseña. La información de cada usuario quedará almacenada en una base de datos con el fin de mantener un historial de reservas y contar con referencias de clientes frecuentes.
Datos básicos a almacenar:

Nombre y apellido
Correo electrónico
Contraseña cifrada
Historial de reservas
Reseñas realizadas

2. Gestión de reservas

Los clientes podrán realizar reservas indicando:
Fecha , horario y cantidad de personas
El sistema administrará una cantidad hipotética de mesas del restaurante ), verificando disponibilidad antes de confirmar una reserva.
El administrador podrá:

Confirmar reservas
Cancelarlas
Consultar el estado de ocupación
Visualizar historial de reservas

3. Gestión del menú

El sitio incluirá una sección de menú donde se mostrarán los platos ofrecidos por el restaurante.
Nombre
Descripción
Precio
Imagen ilustrativa
Categoría (entrada, plato principal, postre, bebida, etc.)
Desde el panel administrador se podrán:
Agregar platos
Modificar información
Eliminar platos del menú

4. Sistema de reseñas
Los clientes registrados podrán dejar reseñas y puntuaciones sobre el servicio recibido luego de una reserva.
Las reseñas incluirán:

Comentario
Puntuación
Fecha de publicación
El administrador podrá visualizar y moderar las reseñas desde el panel de administración.

5. Panel de administración
El sistema contará con un panel privado para administradores donde se centralizará la gestión general del restaurante.
El panel incluirá:

Gestión de reservas
Gestión de menú
Gestión de usuarios
Visualización de reseñas
Estadísticas básicas del sistema (cantidad de reservas, clientes registrados, horarios más solicitados, etc.)

##Alcance técnico

Desarrollo frontend de la interfaz web
Desarrollo backend 
Conexión con base de datos
Sistema de autenticación de usuarios

Limitaciones del proyecto
Para mantener el alcance acorde al trabajo práctico académico, no se incluirán:
Pagos online
Integración con servicios externos
Geolocalización
Aplicaciones móviles nativas
Chat en tiempo real

La idea del sistema es que funcione como un prototipo  orientado a demostrar conocimientos de desarrollo web, manejo de bases de datos y diseño de interfaces de usuario

## Mockups

El mockup del sistema se encuentra en el directorio de este repositorio: 

[docs/mockup.pdf](mockup.pdf)
