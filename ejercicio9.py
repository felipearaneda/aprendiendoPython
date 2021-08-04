"""
#Ejercicio9
Hacer un programa que pida números al usuario
indefinidamente hasta introducir la cifra 111
"""
print("######## PARA SALIR INTRODUZCA *111* ###########")
num = int(input("Introduzca número:\n"))
print(f"Ha introducido {num}\n ")

while num != 111:
    num = int(input("Vuelva a introducir un número:\n"))
    print(f"Ha introducido {num}\n")
    
    if num == 111:
        print("Programa finalizado")
        break