"""
Escriba un programa que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuesto son:
o Los primeros 500€ son libres de impuestos.
o Los siguientes 400€ tiene un 25% de impuesto.
o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto.    
"""

horas = int(input("Introduce el numero de horas trabajadas"))
tarifa_normal = 5
tarifa_especial = tarifa_normal * 1.5
contador = 0
if horas < 35:
    salario_bruto = horas * tarifa_normal
else:
    salario_bruto = 35 * tarifa_normal
    salario_bruto += (horas - 35) * tarifa_especial

if salario_bruto <= 500:
    salario_neto = salario_bruto
else:
    salario_neto = 500
    contador = salario_bruto - 500
    if contador >= 400:
        salario_neto += 400 * 0.75
        contador -= 400
    else:
        salario_neto += contador * 0.75
    if contador >= 0:
        salario_neto += contador * 0.55

print(
    f"Hechando {horas} horas, cobrarias {salario_bruto} en bruto, y {salario_neto} en neto")
