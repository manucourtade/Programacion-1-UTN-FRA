import pygame
from audio.musica import cargar_efecto, reproducir_efecto, EFECTO_CLICK


def gestionar_eventos(evento, pantalla_actual, botones):
    # Validamos que tengamos botones en pantalla:
    if botones is None:
        return pantalla_actual
    
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        pos = pygame.mouse.get_pos()

        for boton in botones:
            if boton["rect"].collidepoint(pos):
                print("CLICK DETECTADO SOBRE: ", boton["accion"])
                efecto = cargar_efecto(EFECTO_CLICK)
                reproducir_efecto(efecto)
                accion = boton["accion"]

                if pantalla_actual == "menu":
                    if accion == "jugar":
                        return "jugar"
                    
                    if accion == "opciones":
                        return "opciones"
                    
                    if accion == "estadisticas":
                        return "estadisticas"
                    
                    if accion == "creditos":
                        return "creditos"
                    
                    if accion == "salir":
                        return "salir"
                    
    return pantalla_actual