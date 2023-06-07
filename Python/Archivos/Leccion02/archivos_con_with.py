from ManejoArchivos import ManejoArchivos

# Manejo de contexto with: sintaxis simplificada, abre y cierra el archivo

# with open('prueba.txt', 'r', encoding= 'UTF8') as archivo:
#   print(archivo.read())
# No hace falta el try ni el finallly
# en el contexto de with lo que se ejecuta de manera automática
# utiliza diferentes métodos: __enter__es el que abre
# El siguiente método que cierra: __exit__

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
