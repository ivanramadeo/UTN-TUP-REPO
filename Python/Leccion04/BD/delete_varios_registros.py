import psycopg2  # Se importa para poder conectarnos a Pstgre


conexion = psycopg2.connect(user='postgres', password='Arenales554',host='127.0.0.1',port='5432',database='test_bd'
)


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Ingrese los números de registro a eliminar (separados por coma):')
            valores = (tuple(entrada.split(',')),)  # Es una tupla de tuplas
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')
except Exception as e:
    print(f'fOcurrio un error: {e}')
finally:
    conexion.close()