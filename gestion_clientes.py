# Con este codigo se cargan los datos en SQL desde Python

from conexion_base_datos import obtener_conexion

def gestionar_clientes():
    print("\n-- GESTIONAR CLIENTES --")
    print("1. Agregar Cliente")
    print("2. Ver Clientes")
    print("3. Modificar cliente")
    print("4. Eliminar cliente")
    print("5. Volver al menú principal")
    subopcion = input("Selecciona una opción: ")

    if subopcion == "1":
        razon_social = input("Razón social: ")
        cuit = input("CUIT: ")
        email = input("Email: ")

        conexion = obtener_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO clientes (razon_social, cuit, email) VALUES (%s, %s, %s)"
                valores = (razon_social, cuit, email)
                cursor.execute(query, valores)
                conexion.commit()
                print("Cliente guardado en la base de datos")
            except Exception as e:
                print("Error al guardar el cliente:", e)
            finally:
                conexion.close()

#Para la opcion 2, se conecta a la base, hace una consulta: SELECT id_cliente, razon_social, cuit, email FROM clientes y lo muestra.
    elif subopcion == "2":
        conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_Cliente, razon_social, cuit, email FROM clientes")
            resultados = cursor.fetchall()

            if resultados:
                print("\n Lista de Clientes:")
                for cliente in resultados:
                    id_cliente, razon_social, cuit, email = cliente
                    print(f"ID_Cliente: {id_cliente} | {razon_social} | CUIT: {cuit} | Email: {email}")
            else:
                print("No hay clientes registrados en la base de datos.")

        except Exception as e:
            print("Error al obtener los clientes:", e)
        finally:
            conexion.close()

#opcion 3 Modificar clientes
    elif subopcion == "3":
     conexion = obtener_conexion()  
    if conexion:
        try:
            cursor = conexion.cursor()

            # Mostrar clientes activos disponibles
            cursor.execute("SELECT id, razon_social, cuit, email FROM clientes WHERE estado = 'activo'")
            resultados = cursor.fetchall()

            if not resultados:
                print("No hay clientes activos para modificar.")
                return

            print("\n📋 Clientes disponibles para modificar:")
            for cliente in resultados:
                print(f"ID: {cliente[0]} | {cliente[1]} | CUIT: {cliente[2]} | Email: {cliente[3]}")

            # Selección de cliente por ID
            cliente_id = input("Ingrese el ID del cliente a modificar: ")

            # Ingreso de nuevos datos
            nuevo_nombre = input("Nuevo nombre o razón social: ")
            nuevo_cuit = input("Nuevo CUIT: ")
            nuevo_email = input("Nuevo email: ")

            # Actualización en base
            query = "UPDATE clientes SET razon_social = %s, cuit = %s, email = %s WHERE id = %s"
            valores = (nuevo_nombre, nuevo_cuit, nuevo_email, cliente_id)
            cursor.execute(query, valores)
            conexion.commit()

            print("✅ Cliente modificado correctamente.")

        except Exception as e:
            print("❌ Error al modificar el cliente:", e)
        finally:
            conexion.close()

from conexion_base_datos import obtener_conexion

def gestionar_clientes():
    print("\n-- GESTIONAR CLIENTES --")
    print("1. Agregar Cliente")
    print("2. Ver Clientes")
    print("3. Modificar cliente")
    print("4. Eliminar cliente")
    print("5. Volver al menú principal")
    subopcion = input("Selecciona una opción: ")

    # Subopción 1 - Agregar
    if subopcion == "1":
        razon_social = input("Razón social: ")
        cuit = input("CUIT: ")
        email = input("Email: ")

        conexion = obtener_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO clientes (razon_social, cuit, email) VALUES (%s, %s, %s)"
                valores = (razon_social, cuit, email)
                cursor.execute(query, valores)
                conexion.commit()
                print("Cliente guardado en la base de datos")
            except Exception as e:
                print("Error al guardar el cliente:", e)
            finally:
                conexion.close()

    # Subopción 2 - Ver. Se crea la sentencia SELECT para traer los datos de SQL
    elif subopcion == "2":
        conexion = obtener_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_cliente, razon_social, cuit, email FROM clientes WHERE estado = 'activo'")
                resultados = cursor.fetchall()

                if resultados:
                    print("\n Lista de Clientes:")
                    for cliente in resultados:
                        id_cliente, razon_social, cuit, email = cliente
                        print(f"ID: {id_cliente} | {razon_social} | CUIT: {cuit} | Email: {email}")
                else:
                    print("No hay clientes activos")
            except Exception as e:
                print("Error al obtener los clientes:", e)
            finally:
                conexion.close()

    # Subopción 3 - Modificar. Se genera mediante el comando UPDATE
    elif subopcion == "3":
        conexion = obtener_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_cliente, razon_social, cuit, email FROM clientes WHERE estado = 'activo'")
                resultados = cursor.fetchall()

                if not resultados:
                    print("No hay clientes activos para modificar.")
                    return

                print("\n📋 Clientes disponibles para modificar:")
                for cliente in resultados:
                    print(f"ID: {cliente[0]} | {cliente[1]} | CUIT: {cliente[2]} | Email: {cliente[3]}")

                cliente_id = input("Ingrese el ID del cliente a modificar: ")
                nuevo_nombre = input("Nuevo nombre o razón social: ")
                nuevo_cuit = input("Nuevo CUIT: ")
                nuevo_email = input("Nuevo email: ")

                query = "UPDATE clientes SET razon_social = %s, cuit = %s, email = %s WHERE id_cliente = %s"
                valores = (nuevo_nombre, nuevo_cuit, nuevo_email, cliente_id)
                cursor.execute(query, valores)
                conexion.commit()

                print("Cliente modificado correctamente")
            except Exception as e:
                print("Error al modificar el cliente:", e)
            finally:
                conexion.close()

    # Subopción 4 - Suspender
    elif subopcion == "4":
        conexion = obtener_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_cliente, razon_social FROM clientes WHERE estado = 'activo'")
                resultados = cursor.fetchall()

                if not resultados:
                    print("No hay clientes activos para suspender")
                    return

                print("\n Clientes activos:")
                for cliente in resultados:
                    print(f"ID: {cliente[0]} | {cliente[1]}")

                cliente_id = input("Ingrese el ID del cliente a suspender: ")
                cursor.execute("UPDATE clientes SET estado = 'suspendido' WHERE id_cliente = %s", (cliente_id,))
                conexion.commit()
                print("Cliente marcado como 'suspendido'")
            except Exception as e:
                print("Error al suspender el cliente:", e)
            finally:
                conexion.close()
