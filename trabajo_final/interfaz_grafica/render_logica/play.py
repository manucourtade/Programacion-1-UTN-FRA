import pygame
from trabajo_final.juego.logica import tirar_dado
import random

pygame.init()

WIDTH, HEIGHT = 900, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Generala GO")
CLOCK = pygame.time.Clock()
FONT = pygame.font(28)

# ---- CARGAR IMÁGENES ----
imagenes_dados = [
    pygame.image.load("assets/pikachu_dado_1.jpg")
]


dados = []

tirar_dado()

# Para conservar dados según click
conservar = [False, False, False, False, False]

def dibujar():
    SCREEN.fill((200, 230, 255))

    x = 80
    for i in range(5):
        valor = dados[i]
        img = imagenes_dados[valor - 1]

        if conservar[i]:
            pygame.draw.rect(SCREEN, (0, 200, 0), (x - 5, 140, img.get_width() + 10, img.get_height() + 10))

        SCREEN.blit(img, (x, 145))

        x += 150

    pygame.draw.rect(SCREEN, (255, 200, 0), (350, 400, 200, 60))
    t = FONT.render("TIRAR", True, (0, 0, 0))
    SCREEN.blit(t, (415, 415))

    pygame.display.update()

# -------- INICIO ----------

tirar_dado()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # Click en dados
            x = 80
            for i in range(5):
                img = imagenes_dados[dados[i] - 1]
                rect = pygame.Rect(x, 145, img.get_width(), img.get_height())
                if rect.collidepoint(mx, my):
                    conservar[i] = not conservar[i]
                x += 150

            # Botón tirar
            boton_rect = pygame.Rect(350, 400, 200, 60)
            if boton_rect.collidepoint(mx, my):
                nuevos = []
                for i in range(5):
                    if conservar[i]:
                        nuevos.append(dados[i])
                    else:
                        nuevos.append(random.randint(1, 6))
                dados = nuevos

    dibujar()
    CLOCK.tick(30)

pygame.quit()

                