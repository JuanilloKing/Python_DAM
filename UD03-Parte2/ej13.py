"""
Crea una aplicación que dibuje una escalera de números, siendo cada línea números
empezando en uno y acabando en el numero de la línea. Este es un ejemplo, si introducimos un
5 como altura.   
"""

n = int(input("Introduce de cuanta altura quieres la escalera de numeros:"))
acc = 1
while acc <= n:
    for i in range(1, acc + 1):
        print(i, end="")
    print()
    acc += 1
