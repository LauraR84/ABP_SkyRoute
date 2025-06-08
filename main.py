#Este codigo ejecuta el menu tomando las funciones que se crearon para cada opcion.

# Inicia el programa
print("Bienvenidos a SkyRoute - Sistema de Gestion de Pasajes")

opcion = ""  # Inicializamos la variable

from datetime import datetime  #se importan los datos para usarlos despues en la carga de la fecha de venta
from gestion_clientes import gestionar_clientes
from gestion_destinos import gestionar_destinos
from gestion_ventas import registrar_venta
from gestion_ventas import boton_arrepentimiento
from gestion_ventas import consultar_ventas

# Bucle que se repite hasta que el usuario elija "8"
while opcion != "8":
    print("Menu Principal")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Boton de Arrepentimiento")
    print("6. Ver Reporte General")
    print("7. Acerca del sistema")
    print("8. Salir")


    opcion = input("Seleccionar una opción: ")

    if opcion == "1":
        gestionar_clientes()  
        #invoca la funcion que carga, modifica y elimina los datos de clientes en SQL
         
    elif opcion == "2":   
        gestionar_destinos() 
        #invoca la funcion que carga, modifica y elimina los destinos en SQL

    elif opcion == "3":
        registrar_venta()
        #invoca la funcion para cargar una venta

    elif opcion == "4":
        consultar_ventas()
        #invoca la funcion que muestra la lista de ventas en estado activo.

    elif opcion == "5":
        boton_arrepentimiento()
        #permite anular una venta
