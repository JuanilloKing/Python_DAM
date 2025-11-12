"""
Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el
vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas
que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y
comisiones.   
"""

sueldo_base = int(input("Introduce tu suedo base: "))
ventas = 3
comisiones = sueldo_base * 0.3

print(f"Recibira por comisiones: {comisiones}, y el total será de: {sueldo_base + comisiones}")