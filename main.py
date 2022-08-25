import pygame
import random
import math

pygame.init()
pantalla = pygame.display.set_mode((800, 600))

se_ejecuta = True
score = 0

pygame.display.set_caption("Space Invaders")
icono = pygame.image.load("2790378.png")
icono = pygame.transform.scale(icono, (64, 64))
pygame.display.set_icon(icono)

#icono_enemigo = pygame.image.load("enemigo.png")
#icono_enemigo = pygame.transform.scale(icono_enemigo, (32, 32))

misil_img = pygame.image.load("bala.png")
#misil_img = pygame.transform.scale(misil_img, (32, 32))
x_misil = 0
y_misil = 500
delta_x_misil = 0
delta_y_misil = 1
misil_visible = False
cantidad_enemigos = 4

back = pygame.image.load("back_galaxy.png")

x_enemigo = []
y_enemigo = []
delta_x_enemigo = []
delta_y_enemigo = []
icono_enemigo = []

for e in range(cantidad_enemigos):
    icono_enemigo.append(pygame.image.load("enemigo.png"))
    x_enemigo.append(random.randint(0, 736))
    y_enemigo.append(random.randint(50, 200))
    delta_x_enemigo.append(0.3)
    delta_y_enemigo.append(50)

#x_enemigo = random.randint(0,736)
#y_enemigo = random.randint(50,200)

x = 400
y = 540

delta = 0
#delta_x_enemigo = 0.3
#delta_y_enemigo = 50


def misil(a, b):
    global misil_visible
    misil_visible = True
    pantalla.blit(misil_img, (a+16, b+10))


def jugador(a, b):
    pantalla.blit(icono, (a, b))


def enemigo(a, b, ene):
    pantalla.blit(icono_enemigo[ene], (a, b))


def detectar_colision(xe, ye, xm, ym):
    distancia = math.sqrt((xe-xm)**2 + (ye-ym)**2)
    if distancia < 27:
        return True
    else:
        return False


while se_ejecuta:
    # pantalla.fill((0,162,255))
    pantalla.blit(back, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                delta = 0.3
            if evento.key == pygame.K_LEFT:
                delta = -0.3
            if evento.key == pygame.K_SPACE:
                if misil_visible == False:
                    x_misil = x
                    misil(x_misil, y_misil)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                delta = 0

    # modificar ubicacion jugador
    x += delta

    if x <= 0:
        x = 0
    elif x >= 736:
        x = 736

    # modificar ubicacion enemigo
    for e in range(cantidad_enemigos):

        x_enemigo[e] += delta_x_enemigo[e]

        if x_enemigo[e] <= 0:
            delta_x_enemigo[e] = 0.3
            y_enemigo[e] += delta_y_enemigo[e]
        elif x_enemigo[e] >= 736:
            delta_x_enemigo[e] = -0.3
            y_enemigo[e] += delta_y_enemigo[e]

        if detectar_colision(x_enemigo[e], y_enemigo[e], x_misil, y_misil):
            y_misil = 500
            misil_visible = False
            score += 1
            print(f"score : {score}")
            x_enemigo[e] = random.randint(0, 736)
            y_enemigo[e] = random.randint(50, 200)

        enemigo(x_enemigo[e], y_enemigo[e], e)

    if y_misil <= -64:
        y_misil = 500
        misil_visible = False

    if misil_visible:
        misil(x_misil, y_misil)
        y_misil -= delta_y_misil

    """
    if detectar_colision(x_enemigo, y_enemigo, x_misil, y_misil):
        y_misil = 500
        misil_visible = False
        score += 1
        print(f"score : {score}")
        x_enemigo = random.randint(0, 736)
        y_enemigo = random.randint(50, 200)

    """

    #enemigo(x_enemigo, y_enemigo)
    jugador(x, y)
    pygame.display.update()
