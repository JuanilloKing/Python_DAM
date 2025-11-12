"""
Calcular el perímetro y área de un rectángulo dada su base y su altura    
"""

base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))

perimetro = 2 * base + 2 * altura
area = base * altura
print(f"Área: {area}, perimetro: {perimetro}")
