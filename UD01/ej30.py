"""
Dibuja un ordinograma de un programa que dada una cantidad de euros que el usuario
introduce por teclado (múltiplo de 5 €) mostrará los billetes de cada tipo que serán necesarios
para alcanzar dicha cantidad (utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar
el mínimo de billetes posible. Por ejemplo, si el usuario introduce 145 el programa indicará que
será necesario 1 billete de 100 €, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo
29 billetes de 5, que aunque sume 145 € no es el mínimo número de billetes posible).
"""

flag = True
billete500 = 0
billete200 = 0
billete100 = 0
billete50 = 0
billete20 = 0
billete10 = 0
billete5 = 0

while flag:
    money = int(input("Introduce la cantidad de billetes: "))
    if money % 5 == 0:
        while money >= 500:
            billete500 += 1
            money -= 500
        while money >= 200:
            billete200 += 1
            money -= 200
        while money >= 100:
            billete100 += 1
            money -= 100
        while money >= 50:
            billete50 += 1
            money -= 50
        while money >= 20:
            billete20 += 1
            money -= 20
        while money >= 10:
            billete10 += 1
            money -= 10
        while money >= 5:
            billete5 += 1
            money -= 5

        flag = False
        print(f"Numero de billetes de 500: {billete500}")
        print(f"Numero de billetes de 200: {billete200}")
        print(f"Numero de billetes de 100: {billete100}")
        print(f"Numero de billetes de 50: {billete50}")
        print(f"Numero de billetes de 20: {billete20}")
        print(f"Numero de billetes de 10: {billete10}")
        print(f"Numero de billetes de 5: {billete5}")
    else:
        print("Error, has introducido otra cosa que no son billetes")
