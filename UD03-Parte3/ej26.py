"""
Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
• El exponente sea positivo, sólo tienes que imprimir la potencia.
• El exponente sea 0, el resultado es 1.
• El exponente sea negativo, el resultado es 1/potencia con el exponente positivo    
"""

a = int(input("Introduzca base: "))
b = int(input("Introduzca exponente: "))
res = 1
if b >= 0:
    b_contador = b
else:
    b_contador = -b

for _ in range(1, b_contador + 1):
    res *= a
if b >= 0:
    print(f"{a} elevado a {b} da como resultado: {res}")
else:
    print(f"{a} elevado a {b} da como resultado: {1 / res}")
