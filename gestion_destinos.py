# gestion_destinos.py

destinos = []  # Lista simulada de destinos

def gestionar_destinos():
    print("\n-- GESTIONAR DESTINOS --")
    print("1. Ver Destinos")
    print("2. Agregar Destino")
    print("3. Modificar Destino")
    print("4. Eliminar Destino")
    print("5. Volver al Menú Principal")
    subopcion = input("Selecciona una opción del submenú: ")

    if subopcion == "1":
        print("\n Lista de Destinos:")
        if not destinos:
            print("No hay destinos cargados")
        else:
            for i, d in enumerate(destinos, start=1):
                print(f"{i}. {d['pais']}, {d['ciudad']} - ${d['precio']}")

    elif subopcion == "2":
        pais = input("País: ")
        ciudad = input("Ciudad: ")
        precio = input("Precio: ")
        destino = {"pais": pais, "ciudad": ciudad, "precio": precio}
        destinos.append(destino)
        print("Destino agregado correctamente")

    elif subopcion == "3":
        if not destinos:
            print("No hay destinos cargados")
            return
        for i, d in enumerate(destinos, start=1):
            print(f"{i}. {d['pais']}, {d['ciudad']}")
        num = int(input("Ingrese el número del destino a modificar: ")) - 1
        if 0 <= num < len(destinos):
            destinos[num]["pais"] = input("Nuevo país: ")
            destinos[num]["ciudad"] = input("Nueva ciudad: ")
            destinos[num]["precio"] = input("Nuevo precio: ")
            print("Destino modificado")
        else:
            print("Número de destino inválido")

    elif subopcion == "4":
        if not destinos:
            print("No hay destinos cargados")
            return
        for i, d in enumerate(destinos, start=1):
            print(f"{i}. {d['pais']}, {d['ciudad']}")
        num = int(input("Ingrese el número del destino a eliminar: ")) - 1
        if 0 <= num < len(destinos):
            eliminado = destinos.pop(num)
            print(f"Destino eliminado: {eliminado['ciudad']} ({eliminado['pais']})")
        else:
            print("Número de destino inválido.")

    elif subopcion == "5":
        print("Volviendo al menú principal...")
    else:
        print("Opción inválida.")