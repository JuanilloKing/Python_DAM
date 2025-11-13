"""
Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos
variables.    
"""

a = input("Introduce variable numerica A: ")
b = input("Introduce variable numerica B: ")

try:
    invertido_a = a[::-1]
    invertido_b = b[::-1]
    print(f"A invertido: {int(invertido_a)}")
    print(f"B invertido: {int(invertido_b)}")
except:
    print('Error: debes introducir en ambos campos un numero')
