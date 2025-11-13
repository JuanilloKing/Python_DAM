"""
Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una
distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para
ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto
determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.    
"""

try:
    d = float(input("Introduce la distancia entre vehículos (km): "))
    v_delantero = float(
        input("Introduce la velocidad del vehículo delantero (el lento, km/h): "))
    v_trasero = float(
        input("Introduce la velocidad del vehículo trasero (el rápido, km/h): "))

    if v_trasero <= v_delantero:
        print(
            "\nError: La velocidad del vehículo trasero no es mayor que la del delantero.")

    elif d < 0 or v_delantero < 0 or v_trasero < 0:
        print("\nError: Las distancias y velocidades deben ser números positivos.")

    else:
        velocidad_relativa = v_trasero - v_delantero

        tiempo_en_horas = d / velocidad_relativa

        tiempo_en_minutos = tiempo_en_horas * 60

        print(f"Resultado:")
        print(
            f"El vehículo trasero alcanzará al delantero en {tiempo_en_minutos:.2f} minutos.")

except ValueError:
    print("\nError: Debes introducir valores numéricos válidos")
