-- Crear base de datos (ejecutar en consola psql como superusuario)
CREATE DATABASE comentarios_db;

-- Conectarse a la base de datos (dentro de psql)
-- \c comentarios_db

-- Crear tabla comentarios
CREATE TABLE IF NOT EXISTS comentarios (
    id SERIAL PRIMARY KEY,
    texto TEXT NOT NULL,
    usuario_email VARCHAR(255) NOT NULL,
    calificacion INT NOT NULL CHECK (calificacion BETWEEN 1 AND 5),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);