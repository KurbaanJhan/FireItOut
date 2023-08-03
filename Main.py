import pygame
import sys
import main_menu

pygame.init()

pygame.init()
WIDTH, HEIGHT = 1600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fire it Out")
white = (255, 255, 255)
black = (255, 0, 255)
scaling_factor = 2
sky = pygame.image.load("Sky.png")
ground = pygame.image.load("ground.png")
platform_1 = pygame.image.load("ground1.png")
platform_3 = pygame.image.load("ground3.png")
platform_4 = pygame.image.load("ground4.png")
tree_bush = pygame.image.load("tree_bush.png")
tree_double = pygame.image.load("tree_double.png")
tree_pine_cone = pygame.image.load("tree_pine_cone.png")
clok = pygame.time.Clock()
player = pygame.Rect((300, 250, 50, 50))
xpos, ypos = 400, 600
jumping = False
GRAV = 1
JHEIGHT = 20
YVELO = JHEIGHT
standing = pygame.transform.scale(pygame.image.load("assets/stickman1.png"), (32, 32))
jump = pygame.transform.scale(
    pygame.image.load("assets/stickmanrunning2.png"), (32, 32)
)
stikkrect = standing.get_rect(center=(xpos, ypos))

WIN.blit(sky, (0, 0))
WIN.blit(ground, (0, 610))


WIN.blit(platform_1, (1100, 360))
WIN.blit(tree_double, (1100, 255))
WIN.blit(tree_pine_cone, (1200, 213))
WIN.blit(tree_bush, (1350, 205))
WIN.blit(tree_pine_cone, (1450, 213))
WIN.blit(tree_double, (1275, 255))

WIN.blit(platform_3, (50, 360))
WIN.blit(tree_bush, (50, 205))
WIN.blit(tree_bush, (150, 205))
WIN.blit(tree_double, (250, 255))
WIN.blit(tree_pine_cone, (350, 213))


WIN.blit(platform_4, (530, 170))
WIN.blit(tree_bush, (540, 17))
WIN.blit(tree_double, (640, 65))
WIN.blit(tree_pine_cone, (740, 25))
WIN.blit(tree_pine_cone, (840, 25))
WIN.blit(tree_bush, (940, 17))


WIN.blit(tree_double, (410, 505))
WIN.blit(tree_pine_cone, (500, 465))
WIN.blit(tree_bush, (600, 457))
WIN.blit(tree_pine_cone, (700, 465))


WIN.blit(tree_bush, (900, 457))
WIN.blit(tree_bush, (1000, 457))
WIN.blit(tree_double, (1100, 505))
WIN.blit(tree_double, (100, 505))
WIN.blit(tree_double, (1400, 505))
WIN.blit(tree_double, (200, 505))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keyspress = pygame.key.get_pressed()
    if keyspress[pygame.K_SPACE]:
        jumping = True
    if jumping:
        ypos -= YVELO
        YVELO -= GRAV
        if YVELO < -JHEIGHT:
            jumping = False
            YVELO = JHEIGHT
        stikkrect = jump.get_rect(center=(xpos, ypos))
        WIN.blit(jump, stikkrect)
    else:
        stikkrect = standing.get_rect(center=(xpos, ypos))
        WIN.blit(standing, stikkrect)
    pygame.display.update()
    clok.tick(60)
