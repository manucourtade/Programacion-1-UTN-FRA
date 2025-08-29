# Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
# resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la
# función.
def operaciones(num1: int, num2: int) -> int:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    return suma, resta, multiplicacion

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))

resultado_suma, resultado_resta, resultado_multiplicacion = operaciones(n1, n2) 

print(f' Suma: {resultado_suma}, Resta: {resultado_resta}, Multiplicacion: {resultado_multiplicacion}')