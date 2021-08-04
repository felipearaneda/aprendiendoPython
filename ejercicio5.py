""" 
#Ejercicio 5
Hacer un programa que muestre todos los números
entre dos números que diga el usuario.
"""

num1 = int(input("Ingrese primer número:\n"))
num2 = int(input("Ingrese segundo número:\n"))
print(" ")

if num1 < num2:

    for contador in range (num1, num2):
        print(contador)
else:
    print("\n"+"Primer número debe ser menor al segundo número")