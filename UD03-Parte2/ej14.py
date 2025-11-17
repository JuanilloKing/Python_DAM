"""
Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura    
"""

n = int(input("Introduce de cuanta altura quieres la escalera de asteríscos:"))
espacios = n
acc = 1
for _ in range(1, n + 1):
    print(" " * espacios + "*" * acc)
    acc += 2
    espacios -= 1
