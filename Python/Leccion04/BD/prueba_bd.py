import psycopg2  # Se importa para poder conectarnos a Pstgre

## objeto de tipo conexion
conexion = psycopg2.connect(user='postgres', password='Arenales554',host='127.0.0.1',port='5432',database='test_bd'
)

##print(conexion)
try:
    with conexion:
        with conexion.cursor() as cursor:
        #cursor = conexion.cursor()
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #PLaceholder
            id_persona = input('Ingrese el numero de id: ')
            cursor.execute(sentencia, (id_persona,)) # De esta manera ejecutamos la sentencia
            registros = cursor.fetchone() #Recuperamos todos los registros que serán una lista
            print(registros)
except Exception as e:
    print(f'fOcurrio un error: {e}')
finally:
    conexion.close()
#https://www.psycopg.org/docs/usage.html