"""
Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.    
"""

cadena = input("Introduce una cadena: ")

caracter = input("Introduce caracter que deseas buscar: ")

acc = 0

for i in range(0, len(cadena)):
    if cadena[i].lower() == caracter.lower():
        acc += 1

print(f"He encontrado ese caracter {acc} veces")
