"""
Leer una cadena y contar cuántas vocales contiene.    
"""

vocales = "aeiouAEIOU"
palabra = "hola edu"
acc = 0
for i in palabra:
    if i in vocales:
        acc += 1
print(acc)