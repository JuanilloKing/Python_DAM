"""
Escriba un programa que recibe como datos de entrada una hora expresada en horas,
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
transcurrido un segundo
"""

hora = int(input("Introduce la hora (0-23): "))
minutos = int(input("Introduce los minutos (0-59): "))
segundos = int(input("Introduce los segundos (0-59): "))

segundos += 1
if segundos >= 60:
    segundos = 0
    minutos += 1
    if minutos >= 60:
        minutos = 0
        hora += 1        
        if hora >= 24:
            hora = 0
print(f"Hora transcurrido 1 segundo: {hora:02d}:{minutos:02d}:{segundos:02d}")
