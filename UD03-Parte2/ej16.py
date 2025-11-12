"""
Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con
el valor -1 y nos dice si hubo o no alguna nota con valor 10    
"""

flag = True
notaza = False
while flag:
  try:
    nota = int(input("Introduce una nota[-1 si quieres salir]: "))
    if nota == 10:
      notaza = True
    if nota == -1:
      flag = False
  except:
    print('Error: Debes introducir una nota')
if notaza:
  print("Hubo algun 10 por ahí")
else:
    print("Nadie saco un 10 :(")