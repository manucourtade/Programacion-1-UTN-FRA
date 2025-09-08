# Contar mayores a un valor:
# Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.

array_enteros = [100, 111, 2, 23, 1212, 12, 23, 101] 
contar_mayores = 0

for i in range(len(array_enteros)):
    if array_enteros[i] > 100:
        contar_mayores += 1

print(f'{contar_mayores} son mayores a 100')


