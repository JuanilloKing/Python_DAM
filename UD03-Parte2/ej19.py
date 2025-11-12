"""
Programa donde el usuario “piensa” un número del 1 al 100
y el ordenador intenta adivinarlo. Es decir, el ordenador irá proponiendo números una y otra
vez hasta adivinarlo (El usuario deberá indicarlo al ordenador si es mayor o menor o igual al
número pensado).    
"""

flag = True
num = 50

while flag:
    pregunta = input(f"Tu numero es {num} ? [SI/MENOR/MAYOR]: ").upper()
    if pregunta == "SI":
        print("ACERTASTE!")
        flag = False
    if pregunta == "MENOR":
        num -= 1
    if pregunta == "MAYOR":
        num += 1
