#  Buscar un valor:
# Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
# Informar la posición en caso afirmativo, o indicar que no se encuentra.
array_enteros = [100, 111, 2, 23, 1212, 12, 23, 101, 123, 21]

num = int(input('Ingrese el número a buscar: '))

for i in range(len(array_enteros)):
    if array_enteros[i] == num:
        print(f'{num} se encuentra en la posición {i + 1}')
        break
else:
    print(f'{num} no se encuentra en el array!')
        
