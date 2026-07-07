# Taller - Algoritmo de Orden por Fusión

def merge_sort(array):
    # condicion de parada: si el array tiene 1 o menos elementos, ya está ordenado y evito que el código explote en la recursividad 
    if len(array) <= 1:
        return

    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]
    merge_sort(left_part) # llamo recursivamente a la función para ordenar la parte izquierda
    merge_sort(right_part) # llamo recursivamente a la función para ordenar la parte derecha

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # bucle que continúa mientras queden elementos en ambos left_part y right_part
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            # sobreescribo el valor en la posición sorted_index del array original con el valor de left_part (no hay conflicto con datos originales porque estos ya fueron copiados a left_part y right_part)
            left_array_index += 1 # como usamos el valor de left_part, incrementamos su índice para pasar al siguiente elemento
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1 # como usamos el valor de right_part, incrementamos su índice para pasar al siguiente elemento

        sorted_index += 1 # incrementamos el índice del array original para pasar a la siguiente posición

    while left_array_index < len(left_part): # se acabaron los elementos en right_part, pero aún quedan elementos en left_part
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part): # se acabaron los elementos en left_part, pero aún quedan elementos en right_part
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ')
    print(numbers)

