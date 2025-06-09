# conexion de python a la base de datos de MySQL

import mysql.connector
from config import DB_CONFIG

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        return conexion
    except mysql.connector.Error as error:
        print("Error de conexión a la base de datos:", error)
        return None
