"""
Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.    
"""

n = int(input("Introduce altura: "))

for i in range(1, n):
    if i == 1:
        print(((n) * " ") + "*")
    print(((n - i) * " ") + "*" + i * " " + ((i - 1) * " ") + "*")


for i in range(n, 1, -1):
    if i == 2:
        print(((n) * " ") + "*")
    else:
        print(((n - i + 2) * " ") + "*" + (i - 3)
              * " " + ((i - 2) * " ") + "*")
