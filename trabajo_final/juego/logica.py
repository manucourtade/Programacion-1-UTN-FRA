import random
from puntaje.plantilla_puntaje import tabla_puntajes, posibles_jugadas

def tirar_dado(dados):
    # Completa los dados hasta tener 5 (solo tira los que faltan)
    while len(dados) < 5:
        dado = random.randint(1, 6)
        dados.append(dado)

valores = {
    "Uno (1)": 1,
    "Dos (2)": 2,
    "Tres (3)": 3,
    "Cuatro (4)": 4,
    "Cinco (5)": 5,
    "Seis (6)": 6
}

def ronda(valores):
    cant_categorias = 10
    turnos = 3

    tabla_puntajes()

    while cant_categorias > 0:
        print(f'\n--- INICIO DE RONDA. Categorías restantes: {cant_categorias} ---\n')
        dados = []  # reinicia los dados para cada ronda

        for turno in range(turnos):
            print(f'\n<<< TURNO JUGADOR - TIRO {turno + 1} de {turnos} >>>')
            print('-' * 40)
            print('Posición: (1\t) | (2\t) | (3\t) | (4\t) | (5\t) |')
            print('         ',('-' * 39), '|')

            
            tirar_dado(dados)

            print(f'Valor: \t {dados[0]:^5}\t  | {dados[1]:^2} \t  | {dados[2]:^2} \t  | {dados[3]:^2} \t  | {dados[4]:^2} \t  |')
          

            
            if turno <= 3:
                desea_conservar = input(
                    'Ingrese las posiciones de los dados a conservar (1-5), separadas por coma, o ENTER para tirar todos: '
                ).strip()

                if desea_conservar == "":
                    dados = []  # tirar todos
                else:
                    posiciones = desea_conservar.split(",")
                    dados_conservados = []

                    for pos in posiciones:
                        if pos.isdigit():
                            indice = int(pos) - 1
                            if 0 <= indice < len(dados):
                                dados_conservados.append(dados[indice])
                            else:
                                print('⚠️ Posición fuera de rango (1–5).')
                        else:
                            print('⚠️ Ingrese solo números válidos, por ejemplo: 1,3,5')
                            dados_conservados = []
                            break

                    dados = dados_conservados  # guarda los elegidos para el siguiente tiro
                    print(f'DADOS CONSERVADOS: {dados}')
                    if len(dados_conservados) == 5:
                        print('Has conservado los 5 dados')
                        break


        cant_categorias -= 1
