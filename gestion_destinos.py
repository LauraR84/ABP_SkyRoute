#Funcion para gestionar el alta, modificacion y baja de destinos de viajes.

from conexion_base_datos import obtener_conexion


def gestionar_destinos():
    print("\n-- GESTIONAR DESTINOS --")
    print("1. Agregar destino")
    print("2. Ver destinos")
    print("3. Modificar destino")
    print("4. Eliminar destino (suspender)")
    print("5. Volver al menú principal")
    subopcion = input("Selecciona una opción: ")

#Subopcion 1 Agregar destino
    if subopcion == "1":
        pais = input("País: ")
        ciudad = input("Ciudad: ")
        costo_base = int(input("Precio: "))

        conexion = obtener_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO destinos (pais, ciudad, costo_base) VALUES (%s, %s, %s)"
                valores = (pais, ciudad, costo_base)
                cursor.execute(query, valores)
                conexion.commit()
                print("Destino guardado")
            except Exception as e:
                print("Error al guardar el destino:", e)
            finally:
                conexion.close()

#Subopcion 2 Ver destinos
    elif subopcion == "2":
        conexion = obtener_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_destino, pais, ciudad, costo_base FROM destinos WHERE estado = 'activo'")
                resultados = cursor.fetchall()
                if resultados:
                    for d in resultados:
                        print(f"ID: {d[0]} | {d[1]}, {d[2]} - ${d[3]}")
                else:
                    print("No hay destinos activos")
            except Exception as e:
                print("Error al consultar destinos:", e)
            finally:
                conexion.close()

#Subopcion 3 Modificar destino
    elif subopcion == "3":
        conexion = obtener_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_destino, pais, ciudad FROM destinos WHERE estado = 'activo'")
                resultados = cursor.fetchall()

                if not resultados:
                    print("No hay destinos para modificar")
                    return

                for d in resultados:
                    print(f"{d[0]}. {d[1]}, {d[2]}")

                id_destino = input("ID del destino a modificar: ")
                nuevo_pais = input("Nuevo país: ")
                nueva_ciudad = input("Nueva ciudad: ")
                nuevo_precio = input("Nuevo precio: ")

                query = "UPDATE destinos SET pais = %s, ciudad = %s, costo_base = %s WHERE id_destino = %s"
                valores = (nuevo_pais, nueva_ciudad, nuevo_precio, id_destino)
                cursor.execute(query, valores)
                conexion.commit()
                print("Destino modificado")
            except Exception as e:
                print("Error al modificar el destino:", e)
            finally:
                conexion.close()

#Subopcion 4 Eliminar destino. El destino no se elimina por completo, sino que quda en estado suspendido.
    elif subopcion == "4":
        conexion = obtener_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_destino, pais, ciudad FROM destinos WHERE estado = 'activo'")
                resultados = cursor.fetchall()

                if not resultados:
                    print("No hay destinos cargados")
                    return

                for d in resultados:
                    print(f"{d[0]}. {d[1]}, {d[2]}")

                id_destino = input("ID del destino a suspender: ")
                cursor.execute("UPDATE destinos SET estado = 'suspendido' WHERE id_destino = %s", (id_destino,))
                conexion.commit()
                print("Destino suspendido")
            except Exception as e:
                print("Error al suspender el destino:", e)
            finally:
                conexion.close()
