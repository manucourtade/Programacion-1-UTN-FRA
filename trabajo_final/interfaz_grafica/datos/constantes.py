import datos.set_up_json as setup

config = setup.cargar_datos()
HEIGHT = config['default']['ventana']['h']
WIDTH = config['default']['ventana']['w']
TITLE = config['default']['ventana']['titulo']
COLOR_FONDO = config['default']['colores']['fondo']
COLOR_TEXTO_OSCURO = config['default']['colores']['texto_oscuro']
COLOR_TEXTO_CLARO = config['default']['colores']['texto_claro']
COLOR_SECUNDARIO = config['default']['colores']['secundario']
VOLUMEN = config['default']['audio']['vol']

