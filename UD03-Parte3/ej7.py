"""
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas
horas y minutos corresponde    
"""

min = int(input("Introduce número de minutos: "))
horas = 0
while min >= 60:
    horas += 1
    min -= 60

print(f"Horas: {horas}, minutos: {min}")