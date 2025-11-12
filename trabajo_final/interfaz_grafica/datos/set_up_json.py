import json
import os

config__ = {
    'default': {
        
    'ventana': {'w': 800, 'h': 600, 'titulo': 'Generala GO!'},
    'audio': {'vol': 0.07},
    'colores': {'fondo': [196, 101, 86], 'primario': [], 'secundario': [], 'texto_claro': [], 'texto_oscuro': []}

    }
} 

json_archive = 'set_up.json'

def guardar_datos(archivo, config):
    with open(archivo, 'w') as datos:
        json.dump(config, datos, indent=4)

def cargar_datos():
    if os.path.exists(json_archive) or os.path.getsize(json_archive) == 0:
        guardar_datos(config__)
        return config__
    
    with open(json_archive, 'r') as datos:
        datos_cargados = json.load(datos)

        if 'default' not in datos_cargados:
            guardar_datos(config__)
            return config__
    
    return datos_cargados

#guardar_datos(json_archive, config__)