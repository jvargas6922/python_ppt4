"""
Optimizacion de ciclos
"""
# Forma no optimizada
# cuadrados = []
# for i in range(1, 11):
#     cuadrados.append(i ** 2)
# print(cuadrados)


# Forma optimizada usando comprensión de listas
cuadrados_opt = [i ** 2 for i in range(1, 11)]
print(cuadrados_opt)

