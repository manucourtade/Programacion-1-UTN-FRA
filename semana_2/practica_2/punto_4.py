# Crear una función buscar_mayor que reciba tres números y devuelva los tres números
# ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números
# ordenados.


def buscar_mayor(a: int, b: int, c: int) -> int:
    if b <= a >= c:
        if b >= c:
            return a, b, c
        else:
            return a, c, b
    elif a <= b >= c:
        if a >= c:
            return b, a, c
        else:
            return b, c, a
    else:
        if a >= b:
            return c, a, b
        else:
            return c, b, a
    
n1: int = int(input('Ingrese el primer numero:'))
n2: int = int(input('Ingrese el segundo numero:'))
n3: int = int(input('Ingrese el tercer numero:'))

num_max, num_med, num_min = buscar_mayor(n1, n2, n3)
print(f'Números ordenados de mayor a menor: {num_max}, {num_med}, {num_min}')

