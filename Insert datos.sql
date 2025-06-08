use skyroute;

INSERT INTO clientes (razon_social, cuit, email) VALUES ("Septimo cliente", "20-2233551-22", "septimo@elmail.com");
INSERT INTO clientes (razon_social, cuit, email) VALUES ("Octavo cliente", "20-22555551-22", "octavo@elmail.com");
INSERT INTO clientes (razon_social, cuit, email) VALUES ("Noveno cliente", "20-28765451-22", "noveno@elmail.com");

INSERT INTO destinos (pais, ciudad, costo_base, estado) VALUES ("Argentina", "Buenos Aires", "2345", "activo");
INSERT INTO destinos (pais, ciudad, costo_base, estado) VALUES ("Argentina", "Usuhia", "36548", "activo");
INSERT INTO destinos (pais, ciudad, costo_base, estado) VALUES ("Argentina", "Salta", "23500", "activo");

INSERT INTO ventas (id_cliente, id_destino, fecha_venta, estado) VALUES ("7", "8", "2025-06-05 10:10:00", "activo");
INSERT INTO ventas (id_cliente, id_destino, fecha_venta, estado) VALUES ("8", "3", "2025-06-05 10:11:00", "activo");
INSERT INTO ventas (id_cliente, id_destino, fecha_venta, estado) VALUES ("9", "1", "2025-06-05 10:12:00", "activo");