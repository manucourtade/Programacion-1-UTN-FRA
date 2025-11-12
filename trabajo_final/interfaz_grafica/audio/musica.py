import pygame
VOLUMEN = 0.07

MUSICA_PRINCIPAL = "audio/intro.mp3"
EFECTO_CLICK = "audio/boton_principal.wav"

VOLUMEN_MUSICA = VOLUMEN

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
    efecto = pygame.mixer.Sound(ruta)
    efecto.set_volume(VOLUMEN_MUSICA + 0.2)
    return efecto

def reproducir_efecto(efecto):
    efecto.play()