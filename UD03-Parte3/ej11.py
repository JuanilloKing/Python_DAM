"""
Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo.   
"""

x = int(input("Introduce un número: "))
y = int(input("Introduce otro número: "))

if x >= y:
    resultado = x - y
else:
    resultado = y - x
