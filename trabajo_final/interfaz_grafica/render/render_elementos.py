import pygame
from datos.constantes import HEIGHT, WIDTH

LOGO = pygame.image.load("assets/logo.png")
LOGO = pygame.transform.scale(LOGO, (500, 500))

FONDO = pygame.image.load("assets/pokemonfondo.jpg")
FONDO = pygame.transform.scale(FONDO, (WIDTH, HEIGHT))

def logo_juego():
    return LOGO

def fondo_menu():
    return FONDO

def crear_boton_rect(superficie, x, y, ancho, alto, texto, color_fondo, color_texto):
    fuente = pygame.font.Font(None, 40)
    rectangulo = pygame.Rect(x, y, ancho, alto)

    pygame.draw.rect(superficie, color_fondo, rectangulo, border_radius=10)

    texto_img = fuente.render(texto, True, color_texto)
    texto_x = x + (ancho - texto_img.get_width()) // 2
    texto_y = y + (alto - texto_img.get_height()) // 2

    superficie.blit(texto_img, (texto_x, texto_y))

    return rectangulo


# Función para dibujar en pantalla un botón a partir de una imagen
def crear_boton_imagen(superficie, x, y, ancho, alto, ruta_imagen):
    imagen = pygame.image.load(ruta_imagen)
    imagen = pygame.transform.scale(imagen, (ancho, alto))

    forma = imagen.get_rect(topleft=(x, y))
    superficie.blit(imagen, forma.topleft)

    return forma