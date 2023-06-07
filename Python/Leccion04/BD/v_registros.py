import psycopg2  # Se importa para poder conectarnos a Pstgre


conexion = psycopg2.connect(user='postgres', password='Arenales554',host='127.0.0.1',port='5432',database='test_bd'
)


try:
    with conexion:
        with conexion.cursor() as cursor:
        #cursor = conexion.cursor()
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' #PLaceholder
            entrada = input('Ingrese los id a buscar, separados por coma:')
            #id_persona = input('Ingrese el numero de id: ')
            llaves_primarias =(tuple(entrada.split(', ')),)
            cursor.execute(sentencia,llaves_primarias) # De esta manera ejecutamos la sentencia
            registros = cursor.fetchall() #Recuperamos todos los registros que serán una lista
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'fOcurrio un error: {e}')
finally:
    conexion.close()