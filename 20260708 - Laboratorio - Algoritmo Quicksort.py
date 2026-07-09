# 1) Elegir un valor pivote de los elementos de la lista de entrada (usar el primer o el último elemento de la lista).
# 2) Dividir la lista de entrada en tres sublistas: una con elementos menores que el pivote, una con elementos iguales al pivote, y una con elementos mayores que el pivote.
# 3) Llamar recursivamente a quick_sort para ordenar las sublistas y concatenar las sublistas ordenadas para producir la lista final ordenada.
# 4) La función quick_sort no debería modificar la lista pasada como argumento.

def quick_sort(lista):
    if len(lista)<=1:
        return lista
    
    pivote=lista[0]
    menores=[]
    iguales=[]
    mayores=[]

    for elemento in lista:
        if elemento<pivote:
            menores.append(elemento)
        elif elemento>pivote:
            mayores.append(elemento)
        else:
            iguales.append(elemento)

    return quick_sort(menores) + iguales + quick_sort(mayores)
    # recursividad en los conjuntos mejores y mayores para ordenar esos elementos
    # conjunto iguales queda sin cambios porque todos los elementos son iguales al pivote
    # concateno las sublistas ordenadas y devuelvo la lista final ordenada