"""
Imprime una estrella de ocho puntas combinando líneas verticales, horizontales y diagonales con asteriscos en una matriz de tamaño impar n x n (ej. 9x9).    
"""

n = int(input("Introduce  tamaño estrella: "))

if n % 2 == 0:
    print("Por favor, introduce un número impar.")
else:
    medio = n // 2

    for i in range(n):
        for j in range(n):
            if (j == medio or i == j or i + j == n - 1):
                print("*", end="")
            elif (i == medio):
                print("*" * 2, end="")
            else:
                print(" ", end=" ")
        print()
