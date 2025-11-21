

def tabla_puntajes(puntajes):
    print('-' * 40)
    print('\t PLANTILLA DE PUNTAJES')
    print('-' * 40)

 
    print(f'[1]: Unos        \t: {puntajes[1]}')
    print(f'[2]: Doses       \t: {puntajes[2]}')
    print(f'[3]: Treses      \t: {puntajes[3]}')
    print(f'[4]: Cuatros     \t: {puntajes[4]}')
    print(f'[5]: Cincos      \t: {puntajes[5]}')
    print(f'[6]: Seises      \t: {puntajes[6]}')
    print(f'[7]: Escalera(20)\t: {puntajes[7]}')
    print(f'[8]: Full(30)    \t: {puntajes[8]}')
    print(f'[9]: Poker(40)   \t: {puntajes[9]}')
    print(f'[10]: Generala(50)\t: {puntajes[10]}')
    print('-' * 30)

    total = 0
    for i in puntajes:
        if puntajes[i] != '--':
            total = total + puntajes[i]

    print('PUNTAJE TOTAL:', total)
    print('-' * 30)
    return total


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



def jugada_generala(mis_dados, tiro):
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
                return 100
            return 50
            
                
    return 0

def posibles_jugadas(mis_dados, puntajes):
    print('--- POSIBLES JUGADAS ---')

    jugadas = {
        1: jugada_uno_al_seis(mis_dados, 1),
        2: jugada_uno_al_seis(mis_dados, 2),
        3: jugada_uno_al_seis(mis_dados, 3),
        4: jugada_uno_al_seis(mis_dados, 4),
        5: jugada_uno_al_seis(mis_dados, 5),
        6: jugada_uno_al_seis(mis_dados, 6),
        7: jugada_escalera(mis_dados),
        8: jugada_full(mis_dados),
        9: jugada_poker(mis_dados),
        10: jugada_generala(mis_dados, 3)
    }

    print(f'[1]: Unos        -> {jugadas[1]}')
    print(f'[2]: Doses       -> {jugadas[2]}')
    print(f'[3]: Treses      -> {jugadas[3]}')
    print(f'[4]: Cuatros     -> {jugadas[4]}')
    print(f'[5]: Cincos      -> {jugadas[5]}')
    print(f'[6]: Seises      -> {jugadas[6]}')
    print(f'[7]: Escalera    -> {jugadas[7]}')
    print(f'[8]: Full        -> {jugadas[8]}')
    print(f'[9]: Poker       -> {jugadas[9]}')
    print(f'[10]: Generala   -> {jugadas[10]}')


    while True:
        elegir_cat = input('Seleccione el número de la categoría para anotar: ').strip()
        if elegir_cat.isdigit():
            elegir_cat = int(elegir_cat)
            if 1 <= elegir_cat <= 10:
                if puntajes[elegir_cat] == '--':
                    puntos = jugadas[elegir_cat]
                    print(f'\nAnotaste {puntos} puntos en la categoría {elegir_cat}.')
                    return elegir_cat, puntos  
                else:
                    print('Esa categoría ya fue usada, elegí otra.')
            else:
                print('Número fuera de rango (1–10).')
        else:
            print('Ingreso inválido, escribí un número del 1 al 10.')


