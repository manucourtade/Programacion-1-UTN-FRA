import pygame
import random

# Tu lógica original
from puntaje.plantilla_puntaje import tabla_puntajes, posibles_jugadas, jugada_generala
from estadisticas.archivo_json_csv import realizar_registro, archivo

pygame.init()

ANCHO = 900
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
FUENTE = pygame.font.SysFont(None, 36)


# ===============================================
# CARGAR IMÁGENES (las que pasaste)
# ===============================================
imagenes = {
    1: pygame.image.load("assets/pikachu.png"),
    2: pygame.image.load("assets/bulbasur.png"),
    3: pygame.image.load("assets/charmander.png"),
    4: pygame.image.load("assets/squirtle.png"),
    5: pygame.image.load("assets/snorlax.png"),
    6: pygame.image.load("assets/gengar.png"),
}

# Escalar todas
for i in imagenes:
    imagenes[i] = pygame.transform.scale(imagenes[i], (120, 120))


# ===============================================
# FUNCIONES GRAFICAS SIMPLES
# ===============================================
def dibujar_texto(texto, x, y):
    t = FUENTE.render(texto, True, (255, 255, 255))
    PANTALLA.blit(t, (x, y))


def boton(x, y, w, h, texto):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(PANTALLA, (70, 70, 180), rect)
    txt = FUENTE.render(texto, True, (255, 255, 255))
    PANTALLA.blit(txt, (x + 10, y + 10))
    return rect


def dibujar_dados(dados, seleccionados):
    posiciones = [50, 200, 350, 500, 650]

    for i in range(5):
        x = posiciones[i]

        # Si seleccionado → marco verde
        if seleccionados[i] == True:
            pygame.draw.rect(PANTALLA, (0, 255, 0), (x - 5, 195, 130, 130), 4)

        # Dibujo imagen según número del dado
        valor = dados[i]
        PANTALLA.blit(imagenes[valor], (x, 200))


# ===============================================
# INTERFAZ PRINCIPAL DEL JUEGO
# ===============================================
def interfaz_generala():

    # igual que tu ronda()
    puntajes = {
        1:'--', 2:'--', 3:'--', 4:'--', 5:'--',
        6:'--', 7:'--', 8:'--', 9:'--', 10:'--'
    }

    categorias = 10

    while categorias > 0:

        # DADOS VACÍOS
        dados = []
        for i in range(5):
            dados.append(random.randint(1, 6))

        # Seleccionados en False
        seleccionados = []
        for i in range(5):
            seleccionados.append(False)

        turnos = 3

        # =============== TRES TURNOS ===============
        for turno in range(turnos):

            turno_ok = False

            while turno_ok == False:

                # DIBUJAR PANTALLA
                PANTALLA.fill((40, 40, 70))

                dibujar_texto("Categorías restantes: " + str(categorias), 50, 20)
                dibujar_texto("Turno " + str(turno + 1) + " de 3", 50, 60)

                dibujar_dados(dados, seleccionados)

                b_tirar = boton(50, 500, 200, 50, "TIRAR")
                b_ok = boton(300, 500, 200, 50, "CONFIRMAR")

                pygame.display.flip()

                # EVENTOS
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = event.pos

                        # CLICK EN DADOS
                        posiciones = [50, 200, 350, 500, 650]
                        for i in range(5):
                            rect_dado = pygame.Rect(posiciones[i], 200, 120, 120)
                            if rect_dado.collidepoint(mx, my):
                                if seleccionados[i] == False:
                                    seleccionados[i] = True
                                else:
                                    seleccionados[i] = False

                        # CLICK EN TIRAR
                        if b_tirar.collidepoint(mx, my):
                            # tira solo los no seleccionados
                            for i in range(5):
                                if seleccionados[i] == False:
                                    dados[i] = random.randint(1, 6)
                            turno_ok = True

                        # CLICK EN CONFIRMAR
                        if b_ok.collidepoint(mx, my):
                            turno_ok = True

            # ---- EVALUAR GENERALA ----
            puntos_generala = jugada_generala(dados, turno + 1)

            if puntos_generala == 100:
                print("GENERALA SERVIDA")
                return

            if puntos_generala == 50:
                print("Generala normal (+50)")

        # ============================
        # FIN DE los 3 turnos: asignar categoría
        # ============================
        categoria, puntos = posibles_jugadas(dados, puntajes)
        puntajes[categoria] = puntos
        tabla_puntajes(puntajes)

        categorias -= 1

    # FIN DEL JUEGO
    nombre = input("Ingresa nombre: ")
    realizar_registro(archivo, nombre, str(tabla_puntajes(puntajes)))


# EJECUTAR
interfaz_generala()
pygame.quit()
