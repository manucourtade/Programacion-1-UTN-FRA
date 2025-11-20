import pygame
from render.render_pantalla import fondo_creditos, volver_menu

def pantalla_jugar(pantalla):
    fondo2 = fondo_creditos()
    
    # --- VARIABLES DE RONDA ---
    cant_categorias = 10
    turno_actual = 1
    turnos_totales = 3

    fuente_cat = pygame.font.Font(None, 40)
    fuente_turno = pygame.font.Font(None, 25)

    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            # --- CUANDO EL USUARIO APRIETE SPACE ---
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                
                turno_actual += 1
                
                # Si terminó los 3 tiros
                if turno_actual > turnos_totales:
                    turno_actual = 1
                    cant_categorias -= 1
                
                # Si no quedan categorías → fin
                if cant_categorias == 0:
                    print("¡Juego terminado!")
                    return  # → vuelve al menú

        # --- DIBUJADO ---
        pantalla.blit(fondo2, (0, 0))

        # Categorías
        txt_cat = fuente_cat.render(
            f"Categorías restantes: {cant_categorias}", True, (0, 0, 0))
        pantalla.blit(txt_cat, (20, 65))

        # Turno
        txt_turno = fuente_turno.render(
            f"Tiro actual: {turno_actual} de {turnos_totales}", True, (80, 80, 80))
        pantalla.blit(txt_turno, (20, 120))

        if volver_menu(pantalla):
            corriendo = False
        

        pygame.display.update()
        reloj.tick(30)
