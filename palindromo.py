"""
Dada una palabra o frase, di si es un palíndromo o no (se leen igual al derecho, que al reves)    
"""


def palindromo(frase):
    frase_trimeada = frase.lower().replace(" ", "")
    f = -1
    es_palindromo = True
    for palabra in frase_trimeada:
        if palabra != frase_trimeada[f]:
            es_palindromo = False
            break
        f -= 1
    return es_palindromo


print(palindromo("Dabale arroz a la zorra el abad"))
print(palindromo("hola"))
print(palindromo("luz azul"))
