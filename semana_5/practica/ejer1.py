#Ejercicio 1: Registro de Temperaturas
#Una estación meteorológica registra las temperaturas diarias de una semana (7 días) en 3 horarios (mañana, tarde y noche).
#Cargar en una matriz 7x3 las temperaturas (números enteros) y mostrar:
#   El promedio de temperatura de cada día.
#    El promedio general de toda la semana.

matriz = [[0, 0, 0] for _  in range(7)]

DIAS = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

def cargar_temp(mat):
    for i in range(len(mat)):
        print(f'Dia {DIAS[i]}')
        for j in range(len(mat[i])):
            temp = float(input('Ingrese la temperatura: '))

            mat[i][j] = temp
    

def promedio_dia(mat):
    for i in range(len(mat)):
        acumulador = 0.0
        print(f'Dia {DIAS[i]}')
        for j in range(len(mat[i])):
            acumulador += mat[i][j]
        promedio = acumulador / len(mat[i])
        print(f'Promedio: {promedio:.2f}')
        
    

def promedio_general(mat):
    acumulador = 0.0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            acumulador += mat[i][j]
        
        promedio = acumulador / len(mat[i])
    print(f'Promedio general: {promedio:.2f}')

def menu(mat):
    salir = False

    while salir == False:
        opcion = input('''
Registro de Temperaturas
1. Cargar temperaturas
2. Promedio de cada dia
3. Promedio general
4. Salir
=> ''')
        if opcion == '1':
            cargar_temp(mat)
        elif opcion == '2':
            promedio_dia(mat)
        elif opcion == '3':
            promedio_general(mat)
        elif opcion == '4':
            print('ADIOS')
            salir = True
        else:
            print('Ingrese una opcion correcta')

menu(matriz)