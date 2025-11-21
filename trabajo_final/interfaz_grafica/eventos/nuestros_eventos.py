import pygame
from audio.musica import cargar_efecto, reproducir_efecto, EFECTO_CLICK

efecto = cargar_efecto(EFECTO_CLICK)

def gestionar_eventos(evento, pantalla_actual, botones):
    # Si estás en el menú
    if pantalla_actual == "menu":
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botones:
                if botones["jugar"].collidepoint(evento.pos):
                    reproducir_efecto(efecto)
                    return "jugar"
                if botones["opciones"].collidepoint(evento.pos):
                    reproducir_efecto(efecto)
                    return "opciones"
                if botones["creditos"].collidepoint(evento.pos):
                    reproducir_efecto(efecto)
                    return "creditos"
                if botones["estadisticas"].collidepoint(evento.pos):
                    reproducir_efecto(efecto)
                    return "estadisticas"
                if botones["salir"].collidepoint(evento.pos):
                    reproducir_efecto(efecto)
                    return "salir"

    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
        return "menu"

    return pantalla_actual