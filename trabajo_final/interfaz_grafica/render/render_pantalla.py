import pygame
from datos.constantes import WIDTH, COLOR_TEXTO_OSCURO, COLOR_SECUNDARIO, COLOR_TEXTO_CLARO
from .render_elementos import logo_juego, fondo_menu, crear_boton_rect, fondo_creditos

def pantalla_principal(pantalla):
    logo = logo_juego()
    fondo = fondo_menu()
    
    ancho_logo = logo.get_width()
    x_logo = (WIDTH - ancho_logo) // 2
    y_logo = 10

    etiquetas = ["Jugar", "Opciones", "Créditos", "Estadísticas", "Salir"]
    claves = ["jugar", "opciones", "creditos", "estadisticas", "salir"]

    ANCHO_BOTON = 160
    ALTO_BOTON = 60
    ESPACIO = 20

    total_ancho_botones = (ANCHO_BOTON * 5) + (ESPACIO * 4)
    inicio_botones_x = (WIDTH - total_ancho_botones) // 2
    y_botones = y_logo + logo.get_height() - 20

    botones = {}   # ← AHORA ES UN DICCIONARIO

    pantalla.blit(fondo, (0, 0))
    pantalla.blit(logo, (x_logo, y_logo))

    for i, texto in enumerate(etiquetas):
        x = inicio_botones_x + i * (ANCHO_BOTON + ESPACIO)

        rect = crear_boton_rect(
            pantalla,
            x, y_botones,
            ANCHO_BOTON,
            ALTO_BOTON,
            texto,
            COLOR_TEXTO_OSCURO,
            COLOR_SECUNDARIO
        )

        botones[claves[i]] = rect   # ← SE GUARDA COMO DICCIONARIO

    return botones



def pantalla_opciones(pantalla):
    pantalla.fill((40, 40, 40))
    fuente = pygame.font.Font(None, 70)
    texto = fuente.render("PANTALLA DE OPCIONES", True, (COLOR_TEXTO_CLARO))
    pantalla.blit(texto, (100, 100))
    return {}


datos = {
    'autores': ('Manuel Courtade', 'Maximo Savall'),
    'fecha': '31/10/2025',
    'materia': 'Programacion I',
    'docentes': ('Martin Alejandro Garcia', 'Veronica Carbonari'),
    'carrera': 'Tecnicatura en programacion',
    'contacto': ('courtademanuel@outlook.es', 'savallmaximo@gmail.com')
}



def pantalla_creditos(pantalla):
    fondo2 = fondo_creditos()
    pantalla.blit(fondo2, (0, 0))


    fuente = pygame.font.Font(None, 65)
    texto = fuente.render("CREDITOS", True, (COLOR_TEXTO_CLARO)) 
    pantalla.blit(texto, (330, 80))

    fuente_esc = pygame.font.Font(None, 35)
    texto_esc = fuente_esc.render("Presione ESC para volver al menu", True, (255, 255, 255))
    pantalla.blit(texto_esc, (20, 20))

    fuente_autores = pygame.font.Font(None, 35)
    txt_autores = fuente_autores.render('Manuel Courtade, Maximo Savall', True, (0, 0, 0))
    pantalla.blit(txt_autores, (120, 160))

    fuente_fecha = pygame.font.Font(None, 35)
    txt_fecha = fuente_fecha.render('31/10/2025', True, (0, 0, 0))
    pantalla.blit(txt_fecha, (120, 205))

    fuente_materia = pygame.font.Font(None, 35)
    txt_materia = fuente_materia.render('Programacion I', True, (0, 0, 0))
    pantalla.blit(txt_materia, (120, 250))

    fuente_docentes = pygame.font.Font(None, 35)
    txt_docentes = fuente_docentes.render('Martin Alejandro Garcia - Veronica Carbonari', True, (0, 0, 0))
    pantalla.blit(txt_docentes, (120, 295))

    fuente_carrera = pygame.font.Font(None, 35)
    txt_carrera = fuente_carrera.render('Tecnicatura en programacion', True, (0, 0, 0))
    pantalla.blit(txt_carrera, (120, 340))

    fuente_contacto = pygame.font.Font(None, 35)
    txt_contacto = fuente_contacto.render('courtademanuel@outlook.es - savallmaximo@gmail.com', True, (0, 0, 0))
    pantalla.blit(txt_contacto, (120, 385))

    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN: 
            if evento.key == pygame.K_ESCAPE: 
                pantalla_actual = "menu"

    return {}

def pantalla_jugar(pantalla):
    pantalla.fill((0, 0, 0))

    fuente = pygame.font.Font(None, 60)
    txt = fuente.render("Pantalla de JUEGO", True, (255, 255, 255))
    pantalla.blit(txt, (100, 100))

    fuente2 = pygame.font.Font(None, 35)
    txt2 = fuente2.render("Presione ESC para volver al menú", True, (200, 200, 200))
    pantalla.blit(txt2, (50, 50))

    return {}   # no usa botones

def pantalla_estadisticas(pantalla):
    pantalla.fill((40, 40, 40))
    fuente = pygame.font.Font(None, 70)
    texto = fuente.render("PANTALLA DE ESTADISTICAS", True, (COLOR_TEXTO_CLARO))
    pantalla.blit(texto, (100, 100))
    return {}