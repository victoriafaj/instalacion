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
        #infoServer = conexion.get_server_ifo()
       #print("Info del servidor:", infoServer)
        cursor = conexion.cursor()
        nombre = input("Ingrese nombre de usuario: ")
        #cursor. execute("INSERT INTO tipousuario (nombre) VALUES ('Vigilante')") 
        sentencia="INSERT INTO tipousuario (nombre) Values ('{0}')".format(nombre)
        cursor.execute(sentencia)
        conexion.commit()
        print("Registro insertado con éxito.")

except Error as ex:
    print("Error durante la conexion:", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalizado.")