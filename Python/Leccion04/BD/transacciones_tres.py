import psycopg2 as bd
# Se importa para poder conectarnos a Pstgre

## objeto de tipo conexion
conexion = bd.connect(user='postgres', password='Arenales554',host='127.0.0.1',port='5432',database='test_bd'
)

##print(conexion)
try:
    with conexion:
        with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
                valores = ('Alex', 'Rojas Frias','arojasfrias@mail.com')
                cursor.execute(sentencia, valores)

                sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
                valores = ('Jose Carlos', 'Juarez Celman', 'jcjuarezcelman@mail.com',1)
                cursor.execute(sentencia,valores)
except Exception as e:
    print(f'fOcurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()
print('Termina la transaccion')