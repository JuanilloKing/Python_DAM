"""
Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.    
"""

numericos = "1234567890"

cadena = "Hola tengo 19 años"
acc = 0
for i in cadena:
    if i in numericos:
        acc += 1

print(acc)
