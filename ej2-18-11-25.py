"""
Ejercicio de clase figura    
"""

n = int(input("Introduce de cuanto quieres la escalera: "))
s = str(n)
for i in range(1, n + 1):
    if i == 1:
        print(s)
    else:
        i = i - 2
        print(s + (' ' * i) + s)
print(n * s + s)
