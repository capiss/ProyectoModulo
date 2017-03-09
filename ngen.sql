-- CREATE USER 'ngenb'@'localhost' IDENTIFIED BY 'hola123.';
-- GRANT ALL PRIVILEGES ON * . * TO 'ngen'@'localhost';
CREATE DATABASE ngen;
use ngen;

CREATE TABLE Dependencia(
        id_dependencia INT NOT NULL,
        nombre varchar(50),
        PRIMARY KEY(id_dependencia)
);
CREATE TABLE Segmento(
	id_segmento INT NOT NULL,
	segmento varchar(15),
	rango varchar(31),
	id_dependencia INT NOT NULL,
	PRIMARY KEY(id_segmento),
	INDEX (id_dependencia),
        FOREIGN KEY (id_dependencia) REFERENCES Dependencia (id_dependencia)
);

CREATE TABLE Responsable(
	id_responsable INT NOT NULL,
        nombre varchar(20),
	apaterno varchar(20),
	apmaterno varchar(20),
	telefono varchar(8),
	extencion varchar(5),
	correo_electronico varchar(30),
	cargo_puesto varchar(20),
	id_dependencia INT NOT NULL,
	PRIMARY KEY(id_responsable),
	INDEX (id_dependencia),
        FOREIGN KEY (id_dependencia) REFERENCES Dependencia (id_dependencia)

); 

INSERT INTO Dependencia value (1, 'Dirección General de Estudios de Legislación Universitaria');
INSERT INTO Dependencia value (2, 'Dirección General de Administración Escolar');
INSERT INTO Dependencia value (3, 'Dirección General de Presupuesto');
INSERT INTO Dependencia value (4, 'Coordinación de Universidad Abierta y Educación a Distancia');
INSERT INTO Dependencia value (5, 'Dirección General del Deporte Universitario');

INSERT INTO Segmento value (1, '132.248.76.0', '132.248.76.1-132.248.76.254', 3 );
INSERT INTO Segmento value (2, '132.248.82.0', '132.248.82.1-132.248.82.254', 3);
INSERT INTO Segmento value (3, '132.248.201.0', '132.248.201.1-132.248.248.127',1);
INSERT INTO Segmento value (4, '132.248.32.0', '132.248.32.1-132.248.32.254', 2);
INSERT INTO Segmento value (5, '132.248.45.0', '132.248.45.1-132.248.45.254', 4);


INSERT INTO Responsable value (1, 'José Luis', 'Marín', 'Correa', '5622 2958', '41822', 'jluismc_751@hotmail.com', 'Secretario Administrativo', 5); 
INSERT INTO Responsable value (2, 'Federico', 'Torres', 'Sotelo', '5623-1443', NULL, 'ftorres@dgp.unam.mx' 'soporte tecnico' 1);
INSERT INTO Responsable value (3, 'Carlos Roberto', 'Martínez', 'Tarelo', '5622-8730', NULL, 'servicios@cuaed.unam.mx', 'secretario administrativo', 4);
INSERT INTO Responsable value (4, 'Liliana', 'Gomez', 'Perez', '5622 0287', '45681', 'liliana@presupuesto.unam.mx', 'jefa de unidad administrativa', 3);
INSERT INTO Responsable value (5, 'Sergio', 'Rodriguez', 'Medina', '5622 3291','2319', 'sergio@administracion.escolar.unam.mx', 'jefe administrativo', 2);

