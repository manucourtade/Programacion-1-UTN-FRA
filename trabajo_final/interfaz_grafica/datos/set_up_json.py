import json
import os

config__ = {
    'default': {
        
    'ventana': {'w': 1000, 'h': 750, 'titulo': 'Generala GO!'},
    'audio': {'vol': 0.03},
    'colores': {'fondo': [196, 101, 86], 'primario': [], 'secundario': [255, 215, 0], 'texto_claro': [255, 255, 255], 'texto_oscuro': [0, 0, 0]}

    }
} 

json_archive = 'datos/set_up.json'

def guardar_datos(archivo, config):
    with open(archivo, 'w') as datos:
        json.dump(config, datos, indent=4)

def cargar_datos():
    if os.path.exists(json_archive) or os.path.getsize(json_archive) == 0:
        guardar_datos(json_archive, config__)
        return config__
    
    with open(json_archive, 'r') as datos:
        datos_cargados = json.load(datos)

        if 'default' not in datos_cargados:
            guardar_datos(config__)
            return config__
    
    return datos_cargados

#guardar_datos(json_archive, config__)