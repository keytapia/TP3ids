CREATE DATABASE IF NOT EXISTS restaurante_db;
USE restaurante_db

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
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
    estado ENUM('pendiente', 'confirmada', 'cancelada') DEFAULT 'pendiente',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (mesa_id) REFERENCES mesas(id)
);

CREATE TABLE categoria_platos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE platos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria_id INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
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
    id INT AUTO_INCREMENT
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

