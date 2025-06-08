#Escribir al menos 5 consultas SQL (lenguaje DML - SELECT) que permitan recuperar información relevante del sistema. Ejemplos:

#Listar todos los clientes (primero se listan todos, luego solo los activos)
SELECT id_cliente, razon_social, cuit, email, estado FROM clientes;
SELECT id_cliente, razon_social, cuit, email FROM clientes WHERE estado = 'activo';

#Mostrar las ventas realizadas en una fecha específica. 

SELECT * FROM ventas WHERE DATE(fecha_venta) = '2025-06-05';

#Obtener la última venta de cada cliente y su fecha (ademas se agrupan por razon social).
  #JOIN: une la tabla ventas con la tabla clientes
  #GROUP BY d.Pais: agrupa todas las ventas por cliente

SELECT c.ID_Cliente, c.Razon_Social, MAX(v.Fecha_Venta) AS Ultima_Venta
FROM clientes c
JOIN ventas v ON c.ID_Cliente = v.ID_Cliente
GROUP BY c.ID_Cliente, c.Razon_Social;

#Listar todos los destinos que empiezan con “S” (por una cuestion de pacticidad, reemplazamos S por A)
    #LIKE 'A%': busca todos los valores de la columna Pais que empiezan con "A"
    #% representa cualquier cadena de caracteres despues de la "A".

SELECT * FROM destinos WHERE Pais LIKE 'A%';

#Mostrar cuántas ventas se realizaron por país.
  #JOIN: une la tabla ventas con la tabla destinos para acceder al pais.
  #COUNT(*): cuenta la cantidad de ventas por grupo
  #GROUP BY d.Pais: agrupa todas las ventas por pais
  #ORDER BY: muestra primero los paises con mas ventas

SELECT d.Pais, COUNT(*) AS Cantidad_Ventas
FROM ventas v JOIN destinos d ON v.ID_Destino = d.ID_Destino
GROUP BY d.Pais ORDER BY Cantidad_Ventas DESC;


