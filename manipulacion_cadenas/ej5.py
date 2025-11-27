"""
Verificar si en una cadena específica está algun caracter en otra cadena con un ciclo y comparaciones.    
"""

cadena1 = input("Introduce cadena: ")
cadena2 = input("Introduce otra cadena: ")
flag = False
acc = 0
while len(cadena1) > acc:
    if cadena2.find(cadena1[acc].lower()):
        flag = True
        break
    acc += 1

if flag:
    print(f"Hemos encontrado dicho caracter")
else:
    print("No hemos encontrado el caracter")
