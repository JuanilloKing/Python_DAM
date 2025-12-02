"""
Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.    
"""

vocales = "aeiouAEIOU"
palabra = "hola edu"
palabra_nueva = ""

for i in palabra:
    palabra_nueva += i
    if i in vocales:
        palabra_nueva += i

print(palabra_nueva)
