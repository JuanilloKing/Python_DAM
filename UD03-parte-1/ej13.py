"""
Escriba un programa que lea dos números y lo visualiza en orden ascendente  
"""
x = int(input("Introduce un numero: "))
y = int(input("Introduce otro numero: "))

if x > y:
  print(f"Ordenado de manera ascendete: {y},{x}")

if y > x:
    print(f"Ordenado de manera ascendete: {x},{y}")

if x == y:
    print("Son iguales")
