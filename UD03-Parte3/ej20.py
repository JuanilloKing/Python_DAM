"""
Algoritmo que pida dos números e indique si el primero es mayor que el segundo.
"""

x = int(input("Introduce un número: "))
y = int(input("Introduce otro número: "))
if x > y:
    print(f"{x} es mayor que {y}")
elif x < y:
    print(f"{y} es mayor que {x}")
else:
    print("Ambos son el mismo número")
