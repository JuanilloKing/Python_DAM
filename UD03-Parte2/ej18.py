"""
Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla.    
"""

a = int(input("Introduzca numero: "))
b = int(input("Introduzca potencia: "))
res = 1
for _ in range(1, b + 1):
    res *= a
print(f"{a} elevado a {b} da como resultado: {res}")