import psycopg2  # Se importa para poder conectarnos a Pstgre


conexion = psycopg2.connect(user='postgres', password='Arenales554',host='127.0.0.1',port='5432',database='test_bd'
)


try:
    with conexion:
        with conexion.cursor() as cursor:
        #cursor = conexion.cursor()
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Roldan', 'jroldan@mail.com',12) #Es una tupla
            cursor.execute(sentencia,valores)
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')
except Exception as e:
    print(f'fOcurrio un error: {e}')
finally:
    conexion.close()