"""
Dibuja un ordinograma de un programa que lea un número positivo N y calcule y visualice
su factorial N! siendo el factorial   
"""

def factorial(n):
    if n < 0:
        return "Error: Factorial no puede ser negativo"
    
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    
    for i in range(2, n + 1):
        resultado *= i
        
    return resultado

numero = 5
resultado_final = factorial(numero)

print(f"El factorial de {numero} es: {resultado_final}")
