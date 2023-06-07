# archivo = open('prueba.txt', 'r', encoding='UTF-8') # r = read
archivo = open('prueba.txt', 'r', encoding='UTF-8')
# letras: r-read, a-append, w-write, x-crea un archivo
# t-tipo de archivo (text)
#b-tipo de archivo (binary)
#w+ escribir y leer
#r+ leer y escribir

#print(archivo.read())
#print(archivo.read(10))
#print(archivo.read(10))
#print(archivo.readline())
#print(archivo.readline())

# vamos a iterar el archivo
#for linea in archivo:
    #print(linea) #iteramos todos los elementos del archivo
    # print(archivo.readlines()) # accedemos al archivo como si fuera una lista
# print(archivo.readlines()[9])

# Anexamos información, copiamos a otro
archivo2 = open('copia.txt', 'a', encoding='UTF-8')
archivo2.write(archivo.read())
archivo.close() #cerramos el primer archivo
archivo2.close() #cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')
