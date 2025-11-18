n = int(input("Introduce altura: "))

espacio_max = n + 1
acc = 1
while acc <= n:
    espacio = " " * (espacio_max - acc)
    if acc == 1:
        print(espacio + '*')
    else:
        print(espacio + '*' + ((acc - 2) * " ") + '*')
    acc += 1

while acc != 0:
    espacio = " " * (espacio_max - acc)
    if acc == 1:
        print(espacio + '*')
    else:
        print(espacio + '*' + ((acc - 2) * " ") + '*')
    acc -= 1
