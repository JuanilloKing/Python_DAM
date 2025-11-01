"""
    hola
"""
precio_articulo = float(input("Dime precio articulo real: "))
precio_venta = float(input("Precio de venta: "))

if precio_venta < precio_articulo:
    descuento = ((precio_articulo - precio_venta) / precio_articulo) * 100
    print(f"Te han descontado un {descuento}%")
else:
    print("Me estas intentando timar, esto cuesta mas barato")