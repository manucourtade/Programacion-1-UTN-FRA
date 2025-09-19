#Ejercicio 3: Control de Producción
#Una fábrica produce 3 productos y mide la producción durante 4 días.
#Cargar en una matriz 3x4 las cantidades producidas. Mostrar:
#    La producción total de cada producto.
#    La producción total de cada día.
#    Cuál fue el día con mayor producción total.

matriz = [[0, 0, 0, 0] for _ in range(3)]

def menu(mat):
    salir = False
    while salir == False:
        print('1. Ingresar cantidades producidas')
        print('2. Produccion total de cada producto')
        print('3. Produccion total de cada dia')
        print('4. Dia con mas produccion total')
        print('5. Salir')

        opcion = input('Ingrese una opcion: ')

        if opcion == '1':
            ingresar_cant(mat)
        elif opcion == '2':
            produc_total_produc(mat)
        elif opcion == '3':
            produc_total_dia(mat)
        elif opcion == '4':
            dia_mayor_produc(mat)
        elif opcion == '5':
            salir = True
        else:
            print('Ingrese opcion valida.')

def ingresar_cant(mat):

    for i in range(len(mat)):
        print(f'Producto {i + 1}')
        for j in range(len(mat[i])):
            cantidad = int(input(f'Ingrese la cantidad de produccion del dia {j + 1}: '))

            if cantidad >= 0:
                mat[i][j] = cantidad
            else:
                print('Ingrese cantidad positiva.')
                continue

def produc_total_produc(mat):
    for i in range(len(mat)):
        suma_prod = 0
        print(f'Producto {i + 1}')
        for j in range(len(mat[i])):
            suma_prod += mat[i][j]
        
        print(suma_prod)

def produc_total_dia(mat):
    for j in range(len(mat[0])):       
        suma_dia = 0
        for i in range(len(mat)):      
            suma_dia += mat[i][j]
        print(f"DIA {j + 1}: {suma_dia}")


def dia_mayor_produc(mat):
    mayor = 0
    dia_pos = 0
    for j in range(len(mat[0])):        
        suma_dia = 0
        for i in range(len(mat)):    
            suma_dia += mat[i][j]
        if suma_dia > mayor:
            mayor = suma_dia
            dia_pos = j + 1
    print(f"El día {dia_pos} tuvo la mayor producción: {mayor}")

    
menu(matriz)

