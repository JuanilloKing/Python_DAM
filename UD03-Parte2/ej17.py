"""
Programa que suma independientemente los pares y los impares de los números
comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas    
"""
suma_par = 0
suma_impar = 0
for i in range(100, 201):
    if i % 2 == 0:
      suma_par += i
    else:
        suma_impar += i
print(f"Suma par: {suma_par} \nSuma impar: {suma_impar}")