"""
Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún
número negativo o no    
"""

negativo = False
for _ in range(1, 101):
    n = int(input("Introduce numero: "))
    if n < 0:
      negativo = True
