import random
from puntaje.plantilla_puntaje import tabla_puntajes, posibles_jugadas, jugada_generala
from estadisticas.archivo_json_csv import realizar_registro, archivo

def tirar_dado(dados):
    while len(dados) < 5:
        dado = random.randint(1, 6)
        dados.append(dado)


def ronda():

    simbolos = {
        1: 'Pikachu',
        2: 'Bulbasur',
        3: 'Charmander',
        4: 'Squirtle',
        5: 'Snorlax',
        6: 'Gengar'
    }

    puntajes = {
        1:'--', 
        2: '--',  
        3: '--',  
        4: '--', 
        5: '--',
        6: '--',  
        7: '--',  
        8: '--', 
        9: '--',  
        10: '--'  
    }

    cant_categorias = 10
    turnos = 3


    while cant_categorias > 0:
        print(f'\n--- INICIO DE RONDA. Categorías restantes: {cant_categorias} ---\n')
        dados = []  
        for turno in range(turnos):
            print(f'\n<<< TURNO JUGADOR - TIRO {turno + 1} de {turnos} >>>')
            print('         ',('-' * 61), '|')
            print('Posición: (1\t)   | (2\t)| (3\t)     | (4\t)  | (5\t )\t|')
            print('         ',('-' * 61), '|')

            tirar_dado(dados)
            print(f'Simbolo: {simbolos[dados[0]]:^10} | {simbolos[dados[1]]:^10} | {simbolos[dados[2]]:^10} | {simbolos[dados[3]]:^10} | {simbolos[dados[4]]:^10} |')  
            print('         ',('-' * 61), '|')
            print(f'Valor: \t {dados[0]:^5}\t    | {dados[1]:^2} \t | {dados[2]:^2} \t      |    {dados[3]:^2} \t   | {dados[4]:^2} \t|')

            puntos_generala = jugada_generala(dados, turno + 1)

            if puntos_generala == 100:  
                print('\n¡GENERALA SERVIDA! Fin del juego ')
                puntos = 100
                cant_categorias = 0
                break
            elif puntos_generala == 50:  
                print('\n¡Generala! +50 puntos')
                puntos = 50

            elif turno < 3:
                desea_conservar = input(
                    'Ingrese las posiciones de los dados a conservar (1-5), separadas por coma, o ENTER para tirar todos: '
                ).strip()

                if desea_conservar == "":
                    dados = []  
                else:
                    posiciones = desea_conservar.split(",")
                    dados_conservados = []

                    for pos in posiciones:
                        if pos.isdigit():
                            indice = int(pos) - 1
                            if 0 <= indice < len(dados):
                                dados_conservados.append(dados[indice])
                            else:
                                print('Posición fuera de rango (1–5).')
                        else:
                            print('Ingrese solo números válidos, por ejemplo: 1,3,5')
                            dados_conservados = []
                            break

                    dados = dados_conservados
                    print(f'DADOS CONSERVADOS: {dados}')
                    if len(dados) == 5:
                        print('Has conservado los 5 dados')
                        break
        categoria, puntos = posibles_jugadas(dados, puntajes)
        puntajes[categoria] = puntos  
        total_puntos = tabla_puntajes(puntajes)
        cant_categorias -= 1

        
    nombre = ''
    while nombre == '':
        nombre = input('Ingrese su nombre para registrar: ').strip().title()
        if nombre ==  '':
            print('No puede ingresar nombres en blanco!')

    total_puntos = str(total_puntos)
    realizar_registro(archivo, nombre, total_puntos)
    print(f"\nRegistro guardado correctamente: {nombre} -> {total_puntos} puntos.\n")
        


