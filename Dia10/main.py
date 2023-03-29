import pygame

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("Dia10/ovni32.png")
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load("Dia10/cohete.png")
jugador_x = 368
jugador_y = 536

def jugador():
    pantalla.blit(img_jugador, (jugador_x, jugador_y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill((205,144,228))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    
    jugador()
    pygame.display.update()        