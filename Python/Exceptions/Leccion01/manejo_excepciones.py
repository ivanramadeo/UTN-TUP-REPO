'''
Las excepciones o Exceptions se utilizan para mantener funcionando el programa
es decir, que no se detenga la ejecución.
Además pueden servir para mostrar qué tipo de error está ocurriendo
'''
from NumerosIgualesException import NumerosIgualesException
resultado = None # No tiene valor
# La creación de excepciones se hace utilizando clases, en este caso NumerosIgualesException
# Sirve para personalizar aquellas condiciones que podríamos considerar un error acorde a nuestras intenciones
try:
    a = int(input('Ingrese el primer número: '))
    b = int(input('Ingrese el segundo número: '))
    if a == b:
        raise NumerosIgualesException('Son números iguales')
    resultado = a / b
    # 10 / 0
    # resultado = a / b # Modificamos
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    # Exception es la clase padre, más utilizada
    # except ZeroDivisionError as e: (más expecífico)
    # Si se cambia la variable a por un string y se utiliza ZeroDivisionError
    # Resulta en un error no procesado
    print(f'Exception - Ocurrió un error: {type(e)}')
else:
    print('No se arrojó ninguna excepción')
finally: # Siepmpre se va a ejecutar
    print('Ejecución de este bloque finally')
print('--------Línea divisoria----')
print(f'El resultado es: {resultado}')
# Al ocurrir un error, la variable resultado no cambia
print('seguimos....') #Este print demuestra que el código se sigue ejecutando
