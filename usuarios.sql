-- BBDD
CREATE DATABASE Usuarios;
USE Usuarios;

-- Tabla para almacenar la información de usuarios
CREATE TABLE datos_usuarios (
    id_us INT PRIMARY KEY,
    nombre_us VARCHAR(50),
    correo_us VARCHAR(100),
    fecha_registro_us DATE
);

-- Tabla para almacenar la información de los usuarios que concedieron los permisos
CREATE TABLE permisos (
    id_permiso_usuario INT PRIMARY KEY,
    nombre_usuario VARCHAR(50)
);

ALTER TABLE permisos
ADD FOREIGN KEY (id_usuario) REFERENCES usuarios(id_us);

