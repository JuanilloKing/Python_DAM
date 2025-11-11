"""
Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de
la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura. 
"""

n = int(input("Introduce de cuanta altura quieres la escalera de asteríscos:"))
acc = 1
while acc <= n:
    print("*" * acc)
    acc += 1