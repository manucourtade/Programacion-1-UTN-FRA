import pygame
from datos.constantes import VOLUMEN

MUSICA_PRINCIPAL = "assets/musica_pokemon.mp3"
EFECTO_CLICK = "assets/pokemon_boton.wav"

def reproducir_musica(ruta, loop=True):
    pygame.mixer.music.load(ruta)
    if loop:
        cantidad_reproducciones = -1
    else:
        cantidad_reproducciones = 0
    pygame.mixer.music.play(cantidad_reproducciones)

def detener_musica():
    pygame.mixer.music.stop()

def pausar_musica():
    pygame.mixer.music.pause()

def reanudar_musica():
    pygame.mixer.music.unpause()

def cambiar_volumen(valor):
    pygame.mixer.music.set_volume(valor)

def cargar_efecto(ruta):
    pygame.mixer.init()
    efecto = pygame.mixer.Sound(ruta)
    efecto.set_volume(VOLUMEN + 0.7)
    return efecto

def reproducir_efecto(efecto):
    efecto.play()