dinero = 1000
flag = True
while flag:
    print("*-----------------------------*")
    print("Bienvenido a su cajero Virtual")
    print(f"Saldo total actual: {dinero}")
    opcion = int(input("Opciones: \n1-Ingresar dinero a su cuenta \n2-Retirar dinero de la cuenta \n3-Salir\n"))
    print(" ")
    if opcion < 1 and opcion > 3:
      print("Opcion incorrecta, elija una de las tres opciones dadas")
      print("")
    if opcion == 1:
      aniadir_dinero = int(input("Dime el dinero que desea introducir: "))
      dinero +=aniadir_dinero
      print(f"Has añadido {aniadir_dinero}, ahora tienes en la cuenta {dinero}")
    if opcion == 2:
        retirar_dinero = int(input("Dime el dinero que desea retirar: "))
        if retirar_dinero > dinero:
          print("No hay saldo suficiente")
        else:
            dinero -=retirar_dinero
            print(f"Has retirado {retirar_dinero}, ahora tienes en la cuenta {dinero}")
    if opcion == 3:
      flag = False
