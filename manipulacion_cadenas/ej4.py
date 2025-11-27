"""
Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).    
"""

cadena = input("Introduce la cadena a invertir: ")
cadena_invertida = ""
for i in range(len(cadena) - 1, -1, -1):
    cadena_invertida += cadena[i]

print(cadena_invertida)
