x = int(input("Introduce un numero: "))
y = int(input("Introduce otro numero: "))

if x > y:
    print(f"El mayor entre {x} y {y} es {x}")

if y > x:
    print(f"El mayor entre {x} y {y} es {y}")

if x == y:
    print("Son iguales")
