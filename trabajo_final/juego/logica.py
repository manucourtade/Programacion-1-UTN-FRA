import random

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

    while cant_categorias > 0:
        print(f'\n--- INICIO DE RONDA. Categorías restantes: {cant_categorias} ---\n')

        dados = [] 

        for turno in range(1, turnos + 1):
            print(f'<<< TURNO JUGADOR - TIRO {turno} de 3 >>>')
            print('-' * 40)
            print('Posición: (1\t) | (2\t) | (3\t) | (4\t) | (5\t) |')
            print('-' * 40)

           
            while len(dados) < 5:
                dado = random.randint(1, 6)
                dados.append(dado)

            print(f'Dados actuales: {dados}\n')

           
            if turno < 3:
                desea_conservar = input('Ingrese la posición de los dados a conservar (1-5), separados por coma, o ENTER para no conservar: ').strip()

                if desea_conservar == "":
                    dados = [] 
                else:
                    posiciones = desea_conservar.split(",")
                    dados_conservados = []

                    for pos in posiciones:
                        pos = pos.strip()
                        if pos.isdigit():
                            indice = int(pos) - 1
                            if 0 <= indice < 5:
                                dados_conservados.append(dados[indice])

                    dados = dados_conservados

        print(f'Tirada final: {dados}')
        cant_categorias -= 1


ronda(valores)


