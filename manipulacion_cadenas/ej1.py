"""
Leer una cadena desde teclado y mostrarla carácter por carácter usando un ciclo for y el índice.    
"""

entrada = input("Introduce cadena: ")

for i in range(0, len(entrada)):
    print(entrada[i])
