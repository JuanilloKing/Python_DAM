"""
En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
Si los tres dados son seis, mostrar el mensaje “Excelente”
Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
Si un dado se obtiene seis, mostrar el mensaje “Regular”
Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”    
"""
import random
aciertos = 0
for _ in range(1, 3):
    dado = random.randint(1, 6)
    if dado == 6:
        aciertos += 1

match aciertos:
    case 0:
        print("Pésimo")
    case 1:
        print("Regular")
    case 2:
        print("Muy bien")
    case 3:
        print("Excelente")
