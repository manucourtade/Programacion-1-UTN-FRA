import random
from puntaje.plantilla_puntaje import tabla_puntajes
from validaciones.validar_jugadas import dados_invalidos
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

        dados = [] 

        for turno in range(turnos):
            print(f'<<< TURNO JUGADOR - TIRO {turno + 1} de 3 >>>')
            print('-' * 40)
            print('Posición: (1\t) | (2\t) | (3\t) | (4\t) | (5\t) |')
            print('         ',('-' * 39), '|')

            # Completa los dados que falten hasta tener 5
            while len(dados) < 5:
                dado = random.randint(1, 6)
                dados.append(dado)

            # Mostrar los valores actuales
            print(f'Valor: \t {dados[0]:^5}\t  | {dados[1]:^2} \t  | {dados[2]:^2} \t  | {dados[3]:^2} \t  | {dados[4]:^2} \t  |')

            # Si no es el último turno, preguntar qué dados conservar
            if turno < 3:
                desea_conservar = input(
            'Ingrese las posiciones de los dados a conservar (1-5), separadas por coma, o ENTER para tirar todos: ').strip()

                if desea_conservar == "":
                    dados = []  
                else:
                    posiciones = desea_conservar.split(",")
                    dados_conservados = []

                    for pos in posiciones:
                        pos = pos.strip()
                        if pos.isdigit():
                            indice = int(pos) - 1
                            if dados_invalidos(pos):
                                dados_conservados.append(dados[indice])
                            else:
                                print('Posición fuera de rango (1–5).')
                        else:
                            print('Ingrese solo números, por ejemplo: 1,3,5')
                            dados_conservados = []

                    dados = dados_conservados
            print(f'TUS DADOS: {dados}')
            
            


        cant_categorias -= 1

ronda(valores)
