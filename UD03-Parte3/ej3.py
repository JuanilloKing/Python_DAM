"""
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa    
"""
from math import sqrt

cateto1 = float(input("Introduce un cateto: "))
cateto2 = float(input("Introduce otro cateto: "))

hipotenusa = sqrt((cateto1 ** 2) + (cateto2 ** 2))

print(f"{hipotenusa:.2f}")