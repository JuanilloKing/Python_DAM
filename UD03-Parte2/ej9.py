"""
Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos.
"""

positivos = 0
negativos = 0

n = int(input("Introduce un numero: "))

while n != 0:
    if n < 0:
        negativos -= 1
    else:
        positivos += 1
    n = int(input("Introduce otro número: "))

print(f"Positivos: {positivos} \nNegativos: {negativos}")
