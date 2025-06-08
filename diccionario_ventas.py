#Acá se van a guardar los datos en formato de diccionario. Se incluye
#Registro de ventas y registro de "Botón de Arrepentimiento"

# gestion_ventas.py

from datetime import datetime

ventas = []  # Lista simulada de ventas

def registrar_venta():
    print("\n-- REGISTRAR VENTA --")
    cliente = input("Nombre del cliente: ")
    destino = input("Destino: ")
    fecha = datetime.now()  # Toma fecha y hora actual automáticamente
    estado = input("Estado de la venta (confirmada/pagada/etc.): ")

    venta = {
        "cliente": cliente,
        "destino": destino,
        "fecha": fecha,
        "estado": estado
    }
    ventas.append(venta)
    print(f"Venta registrada: {cliente} -> {destino} - {fecha.strftime('%d/%m/%Y %H:%M')}")

#Para el arrepentimiento, primero se listan todas las ventas numeradas.
#El usuario puede elegir cuál anular.
#Se evalúa si la venta puede ser anulada (dentro del límite de 2 min simulando los 60 días).
#Se guarda la fecha y hora exacta del arrepentimiento automáticamente.

def boton_arrepentimiento():
    print("\n-- BOTÓN DE ARREPENTIMIENTO --")
    if not ventas:
        print("No hay ventas registradas")
        return

    ultima = ventas[-1]
    ahora = datetime.now()
    diferencia = ahora - ultima["fecha"]
    
    print("Ventas registradas:")
    for i, v in enumerate(ventas, start=1):
        estado = v['estado']
        print(f"{i}. Cliente: {v['cliente']} - Destino: {v['destino']} - Fecha: {v['fecha'].strftime('%d/%m/%Y %H:%M')} - Estado: {estado}")
   
    try:
        num = int(input("Ingrese el número de la venta que desea anular: ")) - 1
        if num < 0 or num >= len(ventas):
            print("Número inválido")
            return
    except ValueError:
        print("Entrada inválida")
        return

    venta = ventas[num]
    ahora = datetime.now()
    diferencia = ahora - venta["fecha"]

    if diferencia.total_seconds() > 120:
        print("No se puede anular esta venta. Ya pasaron más de 2 minutos")
        return

    motivo = input("Motivo del arrepentimiento: ")
    venta["estado"] = f"Anulada ({motivo})"
    venta["fecha_anulacion"] = ahora
    print(f"Venta anulada correctamente - {ahora.strftime('%d/%m/%Y %H:%M')}")
