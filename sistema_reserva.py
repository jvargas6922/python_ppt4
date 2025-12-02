"""
Sistema de Gestión de Reservas
Contexto:
    En este ejercicio, construiremos un sistema de gestión de reservas para un cine. El usuario podrá reservar
    boletos, seleccionar funciones y visualizar su resumen de compra. Se aplicarán ciclos while, for, y estructuras
    condicionales para manejar la lógica del sistema.
Consigna: 
    1. Mostrar una lista de películas disponibles con horarios. (listo)
    2. Permitir al usuario seleccionar una película y la cantidad de boletos.
    3. Validar la disponibilidad de boletos.
    4. Mostrar el resumen final con la película, el número de boletos y el precio total.
    5. Permitir nuevas reservas hasta que el usuario decida salir.
Paso a paso: 
    1) Definir un diccionario con películas y horarios.
    2) Usar un while para mostrar el menú y permitir que el usuario haga selecciones repetidas hasta que decida salir.
    3) Solicitar la película y la cantidad de boletos.
    4) Verificar disponibilidad de boletos antes de confirmar la compra.
    5) Calcular el precio total basado en la cantidad de boletos comprados.
    6) Permitir agregar más reservas o finalizar la compra.
    7) Mostrar un resumen final con todas las reservas realizadas y el costo total.
"""
# Lista de peliculas con su horario y disponibilidad
lista_horarios = ["18:00", "20:00", "16:30"]
peliculas = {
    "Avatar 2": {
        "horario": lista_horarios, # 18:00, 20:00, 16:30, etc
        "boletos_disponibles": 30
    },
    "Avengers Endgame": {
        "horario": lista_horarios, # 18:00, 20:00, 16:30, etc
        "boletos_disponibles": 25
    },
    "Toy Story 4": {
        "horario": lista_horarios, # 18:00, 20:00, 16:30, etc
        "boletos_disponibles": 40
    }
}

print(peliculas)

pelicula = input("Ingrese la pelicula que desea ver: ")
# for pelicula in peliculas.keys():
if pelicula in peliculas:
    print("Existe la pelicula")
    # horarios disponible de la pelicula seleccionada
    print("Horarios disponibles: ")
    for horario in peliculas[pelicula]["horario"]:
        print(horario)
else:
    print("No existe la pelicula")
