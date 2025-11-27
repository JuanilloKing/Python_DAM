
n = int(input("Introduce tamaño del tablero [n * n]: "))
acc = 4
salida = 0
for _ in range(1, n + 1):
    while acc % 4 == 0:
        print(("***" + " " * 3) * n)
        salida += 1
        if salida == 3:
            acc = 1
            salida = 0
    else:
        print((" " * 3 + "***") * n)
    acc += 1
