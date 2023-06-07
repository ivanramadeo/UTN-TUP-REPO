import psycopg2 as bd
# Se importa para poder conectarnos a Pstgre

## objeto de tipo conexion
conexion = bd.connect(user='postgres', password='Arenales554',host='127.0.0.1',port='5432',database='test_bd'
)

##print(conexion)
try:
    conexion.autocommit = False #se inicia la transaccion
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Laura', 'Martinez Frias','lmartinez@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan', 'Juarez Celman', 'jjuarez@mail.com',1)
    cursor.execute(sentencia,valores)


    conexion.commit() # se ciera la transaccion
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f'fOcurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()