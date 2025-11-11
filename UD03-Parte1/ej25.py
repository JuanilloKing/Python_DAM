"""
La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el matricula, la mensualidad, el IGV 18% (matricula + mensualidad) y el monto final a pagar. (Use el
control switch)
"""

nombre = input("Ingrese nombre postulante: ")
facultad = (input("Ingrese facultad a estudiar: ")).lower()

match facultad:
    case "ingenieria de sistemas":
        matricula = 350
        mensualidad = 650
        IGV = (matricula + mensualidad) * 0.18
    case "derecho":
        matricula = 300
        mensualidad = 550
        IGV = (matricula + mensualidad) * 0.18
    case "ingenieria naviera":
        matricula = 300
        mensualidad = 500
        IGV = (matricula + mensualidad) * 0.18
    case "ingenieria pesquera":
        matricula = 310
        mensualidad = 460
        IGV = (matricula + mensualidad) * 0.18
    case "contabilidad":
        matricula = 280
        mensualidad = 490
        IGV = (matricula + mensualidad) * 0.18
    case "administracion":
        matricula = 360
        mensualidad = 520
        IGV = (matricula + mensualidad) * 0.18
    case _:
        print("No tenemos registrado esa facultad")

print(f"Tu nombre {nombre}")
print(f"Facultad: {facultad}")
print(f"Importe: {matricula}")
print(f"Mensualidad: {mensualidad:.2f}")
print(f"IGV: {IGV}")
print(f"Monto final a pagar: {matricula + IGV + (mensualidad * 12)}")