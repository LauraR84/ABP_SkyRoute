# gestion_clientes.py

clientes = []  # Lista simulada para pruebas (luego se puede conectar a SQL)

def gestionar_clientes():
    print("\n-- GESTIONAR CLIENTES --")
    print("1. Ver Clientes")
    print("2. Agregar Cliente")
    print("3. Modificar Cliente")
    print("4. Eliminar Cliente")
    print("5. Volver al Menú Principal")
    subopcion = input("Selecciona una opción del submenú: ")

    if subopcion == "1":
        print("\n Lista de Clientes:")
        if not clientes:
            print("No hay clientes cargados")   #si no hay clientes cargados, que lo indique
        else:
            for i, c in enumerate(clientes, start=1):   #i es el contador automatico de iteraciones, y cada elemento de la lista de clientes. Cada cliente es un diccionario.
                print(f"{i}. Razón Social: {c['razon_social']}, CUIT: {c['cuit']}, Email: {c['email']}")

    elif subopcion == "2":
        razon_social = input("Razón social del cliente: ")
        cuit = input("CUIT del cliente: ")
        email = input("Email del cliente: ")
        cliente = {"razon_social": razon_social, "cuit": cuit, "email": email}
        clientes.append(cliente)
        print("Cliente agregado correctamente")

    elif subopcion == "3":
        if not clientes:
            print("No hay clientes cargados")  #se continua contemplando la opcion de que no haya clientes cargados
            return
        for i, c in enumerate(clientes, start=1):
            print(f"{i}. {c['razon_social']} ({c['cuit']})")
        num = int(input("Ingrese el número del cliente a modificar: ")) - 1
        if 0 <= num < len(clientes):
            clientes[num]["razon_social"] = input("Nuevo nombre: ")
            clientes[num]["cuit"] = input("Nuevo CUIT: ")
            clientes[num]["email"] = input("Nuevo email: ")
            print("Cliente modificado")
        else:
            print("Número de cliente inválido")

    elif subopcion == "4":
        if not clientes:
            print("No hay clientes cargados")
            return
        for i, c in enumerate(clientes, start=1):
            print(f"{i}. {c['razon_social']} ({c['cuit']})")
        num = int(input("Ingrese el número del cliente a eliminar: ")) - 1
        if 0 <= num < len(clientes):
            eliminado = clientes.pop(num)
            print(f"Cliente eliminado: {eliminado['razon_social']}")
        else:
            print("Número de cliente inválido")

    elif subopcion == "5":
        print("Volviendo al menú principal...")
    else:
        print("Opción inválida")