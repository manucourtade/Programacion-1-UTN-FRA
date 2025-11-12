import datos.set_up_json as setup

config = setup.cargar_datos()
HEIGHT = config['default']['ventana']['altura']
WIDTH = config['default']['ventana']['ancho']
TITLE = config['default']['ventana']['titulo']
COLOR_FONDO = config['default']['colores']['fondo']
COLOR_TEXTO_OSCURO = config['default']['color']['texto_oscuro']
COLOR_TEXTO_CLARO = config['default']['color']['texto_claro']
COLOR_TEXTO_SECUNDARIO = config['default']['color']['secundario']
VOLUMEN = config['default']['volumen']

