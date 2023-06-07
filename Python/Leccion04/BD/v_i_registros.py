import psycopg2  # Se importa para poder conectarnos a Pstgre


conexion = psycopg2.connect(user='postgres', password='Arenales554',host='127.0.0.1',port='5432',database='test_bd'
)


try:
    with conexion:
        with conexion.cursor() as cursor:
        #cursor = conexion.cursor()
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'clara@mail.com'),
                ('Marcos', 'Canto', 'mcanto@mail.com'),
                ('Marcelo', 'Cuenca', 'cuencam@mail.com')
            ) #Es una tupla de tuplas
            cursor.executemany(sentencia,valores)
            # conexion = commit() se utiliza para guardar los cambios en la base de dato
            registros_insertados = cursor.rowcount
            print(f'Los registros inserados son: {registros_insertados}')
except Exception as e:
    print(f'fOcurrio un error: {e}')
finally:
    conexion.close()