from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as CatPel
opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar las películas')
        print('3. Eliminar catálogo de Peliculs')
        print('4. Salir')
        opcion = int(input('Digite una opcion de menú (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            CatPel.agregar_peliculas(pelicula)
        elif opcion == 2:
            CatPel.listar_peliculas()
        elif opcion == 3:
            CatPel.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrió un error de tipo: {e}')
        opcion = None
    else:
        print('Salimos del programa')
