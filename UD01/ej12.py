"""
Dibuja un ordinograma de un programa que muestre los números pares comprendidos
entre el 1 y el 200. Esta vez utiliza un contador sumando de 1 en 1.    
"""

acc = 0
while acc <= 200:
    if acc % 2 == 0:
      print(acc)
    acc += 1
