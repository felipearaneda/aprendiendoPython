"""
#Ejercicio 7
Hacer un programa que muestre todos los números impares
entre dos números que elija el usuario
"""

num1 = int(input("Rango mínimo:\n"))
num2 = int(input("Ramgo máximo:\n"))

if num1 < num2:
    for rango in range(num1, num2):
        if rango%2 == 1:
            print(f"{rango} Es impar")
else:
    print("Rangos erróneos")