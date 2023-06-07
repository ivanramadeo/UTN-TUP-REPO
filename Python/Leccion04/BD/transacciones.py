import psycopg2 as bd
# Se importa para poder conectarnos a Pstgre

## objeto de tipo conexion
conexion = bd.connect(user='postgres', password='Arenales554',host='127.0.0.1',port='5432',database='test_bd'
)

##print(conexion)
try:
    # conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit() # Hacemos el commit manualmente
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f'fOcurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()