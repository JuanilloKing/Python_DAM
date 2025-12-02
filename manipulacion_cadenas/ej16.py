"""
Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo).    
"""

cadena1 = "hola"
cadena2 = "manteca"
cadena_sumada = ""

for i in range(1, (len(cadena1)) + 1):
    cadena_sumada += cadena1[i - 1]

for i in range(1, (len(cadena2)) + 1):
    cadena_sumada += cadena2[i - 1]

print(cadena_sumada)
