
# debe modificar la lista de entrada en el lugar y devolverla una vez que esté ordenada
# debe seguir el algoritmo de ordenamiento por selección, intercambiando el elemento más pequeño de la porción no ordenada de la lista con el primer elemento no ordenado.
# no debe realizar intercambios innecesarios cuando el elemento más pequeño ya está en la posición correcta.

def selection_sort (lista:list) -> list:

    for i in range(len(lista)-1): # cuando ya se acomodó hasta el anteúltimo número, el último que queda al final ya queda ordenado solo. Así que este bucle no necesita recorrer toda la lista, puede frenar uno antes.
        indice_minimo=i # supongo que es el mínimo hasta que se demuestre lo contrario
        for j in range(i + 1, len(lista)): # range(inicio, fin): j arranca en la posición siguiente a i y camina hasta el final absoluto de la lista
            # Comparamos el elemento actual del recorrido (j) contra nuestro candidato a mínimo
            if lista[j]<lista[indice_minimo]: # si el elemento que estoy mirando es menor que el mínimo que tengo hasta ahora, entonces actualizo el índice del mínimo
                indice_minimo=j

# falta definir el intercambio, solo lo hacemos si el índice del mínimo es diferente al índice actual (i)