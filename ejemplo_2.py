"""
Uso del While
se ocupa cuando no sabemos la cantidad de iteraciones.
Elbucle while se ejecuta mientras una condición sea verdadera.

- Crea un programa que me permita poder competir con la computadora para poder elejir el numero más alto de 10 elementos.
Cuando la computadora gane me restara un punto de vida en caso contrario yo le restare un punto de vida a la computadora.

El programa se ejecutara mientras alguno de los dos tenga puntos de vida.

"""
"""
Entrada:
    - creamos los jugagores.
    - asignamos los puntos de vida a los jugadores.
    - solicitar al usuario que ingrese un numero del 1 al 10
Proceso:
    - realizar la comparacion entre los numeros.
    - restar puntos de vida al jugador que pierda.
    - repetir el proceso mientras alguno de los dos tenga puntos de vida.
Salida:
    - mostrar el ganador.
"""
import random

vida_jugador = 3
vida_computadora = 3
opciones_jugador =[]
opciones_computadora =[]

while vida_jugador > 0 and vida_computadora > 0:
    numero_jugador = int(input("Ingresa un número del 1 al 10: "))
    numero_computadora = random.randint(1, 10)
    # verificamos que las opciones del jugador o el usuario no se repitan
    # validacion de usuario
    while numero_jugador in opciones_jugador:
        print("Ya elegiste ese número. Por favor, elige otro.")
        numero_jugador = int(input("Ingresa un número del 1 al 10: "))
    opciones_jugador.append(numero_jugador)
    # validacion de computadora
    while numero_computadora in opciones_computadora:
        numero_computadora = random.randint(1, 10)
    opciones_computadora.append(numero_computadora)
    print(f"opciones jugador: {opciones_jugador}")
    print(f"opciones computadora: {opciones_computadora}")
    print("----------------------------------------------")
    print(f"Numero del jugador: {numero_jugador}")
    print(f"Numero de la computadora: {numero_computadora}")
    print("----------------------------------------------")
    if numero_jugador > numero_computadora:
        vida_computadora -= 1
        print("¡Ganaste esta ronda!")
    elif numero_jugador == numero_computadora:
        print("¡Empate! No se resta vida a ninguno.")
    else:
        vida_jugador -= 1
        print("¡La computadora ganó esta ronda!")
    print(f"Vida del jugador: {vida_jugador}")
    print(f"Vida de la computadora: {vida_computadora}")
    print("----------------------------------------------")

if vida_jugador > 0:
    print("¡Felicidades! Ganaste el juego.")
else:
    print("La computadora ganó el juego. ¡Inténtalo de nuevo!")