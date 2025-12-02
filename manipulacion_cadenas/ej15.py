"""
Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.    
"""

cadena = "hola que Adios"
vocales = "aeiouAEIOU"
cadena_nueva = ""
for i in cadena:
    if i in vocales:
        cadena_nueva += "*"
    else:
        cadena_nueva += i
print(cadena_nueva)