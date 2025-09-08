# Invertir orden:
# Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero


array_enteros = [12, 1, 25, 65, 32, 102]

for i in range(len(array_enteros) - 1, -1, -1):  # desde el último hasta el primero
    print(array_enteros[i])
