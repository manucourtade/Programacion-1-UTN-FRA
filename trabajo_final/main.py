from creditos.func_creditos import creditos, datos


def mini_generala():
    while True:
        print('=' * 20)
        print('MINI GENERALA')
        print('=' * 20)

        print('1. Jugar')
        print('2. Estadisticas')
        print('3. Creditos')
        print('4. Salir')
        
        opcion = input('Ingrese una opcion => ')

        if opcion == '1':
            pass
        elif opcion == '2':
            pass
        elif opcion == '3':
            creditos(datos)
        elif opcion == '4':
            print('Gracias por jugar a nuestra generala! ')
            break
        else:
            print('Opcion invalida intente de nuevo')

mini_generala()