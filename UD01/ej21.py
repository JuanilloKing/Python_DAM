"""
Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje de si ha leído número negativo o no.
"""

negativo = False
for _ in range(1, 101):
    n = int(input("Introduce un numero: "))
    if n < 0:
        negativo = True

if negativo:
    print("Ha habido almenos 1 numero negativo")
else:
    print("Todos los numeros fueron positivos")
