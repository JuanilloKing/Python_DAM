x = int(input("Introduce el primer número: "))
y = int(input("Introduce el segundo número: "))
z = int(input("Introduce el tercer número: "))
print("*-------------------------------------*")

numeros = [x, y, z]

numeros_ordenados = sorted(numeros, reverse=True)

mayor = numeros_ordenados[0]
menor = numeros_ordenados[2]

conteo_mayor = numeros_ordenados.count(mayor)

if conteo_mayor == 1:
    print(f"El número mayor es: {mayor}")
else:
    print(f"El número mayor es: {mayor}, repetido {conteo_mayor} veces.")

if conteo_mayor != 3:

    medio = numeros_ordenados[1]

    if medio != mayor:
        conteo_medio = numeros_ordenados.count(medio)

        if conteo_medio == 1:
            print(f"El número intermedio es: {medio}")
        elif conteo_medio == 2:
            print(
                f"El número intermedio/pequeño es: {medio}, repetido 2 veces.")

if menor != mayor:
    conteo_menor = numeros_ordenados.count(menor)

    if menor != medio:
        print(f"El número más pequeño es: {menor}")

print(
    f"Ordenados de mayor a menor: {numeros_ordenados[0]}, {numeros_ordenados[1]}, {numeros_ordenados[2]}")
