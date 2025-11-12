"""
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número
invertido.   
"""

n = input("Introduce un número de dos cifras: ")

if len(n) >= 2:
    try:
        n = int(n)
        print(n)
    except:
        print('Error: lo introducido no es un número.')
