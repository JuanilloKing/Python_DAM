"""
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales. Mostramos las
Iniciales en Mayúsculas sí o sí.    
"""

nombre = input("Introduce tu nombre: ")
apellido1 = input("Introduce tu primer apellido: ")
apellido2 = input("Introduce segundo apellido: ")

print(
    f"INICIALES: {(nombre[0]).upper()}{(apellido1[0]).upper()}{(apellido2[0]).upper()}")
