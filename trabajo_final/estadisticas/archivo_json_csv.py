import os
import json

archivo = 'estadisticas/historial.csv'
archivo_json = 'niveles.json'

def realizar_registro(nombre_archivo, nombre, puntos):
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("=" * 30 + '\n    NOMBRE   |    PUNTAJE \n' + '=' * 30 +'\n')
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(f'   {nombre.strip():<10}|    {puntos.strip():>7}\n')

def historial(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print('NO HAS JUGADO NINGUNA PARTIDA TODAVIA!')
        return
    
    with open(nombre_archivo, 'r') as archivo:
        texto = archivo.read()
    return texto

def leer_archivo_csv(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print('NO HAS JUGADO NINGUNA PARTIDA TODAVÍA!')
        return 

    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()[3:] 
        puntajes = []

        for linea in lineas:
            if '|' in linea:
                partes = linea.strip().split('|')
                nombre = partes[0].strip()
                puntos = partes[1].strip()

                if puntos.isdigit():
                    puntos = int(puntos)
                    puntajes.append((nombre, puntos))

    return puntajes


def ordenar_10_mejores(nombre_archivo):
    puntajes = leer_archivo_csv(nombre_archivo)
    if not puntajes:
        return 

    n = len(puntajes)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if puntajes[j][1] < puntajes[j + 1][1]:
                puntajes[j], puntajes[j + 1] = puntajes[j + 1], puntajes[j]

    top_10 = puntajes[:10]

    print("\n" + "=" * 30)
    print("        TOP 10 JUGADORES")
    print("=" * 30)
    for nombre, puntos in top_10:
        print(f'   {nombre:<10}|    {puntos:>7}')
    print("=" * 30)


def json_tematicas(nombre_archivo):
    simbolos = {
    '1': 'Pikachu',
    '2': 'Bulbasur',
    '3': 'Charmander',
    '4': 'Squirtle',
    '5': 'Snorlax',
    '6': 'Gengar',
    'escalera': '(20 pts) Secuencia 1-2-3-4-5 o 2-3-4-5-6',
    'full': '(30 pts) Tres dados iguales y otros dos iguales',
    'poker': '(40 pts) Cuatro dados iguales',
    'generala': '(50 pts) Cinco dados iguales. Si es servida (en el primer tiro), gana el juego automáticamente y suma 100 puntos'
}
    lista_personajes = []
    lista_personajes.append(simbolos)

    with open(nombre_archivo, 'w', encoding= 'utf-8') as niveles:
        json.dump(lista_personajes, niveles, indent=4)
    
    print(f"Archivo '{nombre_archivo}' creado con éxito ")

def json_background(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return [] 
    
    with open(nombre_archivo, "r", encoding="utf-8") as niveles:
        lista_personajes = json.load(niveles) 
    
    return lista_personajes

json_tematicas(archivo_json)

def mostrar_archivo_json():
    pokemones_categoria = json_background(archivo_json)
    simbolos = pokemones_categoria[0]
    for i, j in simbolos.items():
        print(f'Valor: {i} - Simbolo {j}')

mostrar_archivo_json()


