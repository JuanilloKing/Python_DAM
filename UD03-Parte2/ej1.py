"""
Programa que muestre por pantalla los 20 primeros números naturales (1, 2, 3,…., 20)    
"""

for i in range(1, 21):
    if i != 20:
        print(f"{i} , ",end="")
    else:
        print(i, end=" ")
