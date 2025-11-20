import json
import os

# Ruta absoluta al archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_archive = os.path.join(BASE_DIR, "set_up.json")

config__ = {
    'default': {
        'ventana': {'w': 1000, 'h': 750, 'titulo': 'Generala GO!'},
        'audio': {'vol': 0.03},
        'colores': {
            'fondo': [196, 101, 86],
            'primario': [],
            'secundario': [255, 215, 0],
            'texto_claro': [255, 255, 255],
            'texto_oscuro': [0, 0, 0]
        }
    }
}

def guardar_datos(archivo, config):
    with open(archivo, 'w') as datos:
        json.dump(config, datos, indent=4)

def cargar_datos():
    # Si NO existe → crear archivo con config por defecto
    if not os.path.exists(json_archive):
        guardar_datos(json_archive, config__)
        return config__

    # Si existe pero está vacío → restaurar valores por defecto
    if os.path.getsize(json_archive) == 0:
        guardar_datos(json_archive, config__)
        return config__

    # Si existe y tiene datos → cargar
    with open(json_archive, 'r') as datos:
        datos_cargados = json.load(datos)

    # Si el archivo está corrupto o falta 'default'
    if 'default' not in datos_cargados:
        guardar_datos(json_archive, config__)
        return config__

    return datos_cargados
