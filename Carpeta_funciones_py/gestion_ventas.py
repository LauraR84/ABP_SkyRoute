#Funcion para cargar las ventas y los arrepentimientos.

from datetime import datetime
from conexion_base_datos import obtener_conexion

#Registro de venta
def registrar_venta():
    print("\n-- REGISTRAR VENTA --")
    cliente_id = input("ID del cliente: ")
    destino_id = input("ID del destino: ")
    fecha_venta = datetime.now()
    estado = input("Estado de la venta: ")

    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "INSERT INTO ventas (id_cliente, id_destino, fecha_venta, estado) VALUES (%s, %s, %s, %s)"
            valores = (cliente_id, destino_id, fecha_venta, estado)
            cursor.execute(query, valores)
            conexion.commit()
            print(f"Venta registrada el {fecha_venta.strftime('%d/%m/%Y %H:%M')}")
        except Exception as e:
            print("Error al registrar la venta:", e)
        finally:
            conexion.close()

def consultar_ventas():
    print("\n-- CONSULTAR VENTAS ACTIVAS --")
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """
                SELECT v.id_venta, c.razon_social, d.ciudad, d.pais, v.fecha_venta
                FROM ventas v
                JOIN clientes c ON v.id_cliente = c.id_cliente
                JOIN destinos d ON v.id_destino = d.id_destino
                WHERE v.estado = 'activo'
                ORDER BY v.fecha_venta DESC
            """
            cursor.execute(query)
            resultados = cursor.fetchall()

            if not resultados:
                print("No hay ventas activas cargadas")
                return

            print("\n📋 Ventas activas:")
            for venta in resultados:
                id_venta, cliente, ciudad, pais, fecha = venta
                print(f"ID: {id_venta} | Cliente: {cliente} | Destino: {ciudad}, {pais} | Fecha: {fecha.strftime('%d/%m/%Y %H:%M')}")

        except Exception as e:
            print("Error al consultar las ventas:", e)
        finally:
            conexion.close()
    



def boton_arrepentimiento():
    print("\n-- BOTÓN DE ARREPENTIMIENTO --")
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_venta, fecha_venta, estado FROM ventas ORDER BY id_venta DESC LIMIT 1")
            venta = cursor.fetchone()

            if not venta:
                print("No hay ventas cargadas")
                return

            id_venta, fecha_venta, estado = venta
            ahora = datetime.now()
            diferencia = ahora - fecha_venta

            print(f"Última venta: ID {id_venta} - Fecha: {fecha_venta.strftime('%d/%m/%Y %H:%M')}")

            if diferencia.total_seconds() > 120:
                print("No se puede anular. Pasaron más de 60 dias desde la venta") #dice 60 dias pero los representamos en escala con 2 minutos.
                return

            motivo = input("Motivo del arrepentimiento: ")

            # Actualizar estado, fecha_anulacion y motivo_anulacion
            query = "UPDATE ventas SET estado = %s, fecha_anulacion = %s, motivo_anulacion = %s WHERE id_venta = %s"
            valores = ("anulado", ahora, motivo, id_venta)
            cursor.execute(query, valores)
            conexion.commit()

            print(f"Venta ID {id_venta} anulada correctamente a las {ahora.strftime('%H:%M')}")

        except Exception as e:
            print("Error al anular la venta:", e)
        finally:
            conexion.close()