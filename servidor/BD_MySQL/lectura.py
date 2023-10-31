import mysql.connector
from mysql.connector import Error 

try: 
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        db='condominio' ,
    )
    print ("Se conectó.")

    if conexion.is_connected():
        print("Conexion exitosa.")
        cursor = conexion.cursor()
        cursor.execute("SELECT database();")
        registro = cursor.fetchone()
        print("Conectado a la BD:", registro)
        cursor.execute("SELECT * FROM tipo_usuario")
        resultados=cursor.fetchall()
        for fila in resultados:
            print(fila[0],fila[1], fila[2] )
except Error as ex:
    print("Error durante la conexion:", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalizado.")