"""
Programa que muestre los números desde el 1 hasta un número N que se introducirá por
teclado
"""

try:
    n = int(input("Introduce un numero: "))
    if n >= 0:
      for i in range(1, n + 1):
          print(i)
    else:
        for i in range(1, n - 1, -1):
            print(i)
except ValueError:
  print('Error: Debes introducir un numero')
