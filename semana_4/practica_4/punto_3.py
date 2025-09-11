#  Promedio de valores:
# Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio de los valores.
array_floats = [0.0] * 6

for i in range(len(array_floats)):
    array_floats[i] = float(input(f'Ingrese el numero {i + 1}: '))

suma_array = 0 

for k in array_floats:
    suma_array += k
promedio = suma_array / len(array_floats)

print(f'Promedio del array: {promedio:.2f}')