-- Crear base de datos (funciona tanto para MySQL como PostgreSQL)
CREATE DATABASE IF NOT EXISTS comentarios_db;

-- Usar la base de datos (MySQL)
USE comentarios_db;

-- Crear tabla comentarios
CREATE TABLE IF NOT EXISTS comentarios (
    id SERIAL PRIMARY KEY,
    texto TEXT NOT NULL,
    usuario_email VARCHAR(255) NOT NULL,
    calificacion INT NOT NULL CHECK (calificacion BETWEEN 1 AND 5),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);