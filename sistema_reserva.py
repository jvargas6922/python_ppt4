"""
Sistema de Gestión de Reservas
Contexto:
    En este ejercicio, construiremos un sistema de gestión de reservas para un cine. El usuario podrá reservar
    boletos, seleccionar funciones y visualizar su resumen de compra. Se aplicarán ciclos while, for, y estructuras
    condicionales para manejar la lógica del sistema.
Consigna: 
    1. Mostrar una lista de películas disponibles con horarios. (listo)
    2. Permitir al usuario seleccionar una película y la cantidad de boletos.(listo)
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
lista_opciones = ["1 - Avatar 2", "2 - Avengers Endgame", "3 - Toy Story 4", "4 - Salir"]

lista_peliculas = {
    "Avatar 2": {
        "horario_1": "16:30",
        "boletos_disponibles_horario_1": 30,
        "horario_2": "18:00",
        "boletos_disponibles_horario_2": 30,
        "horario_3": "20:00",
        "boletos_disponibles_horario_3": 30,
        "horarios":["16:30", "18:00", "20:00"]
    },
    "Avengers Endgame": {
        "horario_1": "16:30",
        "boletos_disponibles_horario_1": 25,
        "horario_2": "18:00",
        "boletos_disponibles_horario_2": 25,
        "horario_3": "20:00",
        "boletos_disponibles_horario_3": 25,
        "horarios":["16:30", "18:00", "20:00"]
    },
    "Toy Story 4": {
        "horario_1": "16:30",
        "boletos_disponibles_horario_1": 40,
        "horario_2": "18:00",
        "boletos_disponibles_horario_2": 40,
        "horario_3": "20:00",
        "boletos_disponibles_horario_3": 40,
        "horarios":["16:30", "18:00", "20:00"]
    }
}
seleccion_usuario = {}

print("Peliculas disponibles: ")
for opcion in lista_opciones:
    print(opcion)
pelicula = input("Elija la opcion de la pelicula que desea ver: ")
# while pelicula != "5":
    # pelicula = input("Ingrese la pelicula que desea ver: ")
    # for pelicula in peliculas.keys():
    # saber que pelicula eligio el usuario
if pelicula == "1":
    pelicula = "Avatar 2"
elif pelicula == "2":
    pelicula = "Avengers Endgame"
elif pelicula == "3":
    pelicula = "Toy Story 4"
elif pelicula == "4":
    pelicula = "Salir"
else:
    pelicula = "No existe la pelicula"



if pelicula in lista_peliculas:
    print(f"Horarios disponibles para {pelicula}: {lista_peliculas[pelicula]['horarios']}")
    print("Seleccione un horario: \n1- 16:30  \n2- 18:00 \n3- 20:00")
    horario_seleccionado = input("Ingrese la opcion del horario que desea: ")
    if horario_seleccionado == "1":
        horario = lista_peliculas[pelicula]['horarios'][0]
        boletos_disponibles = lista_peliculas[pelicula]["boletos_disponibles_horario_1"]
    elif horario_seleccionado == "2":
        horario = lista_peliculas[pelicula]['horarios'][1]
        boletos_disponibles = lista_peliculas[pelicula]["boletos_disponibles_horario_2"]
    elif horario_seleccionado == "3":
        horario = lista_peliculas[pelicula]['horarios'][2]
        boletos_disponibles = lista_peliculas[pelicula]["boletos_disponibles_horario_3"]
    else:
        horario = "No existe el horario"
        boletos_disponibles = 0

    print("Horario y Pelicula seleccionada: ", horario, pelicula)
    cantidad_boletos =  int(input("Ingrese la cantidad de boletos que desea reservar: "))
     # avatar => 30 , Avengers Endgame => 25, Toy Story 4 => 40

    if pelicula == "Avatar 2":
        if cantidad_boletos > 30:
            print("No hay suficientes boletos disponibles")
        else:
            print("Reserva exitosa")
    elif pelicula == "Avengers Endgame":
        if cantidad_boletos > 25:
            print("No hay suficientes boletos disponibles")
        else:
            print("Reserva exitosa")
            # podria sacar calculos de los bolestos comprados
    elif pelicula == "Toy Story 4":
        if cantidad_boletos > 40:
            print("No hay suficientes boletos disponibles")
        else:
            print("Reserva exitosa")



"""
{
    pelicula = Avatar 2
    horario = 18:00
    boletos = 3
},
{
    pelicula = Avengers Endgame
    horario = 20:00
    boletos = 2
},
{
    pelicula = Toy Story 4
    horario = 16:30
    boletos = 5
}

"""