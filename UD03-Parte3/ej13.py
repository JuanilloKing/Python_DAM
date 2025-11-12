"""
Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se
puede calcular?    
"""
from math import sqrt
n = int(input("Introduce un número: "))

raiz_cuadrada = sqrt(n)
raiz_cubica = n ** (1/3)

print(f"Raiz cuadrada: {raiz_cuadrada}, raiz cubica: {raiz_cubica}")
