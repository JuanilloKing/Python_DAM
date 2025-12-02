"""
Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez.    
"""

cadena = "La gata es mio soy iy"
palabras_nuevas = ""
palabras_repetidas = ""

for i in range(len(cadena)):
    if cadena[i] not in palabras_nuevas:
        palabras_nuevas += cadena[i]
    elif cadena[i] not in palabras_repetidas:
        palabras_repetidas += cadena[i]

print("Palabras repetidas:" + palabras_repetidas)
