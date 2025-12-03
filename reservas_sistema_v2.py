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

# Diccionario de películas con sus horarios, precio y disponibilidad
peliculas = {
    "1": {
        "titulo": "Avatar: El Camino del Agua",
        "horarios": ["14:00", "17:30", "21:00"],
        "precio": 12.50,
        "disponibles": 50
    },
    "2": {
        "titulo": "Oppenheimer",
        "horarios": ["15:00", "18:00", "21:30"],
        "precio": 13.00,
        "disponibles": 45
    },
    "3": {
        "titulo": "Barbie",
        "horarios": ["13:30", "16:00", "19:00", "22:00"],
        "precio": 11.50,
        "disponibles": 60
    },
    "4": {
        "titulo": "Misión Imposible: Sentencia Mortal",
        "horarios": ["14:30", "17:00", "20:00"],
        "precio": 13.50,
        "disponibles": 40
    },
    "5": {
        "titulo": "Guardianes de la Galaxia Vol. 3",
        "horarios": ["15:30", "18:30", "21:30"],
        "precio": 12.00,
        "disponibles": 55
    }
}

# Lista para almacenar las reservas del usuario
reservas = []
total_general = 0

print("=" * 60)
print("🎬 BIENVENIDO AL SISTEMA DE RESERVAS DE CINE 🎬")
print("=" * 60)

# Bucle principal del sistema
continuar_comprando = True

while continuar_comprando:
    print("\n" + "=" * 60)
    print("PELÍCULAS DISPONIBLES")
    print("=" * 60)
    
    # Mostrar todas las películas disponibles usando bucle for
    for codigo, info in peliculas.items():
        print(f"\n[{codigo}] {info['titulo']}")
        print(f"    💰 Precio: ${info['precio']:.2f} por boleto")
        print(f"    🎫 Boletos disponibles: {info['disponibles']}")
        print(f"    🕐 Horarios: {', '.join(info['horarios'])}")
    
    print("\n" + "=" * 60)
    
    # Solicitar selección de película con validación
    pelicula_valida = False
    while not pelicula_valida:
        pelicula_seleccionada = input("\n🎬 Seleccione el número de la película (o 'salir' para terminar): ").strip()
        
        if pelicula_seleccionada.lower() == 'salir':
            continuar_comprando = False
            break
        
        if pelicula_seleccionada in peliculas:
            pelicula_valida = True
        else:
            print("❌ Opción inválida. Por favor, seleccione un número válido de película.")
    
    if not continuar_comprando:
        break
    
    # Obtener información de la película seleccionada
    pelicula_info = peliculas[pelicula_seleccionada]
    print(f"\n✅ Has seleccionado: {pelicula_info['titulo']}")
    print(f"💰 Precio por boleto: ${pelicula_info['precio']:.2f}")
    print(f"🎫 Boletos disponibles: {pelicula_info['disponibles']}")
    
    # Mostrar horarios disponibles
    print("\n🕐 Horarios disponibles:")
    for i, horario in enumerate(pelicula_info['horarios'], 1):
        print(f"   [{i}] {horario}")
    
    # Seleccionar horario con validación
    horario_valido = False
    while not horario_valido:
        try:
            horario_idx = int(input(f"\nSeleccione el número del horario (1-{len(pelicula_info['horarios'])}): ")) - 1
            if 0 <= horario_idx < len(pelicula_info['horarios']):
                horario_seleccionado = pelicula_info['horarios'][horario_idx]
                horario_valido = True
            else:
                print(f"❌ Por favor, seleccione un número entre 1 y {len(pelicula_info['horarios'])}")
        except ValueError:
            print("❌ Por favor, ingrese un número válido")
    
    print(f"✅ Horario seleccionado: {horario_seleccionado}")
    
    # Solicitar cantidad de boletos con validación
    cantidad_valida = False
    while not cantidad_valida:
        try:
            cantidad_boletos = int(input(f"\n🎫 ¿Cuántos boletos desea comprar? (Disponibles: {pelicula_info['disponibles']}): "))
            
            if cantidad_boletos <= 0:
                print("❌ La cantidad debe ser mayor a 0")
            elif cantidad_boletos > pelicula_info['disponibles']:
                print(f"❌ Lo sentimos, solo hay {pelicula_info['disponibles']} boletos disponibles")
            else:
                cantidad_valida = True
        except ValueError:
            print("❌ Por favor, ingrese un número válido")
    
    # Calcular precio total de esta compra
    precio_compra = cantidad_boletos * pelicula_info['precio']
    
    # Mostrar resumen de la compra actual
    print("\n" + "-" * 60)
    print("📋 RESUMEN DE COMPRA ACTUAL")
    print("-" * 60)
    print(f"Película: {pelicula_info['titulo']}")
    print(f"Horario: {horario_seleccionado}")
    print(f"Cantidad de boletos: {cantidad_boletos}")
    print(f"Precio por boleto: ${pelicula_info['precio']:.2f}")
    print(f"Total de esta compra: ${precio_compra:.2f}")
    print("-" * 60)
    
    # Confirmar compra
    confirmar = input("\n¿Confirmar esta compra? (s/n): ").strip().lower()
    
    if confirmar == 's':
        # Actualizar disponibilidad
        peliculas[pelicula_seleccionada]['disponibles'] -= cantidad_boletos
        
        # Agregar a la lista de reservas
        reservas.append({
            'pelicula': pelicula_info['titulo'],
            'horario': horario_seleccionado,
            'cantidad': cantidad_boletos,
            'precio_unitario': pelicula_info['precio'],
            'subtotal': precio_compra
        })
        
        total_general += precio_compra
        print("\n✅ ¡Compra confirmada exitosamente!")
    else:
        print("\n❌ Compra cancelada")
    
    # Preguntar si desea comprar más boletos
    otra_compra = input("\n¿Desea realizar otra compra? (s/n): ").strip().lower()
    if otra_compra != 's':
        continuar_comprando = False

# Mostrar resumen final si hay reservas
if len(reservas) > 0:
    print("\n" + "=" * 60)
    print("🎉 RESUMEN FINAL DE TODAS TUS RESERVAS 🎉")
    print("=" * 60)
    
    # Mostrar cada reserva usando bucle for
    for i, reserva in enumerate(reservas, 1):
        print(f"\n📌 Reserva #{i}")
        print(f"   🎬 Película: {reserva['pelicula']}")
        print(f"   🕐 Horario: {reserva['horario']}")
        print(f"   🎫 Boletos: {reserva['cantidad']}")
        print(f"   💵 Precio unitario: ${reserva['precio_unitario']:.2f}")
        print(f"   💰 Subtotal: ${reserva['subtotal']:.2f}")
    
    print("\n" + "=" * 60)
    print(f"🎫 TOTAL DE BOLETOS COMPRADOS: {sum(r['cantidad'] for r in reservas)}")
    print(f"💵 TOTAL A PAGAR: ${total_general:.2f}")
    print("=" * 60)
    print("\n✨ ¡Gracias por su compra! ¡Disfrute su película! ✨\n")
else:
    print("\n" + "=" * 60)
    print("👋 No se realizaron compras. ¡Hasta pronto!")
    print("=" * 60)