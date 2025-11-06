import os

archivo = 'estadisticas/historial.csv'
archivo_json = 'estadisticas/niveles.json'

def realizar_registro(nombre_archivo, nombre, puntos):
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("=" * 30 + '\n    NOMBRE   |    PUNTAJE \n' + '=' * 30 +'\n')
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(f'   {nombre.strip():<10}|    {puntos.strip():>7}\n')


def leer_archivo_csv(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print('NO HAS JUGADO NINGUNA PARTIDA TODAVIA!')
        return
    
    with open(nombre_archivo, 'r') as archivo:
        texto = archivo.read()
    return texto


def json_tematicas(nombre_archivo):
    pass



