"""
Leer una cadena y contar cuántos caracteres son letras mayúsculas.
"""

mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
palabra = "Hola Edu"
acc = 0
for i in palabra:
    if i in mayusculas:
        acc += 1
print(acc)
