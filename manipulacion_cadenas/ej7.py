"""
Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.    
"""

letra = input("Introduce cadena: ")
palabra = input("Introduce palabra a ser sustituida: ")
new_palabra = input("Introduce palabra que se sustituirá: ")
letra_cambiada = ""
for i in letra:
    if palabra == i:
      letra_cambiada += new_palabra
    else:
        letra_cambiada += i
print(letra_cambiada)