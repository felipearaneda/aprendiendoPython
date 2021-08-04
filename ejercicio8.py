"""
#Ejercicio 8
¿Cuanto es el X porciento de Y numero?
                    20% de 150
"""

num = int(input("Introduzca número:\n"))
pctj = int(input(f"Introduzca porcentaje que desee de {num} :\n"))

result = pctj/100

print(f"El {pctj}% de {num} es = {num*result}")