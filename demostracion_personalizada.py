"""
crea un codigo que me permita obtener la contraseña de un usuario en python utilizando bucles y condicionales

Entrada:
    - Pedir al usuario que ingrese la contraseña
    - crear una variable que guarde la contraseña correcta
Proceso:
    - buscar los numeros de forma aleatoria que existan en la contraseña correcta
    - agrupar los numeros encontrados en una lista
    - compar los numeros encontrados con la contraseña para poder ordenar los numeros de forma correcta
    - utilizar bucles para recorrer la lista de numeros encontrados
    - utilizar condicionales para verificar si los numeros encontrados coinciden con la contraseña correcta 
Salida:
    - Mostrar un mensaje indicando si la contraseña ingresada es correcta o incorrecta
"""
import random

password_correcto = input("Ingrese la contraseña correcta: ")
    # validamos que la contraseña tenga solo 4 digitos
while len(password_correcto) != 4 or not password_correcto.isdigit():
    password_correcto = input("Contraseña inválida. Ingrese una contraseña de 4 dígitos: ")

contador = 0
while True:
    numeros_encontrados = []
    for char in password_correcto:
        if random.choice([True, False]):
            numeros_encontrados.append(char)
    
    print(f"Números encontrados: {numeros_encontrados}")
    
    # Verificar si los números encontrados coinciden con la contraseña correcta
    if ''.join(numeros_encontrados) == password_correcto:
        print(f"se consiguio la contraseña en el intento número {contador + 1}")
        print("¡Contraseña correcta encontrada!")
        break
    else:
        print("Contraseña incorrecta. Intentando de nuevo...")
    
    contador += 1
    
    if contador >= 100:  # Limitar el número de intentos para evitar un bucle infinito
        print("No se pudo encontrar la contraseña después de varios intentos.")
        break