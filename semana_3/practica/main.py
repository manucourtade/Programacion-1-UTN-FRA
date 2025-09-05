from funciones import *

while True:
    print('''
---Menu Principal---
1. Registrar turno
2. Calcular pago
3. Mostrar mensaje de agradecimiento
4. Salir
''')

    opcion = input(
'Ingrese una opcion => ')
    
    if opcion == '1':
        no, tu = pedir_turno()
        print(registrar_turno(no, tu))

    elif opcion == '2':
        hs, tu = pedir_pago()
        print(calc_pago(hs, tu))

    elif opcion == '3':
        print(mensaje_agradecimiento(no))
        
    elif opcion == '4':
        break
    else:
        print('Ingrese una opcion correcta!')
