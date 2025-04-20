rom random import *

"""
Reparticion de obligaciones

- Jaime
- Carlos
- Andres **2
- Yamit

Objetivo:
1. Implementar las excepciones necesarias al proyecto. 
2. Implementar logs con un archivo .log
3. Modularizar las validaciones en funciones
4. Hacer pruebas de las funciones con Unittest

"""

nombre = input('Ingrese su nombre: ')
print(f'Hola {nombre}, bienvenid@ al Juego de Adivina el numero del 1 al 100 !\n Solo tienes 10 intentos')

numero_random = randint(1, 100) # Se genera el numero aleatorio en ese rango 1 al 100
intentos = 1

while intentos <= 10:
    
    numero = int(input('Ingrese el numero: '))

    if intentos == 10:
        print(f"fallaste en todo {nombre}, era {numero_random} todo este tiempo")
        break
    
    if numero < 1 or numero > 100:
        print("El numero debe de estar 1 y 100. Intenta de nuevo")
        intentos += 1
        continue
    
    elif numero < numero_random:
        print(f'El numero {numero} es menor al que debes adivinar. Sigue intentando.')
        intentos += 1
        continue
    
    elif numero > numero_random:
        print(f'El numero {numero} es mayor al que debes adivinar. Sigue intentando')
        intentos += 1
        continue
    
    #elif numero == numero_random:
    else:
        print(f'FELICIDADES {nombre}\nHa adivinado el numero: {numero}')
        break
    