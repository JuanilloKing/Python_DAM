"""
Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos
la altura de la pirámide por teclado. Este es un ejemplo    
"""

n = int(input("Introduce de cuanta altura quieres la escalera de asteríscos:"))
espacios = 0
acc = 1
for _ in range(1, n):
    acc += 2
for _ in range(1, n + 1):
    print(" " * espacios + "*" * acc + " " * espacios)
    acc -= 2
    espacios += 1
