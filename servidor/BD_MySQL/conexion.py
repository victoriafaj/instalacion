import mysql.connector
from mysql.connector import Error
try:
    conexion = mysql.connector.connect (
        host='localhost',
        port=3306,
        user= 'usuario',
        password= 'usuario',
        db='condominio',
    )

    if conexion.is_connected():
        print("Conexión exitosa.")
        infoServer = conexion.get_server_ifo()
        print("Info del servidor:", infoServer)

except Error as ex:
    print("Error durante la conexion:", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalizado.")