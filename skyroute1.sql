use skyroute;
SELECT v.id_venta, c.razon_social, d.ciudad, d.pais, v.fecha_venta
                FROM ventas v
                JOIN clientes c ON v.id_cliente = c.id_cliente
                JOIN destinos d ON v.id_destino = d.id_destino
                WHERE v.estado = 'activo'
                ORDER BY v.fecha_venta DESC;