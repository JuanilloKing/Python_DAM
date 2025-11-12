"""
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius    
"""

grados_fah = float(input("Introduce grados fahrenheit: "))

grados_cel = (grados_fah - 32) / 1.8

print(f"{grados_cel:.2f}")