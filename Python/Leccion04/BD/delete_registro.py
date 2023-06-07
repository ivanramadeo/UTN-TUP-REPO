import psycopg2  # Se importa para poder conectarnos a Pstgre


conexion = psycopg2.connect(user='postgres', password='Arenales554',host='127.0.0.1',port='5432',database='test_bd'
)


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Ingrese el numero de registro a eliminar:')
            valores = (entrada,)#Es una tupla de valores
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')
except Exception as e:
    print(f'fOcurrio un error: {e}')
finally:
    conexion.close()