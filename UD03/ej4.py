x = int(input("Introduce un numero: "))
y = int(input("Introduce otro numero: "))

if y != 0:
    suma = x + y
    resta = x - y
    producto = x * y
    division = x / y
    print(f"Suma: {suma} \nResta: {resta} \nProducto: {producto} \nDivision: {division} \n")
else:
    print("No podemos hacer una division entre 0, elija otro numero")