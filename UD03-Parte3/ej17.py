"""
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de
viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora
de llegada a la ciudad B.
"""

try:
    hh = int(input("Hora de salida (HH): "))
    mm = int(input("Minutos de salida (MM): "))
    ss = int(input("Segundos de salida (SS): "))

    tiempo = int(input("Tiempo de viaje (T en segundos): "))

    if not (0 <= hh <= 23 and 0 <= mm <= 59 and 0 <= ss <= 59 and tiempo >= 0):
        print("\nError: Los valores de tiempo introducidos no son válidos.")
    else:
        segundos_salida = (hh * 3600) + (mm * 60) + ss
        segundos_llegada_totales = segundos_salida + tiempo
        segundos_del_dia_llegada = segundos_llegada_totales % 86400
        hh_llegada = segundos_del_dia_llegada // 3600
        segundos_restantes = segundos_del_dia_llegada % 3600

        mm_llegada = segundos_restantes // 60
        ss_llegada = segundos_restantes % 60

        print(
            f"La hora de llegada a la ciudad B será: {hh_llegada:02}:{mm_llegada:02}:{ss_llegada:02}")

except ValueError:
    print("\nError: Debes introducir únicamente números válidos.")
