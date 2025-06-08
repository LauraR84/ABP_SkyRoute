create database skyroute;
CREATE TABLE `clientes` (
  `ID_Cliente` int NOT NULL AUTO_INCREMENT,
  `Razon_Social` varchar(45) NOT NULL,
  `CUIT` varchar(20) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `estado` varchar(20) DEFAULT 'activo',
  PRIMARY KEY (`ID_Cliente`)
)

CREATE TABLE `destinos` (
  `ID_Destino` int NOT NULL AUTO_INCREMENT,
  `Pais` varchar(45) NOT NULL,
  `Ciudad` varchar(45) NOT NULL,
  `Costo_Base` int NOT NULL,
  `estado` varchar(20) DEFAULT 'activo',
  PRIMARY KEY (`ID_Destino`)
)

CREATE TABLE `ventas` (
  `ID_Venta` int NOT NULL AUTO_INCREMENT,
  `ID_Cliente` int NOT NULL,
  `ID_Destino` int NOT NULL,
  `Fecha_Venta` datetime NOT NULL,
  `Estado` varchar(45) NOT NULL,
  `Fecha_anulacion` datetime DEFAULT NULL,
  `Motivo_anulacion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID_Venta`),
  KEY `ID_Cliente_idx` (`ID_Cliente`),
  KEY `ID_Destino_idx` (`ID_Destino`),
  CONSTRAINT `fk_destino` FOREIGN KEY (`ID_Destino`) REFERENCES `destinos` (`ID_Destino`),
  CONSTRAINT `ID_Cliente` FOREIGN KEY (`ID_Cliente`) REFERENCES `clientes` (`ID_Cliente`)
) 



