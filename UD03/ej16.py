try:
    entrada = int(
        (input("Introduce un numero entre 0 y 999.999 y te diré las cifras que tiene: ")))
    n = str(entrada)
    if len(n) <= 6 and len(n) >= 1:
        print(f"Tu número tiene {len(n)} cifras")
    else:
        print("Tu numero no está entre los valores [0-999.999]")
except:
    print('Debe ser un numero el valor introducido')
