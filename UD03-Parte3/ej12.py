"""
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos    
"""
from math import sqrt

x1 = int(input("Introduce valor x en el primero punto"))
y1 = int(input("Introduce valor y en el primero punto"))
x2 = int(input("Introduce valor x en el segundo punto"))
y2 = int(input("Introduce valor x en el segundo punto"))

distancia = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(distancia)
