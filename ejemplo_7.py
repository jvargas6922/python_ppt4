"""
realice un programa que me permita recorrer una matriz
"""

matriz = [[1,2,3],[4,5,6],[7,8,9]]
# lista =[  a    ,   b   ,   c   ]

contador = 0
for fila in matriz:
    # contador += 1
    # print(f"Fila {contador}: {fila} ")
    for elemento in fila:
        print(elemento, end=" ")
    print()