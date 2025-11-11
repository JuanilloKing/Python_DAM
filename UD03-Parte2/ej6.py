"""
Programa que lea un número positivo N y calcule y visualice su factorial N! Siendo el
factorial:
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2* 1
N! = N * (N-1) * (N-2) * … *
"""

n = int(input("Introduce numero positivo: "))
if n < 0:
  print("Error, el numero debe ser mayor a cero")
else:
    if n == 0:
        print(0)
    if n == 1:
        print(1)
    acc = 1
    while n != 0:
      acc *= n
      n -= 1
    print(acc)