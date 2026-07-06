# laboratorio: Immplementación Metodo de Bisección

def square_root_bisection (number,tolerance=0.1, maxiter=10):
# valores por defecto dentro del def: si no se pasan como argumentos cuando se llame la función, se toman los valores y la función no lanza un error
    if number < 0:
        raise ValueError(f'Square root of negative number is not defined in real numbers') 

    elif number == 0 or number == 1:
        print (f'The square root of {number} is {number}')
        return number
    
    else: # luego, number es mayor que 1, por lo tanto, el rango de búsqueda es [0, number]
        low = 0
        high = max(1, number)
        # en una sola línea contemplo el caso en que number sea menor que 1, por ejemplo 0.25: en ese caso el rango de búsqueda será [0, 1]

        for i in range(maxiter): # range devuelve una secuencia de números: (0, maxiter-1)
            mid = (low + high) / 2
            mid_squared = mid ** 2

            if abs(high - low) <= tolerance: # condición de éxito
                root = mid
                print (f'The square root of {number} is approximately {root}') 
                return mid

            elif mid_squared < number:
                low = mid

            else:
                high = mid

    print (f'Failed to converge within {maxiter} iterations')
    return None
# llegado a este punto significa que no se ha encontrado la raíz cuadrada dentro de la tolerancia y el número máximo de iteraciones