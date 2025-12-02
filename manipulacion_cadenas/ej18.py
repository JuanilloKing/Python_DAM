"""
Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación).
"""

cadena = "hola que tal estas"
cadena_consonantes = ""

for i in range(len(cadena)):
    if cadena[i] not in "aeiouAEIOU":
        cadena_consonantes += cadena[i]
print(cadena_consonantes)

