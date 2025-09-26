

def ingreso_personas():
    nombres = [''] * 10
    puntuaciones = [0] * 10
    comentarios = [''] * 10

    salir = 's'
    contador_pers = 0
    while salir == 's' and contador_pers < 10:
        for i in range(len(nombres)):
            while True:
                nombre = input('\nIngrese su nombre: ')
                if nombre == '':
                    print('No puede estar en blanco!')
                else:
                    nombres[i] = nombre
                    break

            while True:
                puntuacion = int(input('\nIngrese su puntuación de satisfacción (1 a 10): '))
                if not (1 <= puntuacion <= 10):
                    print('Solamente puntuaciones del rango 1-10!')
                else:
                    puntuaciones[i] = puntuacion
                    break


            while True:
                comentario = input('\nIngrese un comentario sobre su experiencia: ')
                if comentario == '':
                    print('No puede estar en blanco!')
                else:
                    comentarios[i] = comentario
                    break
            
            print(f'\nParticipante {i+1}:\nNombre: {nombres[i]}\nPuntuacion {puntuaciones[i]}\nComentario: {comentarios[i]}')

            contador_pers += 1
            salir = input('¿Desea ingresar otro participante? (s/n): ').lower()

            if salir == 'n' or contador_pers == 10:
                print('\n¡Gracias!\n')
                break

    return nombres, puntuaciones, comentarios

def mostrar_part_promedio(nombres, puntuaciones, comentarios):
    suma = 0 
    contador = 0
    for i in range(len(nombres)):
        if nombres[i] == '':
            break

        print(f'''
Participante {i + 1}:
NOMBRE: {nombres[i]}
PUNTUACION: {puntuaciones[i]}
COMENTARIO: "{comentarios[i]}"\n''')

        suma += puntuaciones[i]
        contador += 1
    promedio = suma/contador
    print(f'PROMEDIO GENERAL: {promedio:.2f}')

def ordenar_participantes(part, punt, coment):
    tam = len(part)
    for i in range(tam - 1):
        if part[i] == '':
            break
        for j in range(tam - i - 1):
            if punt[j] < punt[j + 1]:
                part[j], part[j + 1] = part[j + 1], part[j]
                punt[j], punt[j + 1] = punt[j + 1], punt[j]
                coment[j], coment[j + 1] = coment[j + 1], coment[j]

    print("\nLISTA ORDENADA:\n")
    for idx in range(tam):
        if part[idx] != '' and punt[idx] != 0:
            print(f"Participante {idx + 1}:")
            print(f"  NOMBRE: {part[idx]}")
            print(f"  PUNTUACION: {punt[idx]}")
            print(f"  COMENTARIO: \"{coment[idx]}\"\n")

            

def menu():   
    while True:
        print("--- Menú Encuesta de Satisfacción ---")
        print("1. Ingresar participantes")
        print("2. Mostrar participantes y promedio")
        print("3. Ordenar participantes por puntuación")
        print("4. Salir")
        seleccion = input("Seleccione una opción (1-4): ")
        if seleccion == "1":
            nombre, puntuacion, comentario = ingreso_personas()
        elif seleccion == "2":
            mostrar_part_promedio(nombre, puntuacion, comentario)
        elif seleccion == "3":
            ordenar_participantes(nombre, puntuacion, comentario)
        elif seleccion == "4":
            print('ADIOS!!')
            break
        else:
            print("Opción inválida. Intente nuevamente.")


menu()
    