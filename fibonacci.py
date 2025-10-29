"""
Ejercicio que muestra los 10 primeros digitos de fibonacci
"""

num = 1
num_anterior = 0
acc = 0
aux = 0
print(num_anterior)
print(num)

while acc < 8:
    aux = num + num_anterior
    num_anterior = num
    num = aux
    print(aux)
    acc += 1
