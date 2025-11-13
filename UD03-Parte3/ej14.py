"""
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número
invertido.   
"""

n = input("Introduce un número de dos cifras: ")
if len(n) == 2:
    try:
        numero_invertido = n[1] + n[0]
        print(int(numero_invertido))
    except:
        print('Error: lo introducido no es un número.')
else:
    print("Debe ser de longitud 2 [01-99]")
