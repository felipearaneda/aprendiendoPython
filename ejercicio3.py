""" 
#Ejercicio 3
Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60
primeros números naturales. Resolver con:
                            -Bucle For
                            -Bucle While
"""

cont = 0

for cont in range(1,62):
    print(f"{cont} x {cont} = {cont*cont}")

num = 0
while num <= 62:
    print(f"{num} x {num} = {num*num}")
    num += 1