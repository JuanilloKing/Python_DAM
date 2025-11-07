"""
Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra.
"""

compra = float(input("Introduce monto de compra: "))
dia_semana = input("¿Es martes o jueves? [SI/NO]")

if dia_semana.upper() == "SI":
    compra = compra * 0.85

print(f"Monto total de compra: {compra}")
