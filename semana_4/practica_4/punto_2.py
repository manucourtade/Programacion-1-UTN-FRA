# Sumar todos los elementos:
# Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los elementos.

array_suma = [0] * 10

for i in range(len(array_suma)):
    array_suma[i] = int(input(f'Ingrese el numero {i + 1}: '))
    
suma_total = 0
for num in array_suma:
    suma_total += num

# Mostrar resultado
print(f'La suma de todos los elementos es {suma_total}')