"""
Crea una aplicación que dibuje una escalera de números, siendo cada línea un número.
Nosotros le pasamos la altura por teclado.    
"""

n = int(input("Introduce de cuanta altura quieres la escalera de numeros:"))
acc = 1
while acc <= n:
    for i in range(1, acc + 1):  
        print(i, end="")
        if i == acc:
          print(" ")
    acc += 1
