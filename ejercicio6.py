"""
#Ejercicio 6
Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el título de la tabla y luego las multiplicaciones
"""

for titulo in range (1, 11):
    print(f"########### Tabla del {titulo} ############\n")

    for numero in range (1, 11):
        print(f"{titulo} x {numero} = {numero*titulo}\n")