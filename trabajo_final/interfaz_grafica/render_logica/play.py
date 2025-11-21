import pygame
import random
from render.render_pantalla import fondo_creditos, volver_menu
from puntaje.plantilla_puntaje import jugada_generala, posibles_jugadas, tabla_puntajes
from juego.logica import tirar_dado

imagen_dado_1 = pygame.image.load("assets/pikachu.png")
imagen_dado_2 = pygame.image.load("assets/bulbasur.png")
imagen_dado_3 = pygame.image.load("assets/charmander.png")
imagen_dado_4 = pygame.image.load("assets/squirtle.png")
imagen_dado_5 = pygame.image.load("assets/snorlax.png")
imagen_dado_6 = pygame.image.load("assets/gengar.png")

pokemon_imagenes = [
    imagen_dado_1,
    imagen_dado_2,
    imagen_dado_3,
    imagen_dado_4,
    imagen_dado_5,
    imagen_dado_6
]

for i in range(len(pokemon_imagenes)):
    pokemon_imagenes[i] = pygame.transform.scale(pokemon_imagenes[i], (250, 250))


def pantalla_jugar(pantalla):
    fondo2 = fondo_creditos()

    # Datos de la ronda
    cant_categorias = 10
    turno_actual = 1
    turnos_totales = 3

    dados = []   # almacena los 5 dados actuales

    fuente = pygame.font.Font(None, 40)
    fuente_fin = pygame.font.Font(None, 50)

    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            # ESPACIO = tirar dados
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:

                dados = []  
                tirar_dado(dados)   # ← CORRECTO, ANTES ESTABA MAL

                # Evaluar generala
                puntos_generala = jugada_generala(dados, turno_actual)

                if puntos_generala == 100:
                    pantalla.blit(
                        fuente_fin.render("¡GENERALA SERVIDA! Fin del juego", True, (0, 0, 0)),
                        (200, 400)
                    )
                    pygame.display.update()
                    pygame.time.wait(2000)
                    return "menu"

                if puntos_generala == 50:
                    print("Generala normal (+50 puntos)")

                # Avanzar turno
                turno_actual += 1

                if turno_actual > turnos_totales:
                    turno_actual = 1
                    cant_categorias -= 1

                # Si no quedan categorías → fin
                if cant_categorias == 0:
                    pantalla.blit(
                        fuente_fin.render("¡Juego terminado!", True, (0, 0, 0)),
                        (300, 400)
                    )
                    pygame.display.update()
                    pygame.time.wait(2000)
                    return "menu"

        # --- DIBUJAR ---
        pantalla.blit(fondo2, (0, 0))

        # Texto superior
        texto_cat = fuente.render(f"Categorías restantes: {cant_categorias}", True, (0, 0, 0))
        pantalla.blit(texto_cat, (20, 70))

        texto_turno = fuente.render(f"Tiro actual: {turno_actual} de {turnos_totales}", True, (80, 80, 80))
        pantalla.blit(texto_turno, (20, 120))

        x_base = 10
        y_base = 250

        for i, valor in enumerate(dados):

            imagen = pokemon_imagenes[valor - 1]
            x = x_base + i * 250
            pantalla.blit(imagen, (x, y_base))

        if volver_menu(pantalla):
            return "menu"

        pygame.display.update()
        reloj.tick(30)
