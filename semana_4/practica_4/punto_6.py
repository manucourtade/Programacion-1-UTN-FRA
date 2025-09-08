# Mayor y su posición:
# Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se encuentra.
array_enteros = [10, 20, 30, 140 , 50, 60, 70]
valor_max = 0
for i in range(len(array_enteros)):
    if array_enteros[i] > valor_max:
        valor_max = array_enteros[i]
        pos_max = i
print(f'El mayor valor es {valor_max} y se encuentra en la posición {pos_max + 1}')

        