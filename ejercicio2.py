""" 
Ejercicio 2.
Escribir un script que muestre por pantalla 
todos los números pares del 1 al 120.
"""

num = 1

for num in range(1, 121):
    if num%2 == 0:
        print(f"{num} PAR")
    else:
        print(f"{num} NO ES PAR")