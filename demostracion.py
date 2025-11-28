"""
¿En qué consistirá la Demo?
Mostrar cómo recorrer listas en Python usando for y numerarlas de manera ordenada.
1. Crear una lista de elementos => lista=[]
a. Definir una lista con 8 elementos. => range(1,9)
2. Agregar el ciclo for
a. Imprimir cada elemento en una nueva línea. => print(elemento)
3. Incluir enumerate()
a. b. Utilizar enumerate() para obtener el índice de cada elemento.
Configurar start=1 para numeración desde 1.
4. Ejecutar y verificar la salida
"""
lista_numeros = []
for i in range(1, 9):
    lista_numeros.append(i)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]
                #1  2  3  4  5  6  7, 8   => índices

for index, numero in enumerate(lista_numeros, start=1):
    print(f"posicion=> {index}. | valor=> {numero}")
