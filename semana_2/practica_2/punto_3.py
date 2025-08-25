# Definir una función area_triangulo que reciba la base y la altura de un triángulo y
# devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.
# Fórmula: area = (b * h) / 2

def area_triangulo(b: float, h: float) -> float:
    return (b * h) /   2

base = float(input('Ingrese la base del triangulo: '))
altura = float(input('Ingrese la altura del triangulo: '))

area = area_triangulo(base, altura)

print(f'El area del triangulo es: {area}')