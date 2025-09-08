# Intercambiar elementos pares por ceros:
# Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array resultante.

array_pares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(array_pares)):
    if array_pares[i] % 2 == 0:
        array_pares[i]= 0

print(array_pares)