--creción de la base de datos
CREATE DATABASE IF NOT EXISTS `restaurante`;
--creación de usuario
CREATE USER 'Usuario'@'%' IDENTIFIED BY 'a.1234567';
--darle privilegios al usuario
GRANT ALL PRIVILEGES ON restaurante.* TO 'Usuario'@'%';
FLUSH PRIVILEGES;