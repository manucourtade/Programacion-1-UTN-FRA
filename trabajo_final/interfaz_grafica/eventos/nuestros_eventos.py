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

    # ✔ NUEVO: si estás en créditos y presionás ESC → volver al menú
    if pantalla_actual == "creditos":
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            return "menu"

    # Podés agregar lo mismo en otras pantallas si querés que ESC vuelva al menú
    if pantalla_actual == "opciones":
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            return "menu"
    
    if pantalla_actual == "jugar":
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            return "menu"
        
    if pantalla_actual == "estadisticas":
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            return "menu"


    return pantalla_actual