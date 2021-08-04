"""
#Ejercicio 10
El programa tiene que pedir la nota de 15 alumnos
y mostrar en pantalla cuantos aprobaron y cuantos suspenden
"""

contador = 0
aprobados = 0
suspendidos = 0

while contador <= 15:
    x = int(input("Ingrese nota:\n"))

    if x >= 4:
        aprobados += 1
    else:
        suspendidos += 1

    contador += 1

print(f"Han aprobado {aprobados} alumnos\n Han suspendido {suspendidos} alumnos")