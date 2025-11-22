import pygame
import random
from render.render_pantalla import fondo_creditos, volver_menu
from puntaje.plantilla_puntaje import jugada_generala, jugada_uno_al_seis, jugada_full, jugada_poker, jugada_escalera
from estadisticas.archivo_json_csv import realizar_registro, archivo
from render.render_elementos import crear_boton_rect
from datos.constantes import WIDTH,HEIGHT

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

def tirar_un_dado():
    return random.randint(1, 6)

def solicitar_nombre(pantalla, puntaje_total):
    fondo = fondo_creditos()
    fuente_titulo = pygame.font.Font(None, 60)
    fuente_texto = pygame.font.Font(None, 45)
    fuente_input = pygame.font.Font(None, 50)

    nombre = ""
    activo = True
    clock = pygame.time.Clock()

    while activo:
        pantalla.blit(fondo, (0, 0))

        # TÍTULO
        txt_titulo = fuente_titulo.render("¡Partida terminada!", True, (0, 0, 0))
        pantalla.blit(txt_titulo, (30, 200))

        # PUNTAJE
        txt_puntaje = fuente_texto.render(f"Tu puntaje total es: {puntaje_total}", True, (0, 0, 0))
        pantalla.blit(txt_puntaje, (30, 260))

        # PEDIR NOMBRE
        txt_pedir_nombre = fuente_texto.render("Ingrese su nombre para anotar:", True, (0, 0, 0))
        pantalla.blit(txt_pedir_nombre, (30, 330))

        # CAJA
        pygame.draw.rect(pantalla, (255, 255, 255), (30, 380, 500, 60))
        pygame.draw.rect(pantalla, (0, 0, 0), (30, 380, 500, 60), 3)

        txt_nombre = fuente_input.render(nombre, True, (0, 0, 0))
        pantalla.blit(txt_nombre, (40, 390))

        pygame.display.update()

        # EVENTOS
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:

                # Enter → confirmar nombre
                if evento.key == pygame.K_RETURN:
                    if len(nombre.strip()) > 0:
                        activo = False  # ← salimos del bucle
                        break

                # Borrar un carácter
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]

                else:
                    # Agregar texto normal
                    if len(nombre) < 18:
                        nombre += evento.unicode

        clock.tick(30)

    return nombre  # ← AHORA ESTÁ BIEN UBICADO




def boton_tirar_dados(pant):
    x = WIDTH - 200
    y = HEIGHT - 100
    texto = "Tirar dados"

    rect = crear_boton_rect(
        pant,
        x, y,
        160,
        60,
        texto,
        (255, 215, 0),
        (255, 255, 255)
    )
    return rect

puntajes = {
    'Pikachu (1)': None,          # Unos
    'Bulbasur (2)': None,         # Doses
    'Charmander (3)': None,       # Treses
    'Squirtle (4)': None,         # Cuatros
    'Snorlax (5)': None,          # Cincos
    'Gengar (6)': None,           # Seises
    'Evolucion (20)': None,        # Escalera
    'Triple combo (30)': None,     # Full
    'Fuerza Cuadruple (40)': None, # Poker
    'Legendario (50 | 100)': None        # Generala
}

def elegir_categoria_interfaz(pantalla, jugadas, puntajes):
    mapa_categorias = {
        "Pikachu (1)": 1,
        "Bulbasur (2)": 2,
        "Charmander (3)": 3,
        "Squirtle (4)": 4,
        "Snorlax (5)": 5,
        "Gengar (6)": 6,
        "Evolucion (20)": 7,
        "Triple combo (30)": 8,
        "Fuerza Cuadruple (40)": 9,
        "Legendario (50 | 100)": 10
    }

    fondo = fondo_creditos()
    pantalla.blit(fondo, (0, 0))

    fuente = pygame.font.Font(None, 40)

    inicio_x = 100
    inicio_y = 100
    separacion = 60
    rectangulos = []

    # Puntaje total actual
    total_puntos = puntaje_total(puntajes)

    categorias = list(puntajes.keys())

    for idx, categoria in enumerate(categorias):
        y = inicio_y + idx * separacion

        if puntajes[categoria] is None:
            color = (0, 255, 0)
            puntos_posibles = jugadas[mapa_categorias[categoria]]
            texto = f"{categoria} → {puntos_posibles} pts"
        else:
            color = (255, 0, 0)
            texto = f"{categoria} → YA USADA"

        rect = pygame.Rect(inicio_x, y, 520, 50)
        pygame.draw.rect(pantalla, color, rect)

        rendered = fuente.render(texto, True, (0, 0, 0))
        pantalla.blit(rendered, (inicio_x + 10, y + 10))

        rectangulos.append((rect, categoria))

    # Mostrar el total abajo
    texto_total = fuente.render(f"Puntaje total: {total_puntos}", True, (255, 255, 255))
    pantalla.blit(texto_total, (inicio_x, inicio_y + separacion * len(categorias) + 50))

    pygame.display.update()

    # Esperar selección
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                for rect, categoria in rectangulos:
                    if rect.collidepoint(x, y):
                        if puntajes[categoria] is None:
                            idx = mapa_categorias[categoria]
                            return categoria, jugadas[idx]
                        else:
                            print("Categoría ya usada")



def puntaje_total(puntajes):
    total = 0
    for clave in puntajes:
        if puntajes[clave] is not None:
            total += puntajes[clave]
    return total



def pantalla_jugar(pantalla):

    fondo = fondo_creditos()

    cant_categorias = 10
    turno_actual = 1
    turnos_totales = 3

    # Primeros dados
    dados = [tirar_un_dado() for _ in range(5)]
    dados_bloqueados = [False] * 5

    fuente = pygame.font.Font(None, 40)
    fuente_fin = pygame.font.Font(None, 50)
    reloj = pygame.time.Clock()

    corriendo = True
    while corriendo:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                # --- BOTÓN TIRAR ---
                if rect_boton_tirar.collidepoint(evento.pos):

                    # Tirar solo los desbloqueados
                    for i in range(5):
                        if not dados_bloqueados[i]:
                            dados[i] = tirar_un_dado()

                    # Generala
                    puntos_generala = jugada_generala(dados, turno_actual)

                    if puntos_generala == 100:
                        mensaje = fuente_fin.render("¡GENERALA SERVIDA!", True, (255, 255, 255))
                        pantalla.blit(mensaje, ((1280 - mensaje.get_width()) // 2, 660))
                        pygame.display.update()
                        pygame.time.wait(2500)
                        return "menu"

                    turno_actual += 1

                    # Ya gastó los 3 tiros → elegir categoría
                    if turno_actual > turnos_totales:

                        jugadas = {
                            1: jugada_uno_al_seis(dados, 1),
                            2: jugada_uno_al_seis(dados, 2),
                            3: jugada_uno_al_seis(dados, 3),
                            4: jugada_uno_al_seis(dados, 4),
                            5: jugada_uno_al_seis(dados, 5),
                            6: jugada_uno_al_seis(dados, 6),
                            7: jugada_escalera(dados),
                            8: jugada_full(dados),
                            9: jugada_poker(dados),
                            10: jugada_generala(dados, 3),
                        }

                        categoria, puntos = elegir_categoria_interfaz(pantalla, jugadas, puntajes)
                        puntajes[categoria] = puntos

                        cant_categorias -= 1
                        turno_actual = 1

                        # Reset total
                        dados = [tirar_un_dado() for _ in range(5)]
                        dados_bloqueados = [False] * 5

                        if cant_categorias == 0:
                            total = puntaje_total(puntajes)
                            nombre = solicitar_nombre(pantalla, total)
                            total_puntos = str(total)
                            realizar_registro(archivo, nombre, total_puntos)
                            return "menu"
                        

                # --- CLICK PARA BLOQUEAR DADOS ---
                x, y = evento.pos
                for i in range(5):
                    rect_dado = pygame.Rect(10 + i * 250, 250, 250, 250)
                    if rect_dado.collidepoint(x, y):
                        dados_bloqueados[i] = not dados_bloqueados[i]

        # -------------------- RENDER --------------------
        pantalla.blit(fondo, (0, 0))

        # Botón tirar
        rect_boton_tirar = boton_tirar_dados(pantalla)

        pantalla.blit(fuente.render(f"Categorías restantes: {cant_categorias}", True, (0, 0, 0)), (20, 70))
        pantalla.blit(fuente.render(f"Tiro: {turno_actual} de {turnos_totales}", True, (0, 0, 0)), (20, 120))

        # Mostrar dados
        for i, valor in enumerate(dados):
            img = pokemon_imagenes[valor - 1]
            x = 10 + i * 250
            pantalla.blit(img, (x, 250))

            if dados_bloqueados[i]:
                pygame.draw.rect(pantalla, (255, 0, 0), (x, 250, 250, 250), 5)

        if volver_menu(pantalla):
            return "menu"

        pygame.display.update()
        reloj.tick(60)
