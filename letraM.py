"""
Imprime la letra M mayúscula usando asteriscos en una matriz
cuadrada de tamaño impar n. Las líneas de la M deben visualizarse usando asteriscos, con espacios en el resto.    
"""

n = int(input("Introduce numero impar para hacer la letra M: "))
acc = n - 2
acum = acc
z = (n - 2) // 2
if n % 2 == 0:
    print("Has introducido un numero par, no puedo hacerlo")
else:
    for i in range(n):
        if i == 0:
            print('*' + " " * acc + "*")
            acc -= 2
        elif acc > 0:
            print('*' + " " * (i - 1) + '*' + " " *
                  acc + '*' + (i - 1) * " " + '*')
            acc -= 2
        elif acc < 0:
            print('*' + " " * z + '*' + " " * z + '*')
            acc = 0
        elif acc == 0:
            print('*' + " " * acum + "*")
