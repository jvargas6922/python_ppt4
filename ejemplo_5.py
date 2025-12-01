"""
script para recorrer un bucle anidado

"""
for i in range(1, 4):
    for j in range(1, 4):
        print(f"Iterador externo {i}, Iterador interno {j}")

"""
 Iterador Externo i = 1 || Iterador Interno j = 1
 Iterador Externo i = 1 || Iterador Interno j = 2
 Iterador Externo i = 1 || Iterador Interno j = 3
 ------------------------------------------------
 Iterador Externo i = 2 || Iterador Interno j = 1
 Iterador Externo i = 2 || Iterador Interno j = 2
 Iterador Externo i = 2 || Iterador Interno j = 3
 ------------------------------------------------
 Iterador Externo i = 3 || Iterador Interno j = 1
 Iterador Externo i = 3 || Iterador Interno j = 2
 Iterador Externo i = 3 || Iterador Interno j = 3




"""