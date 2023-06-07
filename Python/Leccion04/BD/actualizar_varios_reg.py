import psycopg2  # Se importa para poder conectarnos a Pstgre


conexion = psycopg2.connect(user='postgres', password='Arenales554',host='127.0.0.1',port='5432',database='test_bd'
)


try:
    with conexion:
        with conexion.cursor() as cursor:
        #cursor = conexion.cursor()
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Romina', 'Ayala', 'rayala@mail.com',12),
                ('Maria Laura', 'Vergara', 'mlvergara@mail.com', 10),
            ) #Es una tupla de tuplas
            cursor.executemany(sentencia,valores)
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')
except Exception as e:
    print(f'fOcurrio un error: {e}')
finally:
    conexion.close()