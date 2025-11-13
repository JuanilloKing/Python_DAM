"""
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar qué tipo de triángulo es, teniendo en
cuenta:
• Si se cumple Pitágoras entonces es triángulo rectángulo
• Si sólo dos lados del triángulo son iguales entonces es isósceles.
• Si los 3 lados son iguales entonces es equilátero.
• Si no se cumple ninguna de las condiciones anteriores, es escaleno.   
"""

import math

try:
    A = float(input("Lado A: "))
    B = float(input("Lado B: "))
    C = float(input("Lado C: "))
except ValueError:
    print("Error: Debes introducir valores numéricos.")
    exit()

if (A + B <= C) or (A + C <= B) or (B + C <= A) or (A <= 0 or B <= 0 or C <= 0):
    print(f"\nLos lados {A}, {B} y {C} NO pueden formar un triángulo.")
else:
    print(f"\nAnalizando el triángulo con lados {A}, {B}, {C}:")
    lados = sorted([A, B, C])
    c1 = lados[0]
    c2 = lados[1]
    h = lados[2]

    es_rectangulo = math.isclose(c1**2 + c2**2, h**2)

    es_equilatero = (A == B) and (B == C)

    es_isosceles = (A == B or B == C or A == C) and not es_equilatero

    tipo_triangulo = ""

    if es_rectangulo:
        tipo_triangulo = "RECTÁNGULO"

    elif es_isosceles:
        tipo_triangulo = "ISÓSCELES"

    elif es_equilatero:
        tipo_triangulo = "EQUILÁTERO"

    else:
        tipo_triangulo = "ESCALENO"

    print(f"El triángulo es: {tipo_triangulo}")
