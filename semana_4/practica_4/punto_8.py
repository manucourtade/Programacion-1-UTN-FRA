# Comparar dos arrays:
#Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
# y mostrar un mensaje indicando si son o no iguales.

array1 = [12, 13, 14, 132, 21]
array2 = [12.3, 13.0, 14.01, 132.0, 21.1]

for i in range(len(array1)):
    if array1[i] == array2[i]:
        print('Son iguales!')
    else:
        print('No son iguales')
    