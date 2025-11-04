"""
Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de
10.    
"""
n = int(input("Introduce un numero y te diré si es multiplo de 10: "))
if n % 10 == 0:
    print("Es multiplo de 10")
else:
    print("No es multiplo de 10")
