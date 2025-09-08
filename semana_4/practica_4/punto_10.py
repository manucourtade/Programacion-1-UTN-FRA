# Función para buscar la primera aparición de un valor:
# Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
# la posición de la primera aparición de ese número o -1 si no se encuentra.

array_enteros = [23, 5, 23, 29, 21, 23, 17]
num = int(input('Ingrese el numero a buscar: '))

def primera_aparicion(array_enteros, num):
    for i in range(len(array_enteros)):
        if num == array_enteros[i]:
            return i + 1
        
    return -1
        
print(primera_aparicion(array_enteros, num))




