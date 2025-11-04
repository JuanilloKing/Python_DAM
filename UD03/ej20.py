nota = int(input("Introduce una nota numérica entre 0 y 10: "))
if nota < 0 or nota > 10:
    print("Nota introducida no valida")
if nota >= 0 and nota < 3:
    print("Muy deficiente")
if nota >= 3 and nota < 5:
    print("Insuficiente")
if nota >= 5 and nota < 6:
    print("Suficiente")
if nota >= 6 and nota < 7:
    print("Bien")
if nota >= 7 and nota < 9:
    print("Notable")
if nota >= 9 and nota <= 10:
    print("Sobresaliente")
