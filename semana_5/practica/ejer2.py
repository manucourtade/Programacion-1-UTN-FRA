#Ejercicio 2: Puntajes de un Torneo
#En un torneo de programación hay 4 equipos que compiten en 5 rondas.
#Cargar en una matriz 4x5 los puntajes obtenidos (enteros). Luego mostrar:
#    El puntaje total de cada equipo.
#    Qué equipo obtuvo el mayor puntaje en total.

matriz = [[0, 0, 0, 0, 0] for _ in range(4)]

def menu(mat):
    salir = False
    while salir == False:
        print('1. Ingresar puntaje de los equipos')
        print('2. Puntaje total de equipo')
        print('3. Equipo que obtuvo el mayor puntaje')
        print('4. Salir')

        opcion = input('Ingrese una opcion: ')

        if opcion == '1':
            cargar_puntaje(mat)
        elif opcion == '2':
            puntaje_total(mat)
        elif opcion == '3':
            mejor_equipo(mat)
        elif opcion == '4':
            salir = True
        else:
            print('Ingrese opcion valida.')

def cargar_puntaje(mat):
    for i in range(len(mat)):
        print(f'Equipo {i + 1}')
        for j in range(len(mat[i])):
            puntaje = int(input(f'Ingrese el puntaje obtenido del equipo {i + 1}: '))
            mat[i][j] = puntaje
    
def puntaje_total(mat):
    
    for i in range(len(mat)):
        suma_equipo = 0
        print(f'Equipo {i + 1}')

        for j in range(len(mat)):
            suma_equipo += mat[i][j]
        print(suma_equipo)


def mejor_equipo(mat):
    max_suma = 0
    mejor_equipo = 0

    for i in range(len(mat)):       
        suma_equipo = 0
        for j in range(len(mat[i])): 
            suma_equipo += mat[i][j]

        if suma_equipo > max_suma:   
            max_suma = suma_equipo
            mejor_equipo = i

    print(f'El equipo con mas puntaje es el equipo {mejor_equipo + 1} con un puntaje de {max_suma} puntos')


menu(matriz)
