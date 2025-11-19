"""
La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los
siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo
minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día,
en turno de mañana, 15 %, y en turno de tarde, 10 %.
Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona
que realiza una llamada
"""

tiempo = int(
    input("Introduce el numero de minutos que has estado en llamada: "))
semana = input("¿Es Domingo? [SI/NO] ")

pagar = 0
while tiempo != 0:
    if tiempo >= 10:
        pagar += 0.50
    if tiempo >= 8 and tiempo < 10:
        pagar += 0.70
    if tiempo > 5 and tiempo < 8:
        pagar += 0.80
    if tiempo <= 5:
        pagar += 1
    tiempo -= 1

if semana.upper() == "NO":
    horario = input("Es horario de mañana o de tarde? [MAÑANA/TARDE] ")
    if horario.upper() == "MAÑANA":
        pagar *= 1.15
        print(f"Debes pagar {pagar:.2f} €")
    elif horario.upper() == "TARDE":
        pagar *= 1.10
        print(f"Debes pagar {pagar:.2f} €")
    else:
        print("no te he entendido")
elif semana.upper() == "SI":
    pagar *= 1.03
    print(f"Debes pagar {pagar:.2f} €")
