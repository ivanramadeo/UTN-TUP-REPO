# Declaramos una variable

# se utiliza un método (open) para abrir un archivo existente, o para crear uno
# open puede generar una excepción, es recomendable que esté dentrod de try
try:
    archivo = open('prueba.txt', 'w', encoding='UTF-8')  # w = write
    archivo.write('Programamos con diferentes tipos de archivo, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución  y producción\n ')
    archivo.write('\nletras: r-read, a-append, w-write, x-crea un archivo')
    archivo.write('\nt-tipo de archivo (text)')
    archivo.write('\nb-tipo de archivo (binary)')
    archivo.write('\nw+ escribir y leer')
    archivo.write('\nr+ leer y escribir')
    archivo.write('\nSaludos a todos los alummnos')
    archivo.write('\n Con esto terminamos')

except Exception as e:
    print(e)
finally:  # siempre se ejecuta
    archivo.close()  # Con esto se debe cerrar el archivo
# archivo.write('Todo quedo perfect') una vez cerrado el archivo(finally)
# Es imposible seguir modificándolo


