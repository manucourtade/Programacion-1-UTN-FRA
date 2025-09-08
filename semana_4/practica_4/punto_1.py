# Cargar y mostrar array:
#Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un ciclo for.
array_enteros = [0] * 5

for i in range(len(array_enteros)):
    array_enteros[i] = int(input(f'Ingrese enteros {i + 1}: '))

print("\nContenido del array:")
for i in range(len(array_enteros)):
    print(array_enteros[i])
