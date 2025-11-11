"""
Programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos
son positivos y cuantos negativos.    
"""

positivos = 0
negativos = 0

for _ in range(1, 101):
    n = int(input("Introduce un numero: "))
    if n < 0:
        negativos += 1
    else:
        positivos += 1

print(f"Hay {positivos} numeros positivos y {negativos} numeros negativos")
