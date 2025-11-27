"""
Enunciado:

Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.    
"""

n = int(input("Introduce de cuanta altura quieres la escalera de asteríscos:"))
espacios = n
acc = 1

for _ in range(1, n):
    print(" " * espacios + "*" * acc)
    acc += 2
    espacios -= 1

for _ in range(n, 0, -1):
    print(" " * espacios + "*" * acc)
    acc -= 2
    espacios += 1