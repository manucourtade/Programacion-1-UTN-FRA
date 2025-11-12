import pygame 
import datos.constantes as con
from render.render_pantalla import pantalla_principal, pantalla_opciones
from audio.musica import reproducir_musica, MUSICA_PRINCIPAL
from eventos import nuestros_eventos


pygame.init()

pantalla = pygame.display.set_mode((con.WIDTH, con.HEIGHT))
pygame.display.set_caption(con.TITLE)
reloj = pygame.time.Clock()
FPS = 60
pantalla_actual = "menu"
musica_actual = None

botones = None

ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Lógica de juego
    if pantalla_actual == "menu":
        if musica_actual != "menu":
            reproducir_musica(MUSICA_PRINCIPAL)
            musica_actual = "menu"
        botones = pantalla_principal(pantalla)
    elif pantalla_actual == "jugar":
        botones = None
    elif pantalla_actual == "opciones":
        botones = pantalla_opciones(pantalla)
    elif pantalla_actual == "creditos":
        botones = None
    elif pantalla_actual == "estadisticas":
        botones = None
    elif pantalla_actual == "salir":
        pass
    
    # Actualización de pantalla
    pygame.display.flip()

    # Velocidad de frames por segundo
    reloj.tick(FPS)

# Finalización del programa total
pygame.quit()