"""
Uso de bucles en Python
bucle for y bucle while
uso de pass, break y continue
Cuando se ocupa: 
- El (pass) se usa para indicar que no se va a ejecutar ninguna acción en ese bloque de código.
- El (break) se usa para salir de un bucle antes de que termine su ciclo.
- El (continue) se usa para saltar a la siguiente iteración del bucle.
"""

# ejemplo de lectura 1):
# ejempplo de Pass
# range = cantidad de veces que se va a repetir el bucle
# i = al iterador del bucle

# for i in range(5):
#     if i == 3:
#         pass  # No se hace nada cuando i es 3
#     else:
#         print(f"Iteración {i}")


# ejemplo de lectura 2):
# ejemplo de Break
# for i in range(5):
#     if i == 3:
#         break  # Sale del bucle cuando i es 3
#     print(f"Iteración {i}")

# ejemplo de lectura 3):
# ejemplo de Continue
# for i in range(5):
#     if i == 3:
#         continue  # Salta a la siguiente iteración cuando i es 3
#     print(f"Iteración {i}")

lista_pares =[]
lista_impares =[]

for i in range(0, 101, 5):
                # inicio, fin, paso
    if i % 2 == 0:
        lista_pares.append(i)
        continue
    else:
        lista_impares.append(i)
        pass

print("Números pares:", lista_pares)
print("Números impares:", lista_impares)
