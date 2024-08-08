-- script_inventario.sql

-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS inventario_service;

-- Usar la base de datos
USE inventario_service;

-- Crear la tabla de inventario
CREATE TABLE IF NOT EXISTS inventario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_producto VARCHAR(50) UNIQUE NOT NULL,
    cantidad INT NOT NULL
);

-- Opcionalmente, puedes insertar algunos datos de prueba
INSERT INTO inventario (id_producto, cantidad) VALUES
('PROD001', 100),
('PROD002', 150),
('PROD003', 200)
ON DUPLICATE KEY UPDATE cantidad = VALUES(cantidad);