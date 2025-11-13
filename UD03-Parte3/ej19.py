"""
Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por
cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime
el resultado obtenido por el estudiante.
"""

correctas = int(input("Numero de respuestas correctas: "))
incorrectas = int(input("Numero de respuestas incorrectas: "))
blanco = int(input("Numero de respuestas en blanco: "))
nota = 0

for _ in range(1, correctas + 1):
    nota += 5
for _ in range(1, incorrectas + 1):
    if nota == 0:
        nota = 0
    nota -= 1
print(f"Tu nota es un {nota}")
