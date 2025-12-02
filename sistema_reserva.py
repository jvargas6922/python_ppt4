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
# lista_horarios = ["18:00", "20:00", "16:30"]
# lista_opciones = ["1 - Avatar 2", "2 - Avengers Endgame", "3 - Toy Story 4", "4 - Salir"]

# lista_peliculas = {
#     "1": {
#         "pelicula": "Avatar 2",  
#         # "horarios": "16:30",
#         # "boletos_disponibles_horario_1": 30,
#         # "horario_2": "18:00",
#         # "boletos_disponibles_horario_2": 30,
#         # "horario_3": "20:00",
#         # "boletos_disponibles_horario_3": 30,
#         "horarios":["16:30", "18:00", "20:00"],
#         "boletos_disponibles":[30,30,30],
#         "precio_bolesto": 1500
#     },
#     "Avengers Endgame": {
#         "horario_1": "16:30",
#         "boletos_disponibles_horario_1": 25,
#         "horario_2": "18:00",
#         "boletos_disponibles_horario_2": 25,
#         "horario_3": "20:00",
#         "boletos_disponibles_horario_3": 25,
#         "horarios":["16:30", "18:00", "20:00"]
#     },
#     "Toy Story 4": {
#         "horario_1": "16:30",
#         "boletos_disponibles_horario_1": 40,
#         "horario_2": "18:00",
#         "boletos_disponibles_horario_2": 40,
#         "horario_3": "20:00",
#         "boletos_disponibles_horario_3": 40,
#         "horarios":["16:30", "18:00", "20:00"]
#     }
# }
# seleccion_usuario = {}

# print("Peliculas disponibles: ")
# for opcion in lista_opciones:
#     print(opcion)
# pelicula = input("Elija la opcion de la pelicula que desea ver: ")
# print("Pelicula seleccionada: ", lista_peliculas[pelicula]['pelicula'])
# for horario in lista_peliculas[pelicula]['horarios']:
#     print(horario)
#     horario_seleccionado  = input("Ingrese la opcion del horario que desea: ")
#     if horario_seleccionado in lista_peliculas[pelicula]['horarios']:
#         print("Horario seleccionado: ", horario_seleccionado)
# # while pelicula != "5":
#     # pelicula = input("Ingrese la pelicula que desea ver: ")
#     # for pelicula in peliculas.keys():
#     # saber que pelicula eligio el usuario
# # if pelicula == "1":
# #     pelicula = "Avatar 2"
# # elif pelicula == "2":
# #     pelicula = "Avengers Endgame"
# # elif pelicula == "3":
# #     pelicula = "Toy Story 4"
# # elif pelicula == "4":
# #     pelicula = "Salir"
# # else:
# #     pelicula = "No existe la pelicula"



# # if pelicula in lista_peliculas:
# #     print(f"Horarios disponibles para {pelicula}: {lista_peliculas[pelicula]['horarios']}")
# #     print("Seleccione un horario: \n1- 16:30  \n2- 18:00 \n3- 20:00")
# #     horario_seleccionado = input("Ingrese la opcion del horario que desea: ")
# #     if horario_seleccionado == "1":
# #         horario = lista_peliculas[pelicula]['horarios'][0]
# #         boletos_disponibles = lista_peliculas[pelicula]["boletos_disponibles_horario_1"]
# #     elif horario_seleccionado == "2":
# #         horario = lista_peliculas[pelicula]['horarios'][1]
# #         boletos_disponibles = lista_peliculas[pelicula]["boletos_disponibles_horario_2"]
# #     elif horario_seleccionado == "3":
# #         horario = lista_peliculas[pelicula]['horarios'][2]
# #         boletos_disponibles = lista_peliculas[pelicula]["boletos_disponibles_horario_3"]
# #     else:
# #         horario = "No existe el horario"
# #         boletos_disponibles = 0

# #     print("Horario y Pelicula seleccionada: ", horario, pelicula)
# #     cantidad_boletos =  int(input("Ingrese la cantidad de boletos que desea reservar: "))
# #      # avatar => 30 , Avengers Endgame => 25, Toy Story 4 => 40

# #     if pelicula == "Avatar 2":
# #         if cantidad_boletos > 30:
# #             print("No hay suficientes boletos disponibles")
# #         else:
# #             print("Reserva exitosa")
# #     elif pelicula == "Avengers Endgame":
# #         if cantidad_boletos > 25:
# #             print("No hay suficientes boletos disponibles")
# #         else:
# #             print("Reserva exitosa")
# #             # podria sacar calculos de los bolestos comprados
# #     elif pelicula == "Toy Story 4":
# #         if cantidad_boletos > 40:
# #             print("No hay suficientes boletos disponibles")
# #         else:
# #             print("Reserva exitosa")



# """
# {
#     pelicula = Avatar 2
#     horario = 18:00
#     boletos = 3
# },
# {
#     pelicula = Avengers Endgame
#     horario = 20:00
#     boletos = 2
# },
# {
#     pelicula = Toy Story 4
#     horario = 16:30
#     boletos = 5
# }



## codigo de Eduardo para referencia

peliculas = {
    "El sobreviviente": {
        "horarios": {
            "20:30": 100,
            "22:30": 80,
        },
        "precio": 5000,
    },
    "Zootopia 2": {
        "horarios": {
            "21:40": 75,
            "22:00": 100,
        },
        "precio": 5000,
    },
    "No alimentes a los niños": {
        "horarios": {
            "22:10": 60,
        },
        "precio": 5000,
    },
    "Los ilusionistas 3": {
        "horarios": {
            "19:00": 70,
            "21:50": 50,
        },
        "precio": 5000,
    },
    "Jujutsu kaisen ejecución": {
        "horarios": {
            "22:20": 85,
        },
        "precio": 5000,
    },
    "Depredador: tierras salvajes": {
        "horarios": {
            "19:50": 63,
            "21:50": 69,
        },
        "precio": 5000,
    },
}

# 1) Diccionario con películas y horarios está definido arriba ✓
# 2) Usar un while para mostrar el menú y permitir selecciones repetidas
# Variable para almacenar las reservas realizadas
reservas_totales = []
costo_total = 0

while True:
    print("\n" + "=" * 50)
    print("BIENVENIDO AL SISTEMA DE RESERVAS DEL CINE")
    print("=" * 50)
    print("\nPELÍCULAS DISPONIBLES:")
    print("-" * 50)

    # Crear una lista de películas para acceder por índice
    lista_peliculas = list(peliculas.keys())

    for i, pelicula in enumerate(lista_peliculas, 1):
        print(f"  {i} - {pelicula}")

    print("\n" + "-" * 50)
    seleccion = input(
        "Seleccione el número de la película (o 'salir' para finalizar): "
    )

    if seleccion.lower() == "salir":
        # 7) Mostrar un resumen final con todas las reservas y costo total
        print("\n" + "=" * 50)
        print("RESUMEN FINAL DE RESERVAS")
        print("=" * 50)

        if reservas_totales:
            for idx, reserva in enumerate(reservas_totales, 1):
                print(f"\n{idx}. {reserva['pelicula']}")
                print(f"   Horario: {reserva['horario']}")
                print(f"   Entradas: {reserva['cantidad']}")
                print(f"   Precio unitario: ${reserva['precio_unitario']}")
                print(f"   Subtotal: ${reserva['subtotal']}")

            print("\n" + "-" * 50)
            print(f"COSTO TOTAL: ${costo_total:,.0f}")
            print("=" * 50)
        else:
            print("No realizó ninguna reserva.")

        print("\n¡Gracias por usar el sistema de reservas. ¡Hasta luego!")
        break

    # Validar que la entrada sea un número
    try:
        numero_pelicula = int(seleccion)

        # Validar que el número esté en el rango correcto
        if 1 <= numero_pelicula <= len(lista_peliculas):
            pelicula_seleccionada = lista_peliculas[numero_pelicula - 1]
            print(f"\n{'=' * 50}")
            print(f"HAS SELECCIONADO: {pelicula_seleccionada.upper()}")
            print(f"{'=' * 50}")

            # Obtener horarios disponibles
            horarios_disponibles = peliculas[pelicula_seleccionada]["horarios"]
            lista_horarios = list(horarios_disponibles.keys())

            # Si hay más de un horario, pedir que seleccione
            if len(lista_horarios) > 1:
                print("\nHORARIOS DISPONIBLES:")
                print("-" * 50)
                for idx, horario in enumerate(lista_horarios, 1):
                    boletos = horarios_disponibles[horario]
                    print(f"  {idx} - {horario} | Entradas disponibles: {boletos}")

                horario_seleccion = input(
                    "\nSeleccione el número del horario deseado: "
                )

                try:
                    numero_horario = int(horario_seleccion)
                    if 1 <= numero_horario <= len(lista_horarios):
                        horario_elegido = lista_horarios[numero_horario - 1]
                    else:
                        print("Número de horario inválido.")
                        continue
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
            else:
                # Si solo hay un horario, usarlo automáticamente
                horario_elegido = lista_horarios[0]
                print(f"\nHorario disponible: {horario_elegido}")

            # 3) Solicitar la cantidad de boletos
            boletos_disponibles = horarios_disponibles[horario_elegido]
            print(
                f"\nEntradas disponibles para {horario_elegido}: {boletos_disponibles}"
            )

            cantidad_str = input("¿Cuántas entradas desea comprar? ")

            try:
                cantidad_entradas = int(cantidad_str)

                # 4) Verificar disponibilidad de boletos
                if cantidad_entradas <= 0:
                    print("La cantidad debe ser mayor a 0.")
                    continue

                if cantidad_entradas > boletos_disponibles:
                    print(
                        f"No hay suficientes boletos. Solo hay {boletos_disponibles} disponibles."
                    )
                    continue

                # 5) Calcular el precio total
                precio_unitario = peliculas[pelicula_seleccionada]["precio"]
                subtotal = cantidad_entradas * precio_unitario

                # Mostrar resumen de la compra
                print("\n" + "=" * 50)
                print("RESUMEN DE COMPRA")
                print("=" * 50)
                print(f"Película: {pelicula_seleccionada}")
                print(f"Horario: {horario_elegido}")
                print(f"Entradas: {cantidad_entradas}")
                print(f"Precio por entrada: ${precio_unitario:,.0f}")
                print(f"Subtotal: ${subtotal:,.0f}")
                print("=" * 50)

                # 6) Permitir agregar más reservas o finalizar
                confirmacion = input("\n¿Desea confirmar esta reserva? (s/n): ").lower()

                if confirmacion == "s":
                    # Guardar la reserva
                    reservas_totales.append(
                        {
                            "pelicula": pelicula_seleccionada,
                            "horario": horario_elegido,
                            "cantidad": cantidad_entradas,
                            "precio_unitario": precio_unitario,
                            "subtotal": subtotal,
                        }
                    )

                    # Actualizar boletos disponibles
                    peliculas[pelicula_seleccionada]["horarios"][
                        horario_elegido
                    ] -= cantidad_entradas

                    # Actualizar costo total
                    costo_total += subtotal

                    print("\n¡Reserva confirmada exitosamente!")

                    # Preguntar si desea hacer otra reserva
                    otra_reserva = input(
                        "\n¿Desea realizar otra reserva? (s/n): "
                    ).lower()

                    if otra_reserva != "s":
                        # Mostrar resumen final y salir
                        print("\n" + "=" * 50)
                        print("RESUMEN FINAL DE RESERVAS")
                        print("=" * 50)

                        for idx, reserva in enumerate(reservas_totales, 1):
                            print(f"\n{idx}. {reserva['pelicula']}")
                            print(f"   Horario: {reserva['horario']}")
                            print(f"   Entradas: {reserva['cantidad']}")
                            print(
                                f"   Precio unitario: ${reserva['precio_unitario']:,.0f}"
                            )
                            print(f"   Subtotal: ${reserva['subtotal']:,.0f}")

                        print("\n" + "-" * 50)
                        print(f"COSTO TOTAL: ${costo_total:,.0f}")
                        print("=" * 50)
                        print(
                            "\n¡Gracias por usar el sistema de reservas. ¡Hasta luego!"
                        )
                        break
                else:
                    print("\nReserva cancelada. Volviendo al menú principal...")

            except ValueError:
                print("Por favor, ingrese una cantidad válida.")
        else:
            print(
                "El número ingresado no es válido. Por favor, elija un número de la lista."
            )
    except ValueError:
        print("Por favor, ingrese un número válido o 'salir' para finalizar.")