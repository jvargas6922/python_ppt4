"""
crea un script que me permita la creacion de un de un producto y luego mostrar el producto creado.
"""

# Logica
"""
Entrada:
    - solicitar los datos del producto
Proceso:
    - guardar el producto en una lista o diccionario
Salida:
    - mostrar el producto creado
"""

# creacion de un solo producto.
# producto = input("Ingrese el nombre del producto: ")
# print("Producto creado:", producto)


# productos masivos.
cantidad_producto = int(input("Ingrese la cantidad de productos a crear: "))
lista_productos = []
for i in range(cantidad_producto):
    producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    lista_productos.append(producto)
    print("Producto creado:", producto)

# mostrar todos los productos creados
print("Todos los productos creados:", lista_productos)