import random
def acierta_numero():
    numero = random.randint(1,100)
    intentos = 0
    while True:
        print("--------------------------------------------------")
        print("Bienvenido a el juego de intentar adivinar mi numero!")
        intento = int(input("Dime un numero entre 1 y 100, y te dire si acertaste: "))
        intentos += 1
        if intento > numero:
            if intento - numero > 10:
                print("Tu numero es muy alto")
            if intento - numero <= 10 :
                print("Tu numero es un poquito alto")
        else:
            if numero - intento >10:
                print("Tu numero es muy bajo")
            if numero - intento <= 10 :
                print("Tu numero es un poquito bajo")
        if intento == numero:
            print(f"Has acertado!! Enhorabuena, solo te ha costado {intentos} intentos")
            return

acierta_numero()
