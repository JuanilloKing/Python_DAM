"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
"""

cadena = input("Introduce una cadena: ")
mayuscula = False
for palabra in cadena:
    if palabra.isupper():
        mayuscula = True

if mayuscula:
    print("He encontrado alguna mayuscula")
else:
    print("No habia ninguna mayuscula")
