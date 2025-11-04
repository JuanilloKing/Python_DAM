"""
Escriba un programa que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado (switch).
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente    
"""
nota = int(input("Introduce una nota numérica entre 0 y 10: "))
if nota < 0 or nota > 10:
    print("Nota introducida no valida")
if nota >= 0 and nota < 3:
    print("Muy deficiente")
if nota >= 3 and nota < 5:
    print("Insuficiente")
if nota >= 5 and nota < 6:
    print("Suficiente")
if nota >= 6 and nota < 7:
    print("Bien")
if nota >= 7 and nota < 9:
    print("Notable")
if nota >= 9 and nota <= 10:
    print("Sobresaliente")
