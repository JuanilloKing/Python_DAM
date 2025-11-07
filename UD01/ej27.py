"""
Escribe un programa que lea una secuencia de notas (con valores que
van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10    
"""

flag = True
notaza = False
while flag:
    try:
        nota = int(input("Introduce una nota [0-10]: "))
        if nota == -1:
            flag = False
        if nota < 0 or nota > 10:
            raise ValueError
        if nota == 10:
            notaza = True
    except ValueError:
        flag = False
        print('Las notas no pueden ser numeros que no sean [0- 10]')

if notaza:
    print("Ha habido alguna nota con valor 10")
else:
    print("No ha habido ningun 10")
