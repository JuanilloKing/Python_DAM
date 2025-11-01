import math

long_radio = int(input("Introduce longitud radio: "))
diametro = long_radio * 2
radio = diametro / 2
long_circunferencia = math.pi * diametro
area_circulo = math.pi * radio ** 2
volumen = 4 / 3 * math.pi * radio ** 3
print(f"Longitud circunferencia: {long_circunferencia:.2f} \nArea circulo: {area_circulo:.2f} \nVolumen: {volumen:.2f}")
