DROP DATABASE IF EXISTS restaurante_db;
CREATE DATABASE IF NOT EXISTS restaurante_db;
USE restaurante_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    contrasena VARCHAR(255) NULL DEFAULT NULL,
    rol ENUM('cliente', 'admin') DEFAULT 'cliente'
);

CREATE TABLE mesas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT UNIQUE NOT NULL,
    capacidad INT NOT NULL,
    ubicacion ENUM('interior','exterior') NOT NULL,
    estado ENUM('disponible', 'ocupada') DEFAULT 'disponible'
);

CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    mesa_id INT NOT NULL,
    fecha DATE NOT NULL,
    horario TIME NOT NULL,
    cantidad_personas INT NOT NULL,
    notas_adicionales TEXT,
    estado ENUM('confirmada', 'cancelada') DEFAULT 'confirmada',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (mesa_id) REFERENCES mesas(id)
);

CREATE TABLE categorias_platos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE platos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria_id INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    restricciones_alimentarias VARCHAR(100) NULL,
    precio DECIMAL(10,2) NOT NULL,
    imagen VARCHAR(255),
    disponible BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (categoria_id) REFERENCES categorias_platos(id)
);

CREATE TABLE resenas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    reserva_id INT NOT NULL,
    comentario TEXT,
    puntuacion INT CHECK (puntuacion >= 1 AND puntuacion <= 5),
    fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (reserva_id) REFERENCES reservas(id)
);

CREATE TABLE servicios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    disponible CHAR(2) NOT NULL
);



-- ====================================
-- DATOS DE PRUEBA PARA CARGAR TABLAS
-- ====================================


-- =========================
-- USUARIOS
-- =========================

INSERT INTO usuarios
(nombre, apellido, email, telefono, contrasena, rol)

VALUES
('Admin','Admin','admin@restaurante.com','123456789','1234','admin'),
('Juan','Perez','juan@mail.com','123456789',NULL,'cliente'),
('Brenda','Lopez','brenda@mail.com','123456789',NULL,'cliente'),
('Pedro','Garcia','pedro@mail.com','123456789',NULL,'cliente'),
('Maria','Diaz','maria@mail.com','123456789',NULL,'cliente');


-- =========================
-- MESAS
-- =========================

INSERT INTO mesas
(numero, capacidad, ubicacion, estado)

VALUES
(1,2,'interior','disponible'),
(2,4,'interior','disponible'),
(3,6,'exterior','disponible'),
(4,2,'exterior','disponible'),
(5,8,'interior','disponible');


-- =========================
-- CATEGORÍAS
-- =========================

INSERT INTO categorias_platos
(nombre)

VALUES
('Entradas'),
('Carnes'),
('Pastas'),
('Bebidas'),
('Postres');


-- =========================
-- PLATOS
-- =========================

INSERT INTO platos 
(categoria_id, nombre, descripcion, restricciones_alimentarias, precio, imagen)
VALUES
(1, 'Empanadas', 'Empanadas caseras', NULL, 2000.00, 'empanadas.png'),
(1, 'Pizza', 'Pizza de Muzza', 'Vegetariano', 8200.00, 'pizza.png'),
(2, 'Bife', 'Bife con guarnicion', 'Sin TACC', 12000.00, 'bife.png'),
(2, 'Milanesa Napolitana', 'Milanesa Napolitana con guarnicion', NULL, 9500.00, 'milanesa_napolitana.png'),
(3, 'Ravioles', 'Ravioles con salsa bolognesa', NULL, 8000.00, 'ravioles.png'),
(4, 'Coca Cola', 'Bebida 500ml', 'Vegano, Sin TACC', 2500.00, 'coca.png'),
(4, 'Agua Mineral', 'Agua Mineral', 'Vegano, Sin TACC', 1000.00, 'agua_mineral.png'),
(5, 'Flan', 'Flan casero', 'Vegetariano', 2800.00, 'flan.png');

-- =========================
-- RESERVAS
-- =========================

INSERT INTO reservas
(usuario_id,mesa_id,fecha,horario,cantidad_personas,notas_adicionales,estado)

VALUES

(2,1,'2026-05-10','20:00:00',2,'Mesa cerca de ventana','confirmada'),
(3,2,'2026-05-11','21:00:00',4,'','confirmada'),
(4,3,'2026-05-12','20:00:00',6,'Por motivos de salud','cancelada'),
(5,4,'2026-05-15','22:00:00',2,'','confirmada'),
(2,2,'2026-05-16','20:00:00',4,'','confirmada'),
(2,1,'2026-05-17','20:00:00',2,'','cancelada');


-- =========================
-- RESEÑAS
-- =========================

INSERT INTO resenas
(usuario_id, reserva_id, comentario, puntuacion)

VALUES

(2,1,'Excelente atención',5),
(3,2,'Muy rica la comida',4),
(4,3,'El lugar es horrible',1),
(5,4,'Buen ambiente',5);


-- =========================
-- SERVICIOS
-- =========================

INSERT INTO servicios
(nombre,descripcion)

VALUES
('WiFi','Internet gratuito'),
('Pet Friendly','Mascotas permitidas :D'),
('Estacionamiento','Lugar para estacionar');