import pygame
import os
from datos.constantes import HEIGHT, WIDTH

# Carpeta raíz del proyecto (interfaz_grafica)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- LOGO ---
ruta_logo = os.path.join(BASE_DIR, "assets", "logo.png")
LOGO = pygame.image.load(ruta_logo)
LOGO = pygame.transform.scale(LOGO, (500, 500))

# --- FONDO ---
ruta_fondo = os.path.join(BASE_DIR, "assets", "pokemonfondo.jpg")
FONDO = pygame.image.load(ruta_fondo)
FONDO = pygame.transform.scale(FONDO, (WIDTH, HEIGHT))

# --- fondo creditos ---
ruta_fondo = os.path.join(BASE_DIR, "assets", "Pueblo_Paleta.jpg")
FONDO_CREDITOS = pygame.image.load(ruta_fondo)
FONDO_CREDITOS = pygame.transform.scale(FONDO_CREDITOS, (WIDTH, HEIGHT))
# Devuelven las superficies
def logo_juego():
    return LOGO

def fondo_menu():
    return FONDO

def fondo_creditos():
    return FONDO_CREDITOS

# --- BOTÓN RECTÁNGULO ---
def crear_boton_rect(superficie, x, y, ancho, alto, texto, color_fondo, color_texto):
    fuente = pygame.font.Font(None, 40)
    rectangulo = pygame.Rect(x, y, ancho, alto)

    pygame.draw.rect(superficie, color_fondo, rectangulo, border_radius=10)

    texto_img = fuente.render(texto, True, color_texto)
    texto_x = x + (ancho - texto_img.get_width()) // 2
    texto_y = y + (alto - texto_img.get_height()) // 2

    superficie.blit(texto_img, (texto_x, texto_y))

    return rectangulo

# --- BOTÓN IMAGEN ---
def crear_boton_imagen(superficie, x, y, ancho, alto, ruta_imagen):
    ruta = os.path.join(BASE_DIR, ruta_imagen)  # permite poner rutas como "assets/boton.png"
    imagen = pygame.image.load(ruta)
    imagen = pygame.transform.scale(imagen, (ancho, alto))

    forma = imagen.get_rect(topleft=(x, y))
    superficie.blit(imagen, forma.topleft)
