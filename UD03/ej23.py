"""
Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra.
"""

compra = float(input("Introduce el valor de compra: "))
flag = True
while flag:
    tipo_pago = int(
        input("Tipo pago: CONTADO-> escriba: 1, TARJETA-> escriba 2 \n"))
    if tipo_pago == 1:
        compra = compra * 0.95
        flag = False
    if tipo_pago == 2:
        compra = compra * 1.03
        flag = False
    if tipo_pago != 1 and tipo_pago != 2:
        print("Error al especificar tipo de pago, vuelve a escribirlo.")
    else:
        print(f"Total a pagar: {compra}")
