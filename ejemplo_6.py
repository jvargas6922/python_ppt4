"""
Realice un programa que me permita escribir las tablas de multiplicar del 1 al 10
"""

for i in range(1, 11): # llega de un servicio (API)
    # print(f"Elemetos de mi bucle externo: {i}")
    print(f"Tabla del {i}")
    for j in range(1, 11): # llega de otra fuente (Base de datos)
        print(f"{i} X {j} = { i * j}")
    print("--------------")
    print("\n")