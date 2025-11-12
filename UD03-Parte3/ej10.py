"""
Un alumno desea saber cuál será su calificación final en la materia de Algoritmos Dicha
calificación se compone de los siguientes porcentajes:
• 55% del promedio de sus tres calificaciones parciales.
• 30% de la calificación del examen final.
• 15% de la calificación de un trabajo final.
"""

parcial1 = ((float(input("Nota primer parcial: "))) * 0.55) / 3
parcial2 = (float(input("Nota segundo parcial: ")) * 0.55) / 3
parcial3 = (float(input("Nota tercer parcial: ")) * 0.55) / 3

examen = float(input("Nota examen: ")) * 0.30
trabajo = float(input("Nota trabajo: ")) * 0.15

total_nota = parcial1 + parcial2 + parcial3 + examen + trabajo

print(f"Total nota: {total_nota}")