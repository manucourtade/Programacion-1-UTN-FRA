

def tabla_puntajes():
    print('-' * 40)
    print('\t PLANTILLA DE PUNTAJES')
    print('-' * 40)

    print('[1]: Unos       \t: ')
    print('[2]: Doses      \t: ')
    print('[3]: Treses     \t: ')
    print('[4]: Cuatros     \t: ')
    print('[5]: Cincos     \t: ')
    print('[6]: Seises     \t: ')
    print('[7]: Escalera(20)\t: ')
    print('[8]: Full(30)   \t: ')
    print('[9]: Poker(40)   \t: ')
    print('[10]: Generala(50)\t: ')
    print('-' * 30)
    print('PUNTAJE TOTAL: ')
    print('-' * 30)


def jugada_uno_al_seis(mis_dados, idx_categoria):
    puntos = 0
    for dado in mis_dados:
        dado = int(dado)
        if dado == idx_categoria:
            puntos += idx_categoria
    return puntos

def jugada_escalera(mis_dados):
    puntos = 0
    mis_dados_ordenados = sorted(mis_dados)
    if mis_dados_ordenados == [1, 2, 3, 4, 5] or mis_dados_ordenados == [2, 3, 4, 5, 6]:
        puntos = 20
    return puntos


def jugada_full(mis_dados):
    puntos = 0
    repeticiones = {}  

    for dado in mis_dados:
        if dado in repeticiones:
            repeticiones[dado] += 1
        else:
            repeticiones[dado] = 1

    tiene_tres = False
    tiene_dos = False

    for valor in repeticiones.values():
        if valor == 3:
            tiene_tres = True
        elif valor == 2:
            tiene_dos = True

    if tiene_tres and tiene_dos:
        puntos = 30

    return puntos

def jugada_poker(mis_dados):
    puntos = 0
    repeticiones = {}  

    for dado in mis_dados:
        if dado in repeticiones:
            repeticiones[dado] += 1
        else:
            repeticiones[dado] = 1


    for cantidad in repeticiones.values():
        if cantidad == 4:
            puntos = 40
            break

    return puntos



def jugada_generala(mis_dados,tiro):
    puntos = 0
    repeticiones = {}  

    for dado in mis_dados:
        if dado in repeticiones:
            repeticiones[dado] += 1
        else:
            repeticiones[dado] = 1


    for cantidad in repeticiones.values():
        if cantidad == 5:
                if tiro == 1:
                    print(" ¡Generala servida! ¡Ganaste automáticamente!")
                    puntos = 100
                else:
                    puntos = 50
    return puntos


def posibles_jugadas(mis_dados):
    print('--- POSIBLES JUGADAS ---')
    print('[1]: Unos       \t-> ')
    print('[2]: Doses      \t-> ')
    print('[3]: Treses     \t-> ')
    print('[4]: Cuatros     \t-> ')
    print('[5]: Cincos     \t-> ')
    print('[6]: Seises     \t-> ')
    print('[7]: Escalera(20)\t-> ')
    print('[8]: Full(30)   \t-> ')
    print('[9]: Poker(40)   \t-> ')
    print('[10]: Generala(50)\t-> ')

    elegir_cat = input('Seleccione el numero de la categoria para anotar: ').strip()

    if elegir_cat.isdigit():
        elegir_cat = int(elegir_cat)
    else:
        print('Ingreso inválido')
        return

    if 1 <= elegir_cat <= 6:
        puntos = jugada_uno_al_seis(mis_dados, elegir_cat)
        print(f"Puntos para la categoría {elegir_cat}: {puntos}")

    elif elegir_cat == 7:
        puntos = jugada_escalera(mis_dados)
        print(f"Puntos para Escalera: {puntos}")

    elif elegir_cat == 8:
        puntos = jugada_full(mis_dados)
        print(f"Puntos para Full: {puntos}")

    elif elegir_cat == 9:
        puntos = jugada_poker(mis_dados)
        print(f"Puntos para Póker: {puntos}")

    elif elegir_cat == 10:
        
        puntos = jugada_generala(mis_dados, )
        print(f"Puntos para Generala: {puntos}")

    else:
        print('Categoría inválida')


    

