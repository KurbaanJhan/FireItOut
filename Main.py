import pygame

#Load assets only once and use it in your game loop
sky = pygame.image.load("Sky.png")
ground = pygame.image.load("ground.png")
platform_1 = pygame.image.load("ground1.png")
platform_3 = pygame.image.load("ground3.png")
platform_4 = pygame.image.load("ground4.png")
tree_bush = pygame.image.load("tree_bush.png")
tree_double = pygame.image.load("tree_double.png")
tree_pine_cone = pygame.image.load("tree_pine_cone.png")
standing = pygame.transform.scale(pygame.image.load("assets/stickman1.png"), (32, 32))
jump = pygame.transform.scale(pygame.image.load("assets/stickmanrunning2.png"), (32, 32))

#Initialize player values
xpos, ypos = 400, 600
jumping = False
walking = 1
GRAV = 1
JHEIGHT = 20
YVELO = JHEIGHT
standing = pygame.transform.scale(pygame.image.load("assets/stickman1.png"), (32, 32))
jump = pygame.transform.scale(
    pygame.image.load("assets/stickmanrunning2.png"), (32, 32)
)
walk = pygame.transform.scale(
    pygame.image.load("assets/stickmanrunning1.png"), (32, 32)
)
walk2 = pygame.transform.scale(
    pygame.image.load("assets/stickmanInverted.png"), (32, 32)
)
stikkrect = standing.get_rect(center=(xpos, ypos))

def main_game(screen):
    global xpos, ypos, YVELO, jumping

    clock = pygame.time.Clock()  # create a clock object for timing

    run = True
    while run:
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
        screen.blit(jump, stikkrect)
        if keyspress[pygame.K_d]:
            walking = 2
            xpos += 1
            stikkrect = walk.get_rect(center=(xpos, ypos))
            screen.blit(walk, stikkrect)
        if keyspress[pygame.K_a]:
            walking = 4
            xpos -= 1
            stikkrect = walk2.get_rect(center=(xpos, ypos))
            screen.blit(walk2, stikkrect)
        elif walking == 1 or jumping == False:
            stikkrect = standing.get_rect(center=(xpos, ypos))
            screen.blit(standing, stikkrect)
        # handle every event since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # clear the screen
        screen.fill((0, 0, 0))

        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 610))
        screen.blit(platform_1, (1100, 360))
        screen.blit(tree_double, (1100, 255))
        screen.blit(tree_pine_cone, (1200, 213))
        screen.blit(tree_bush, (1350, 205))
        screen.blit(tree_pine_cone, (1450, 213))
        screen.blit(tree_double, (1275, 255))

        screen.blit(platform_3, (50, 360))
        screen.blit(tree_bush, (50, 205))
        screen.blit(tree_bush, (150, 205))
        screen.blit(tree_double, (250, 255))
        screen.blit(tree_pine_cone, (350, 213))

        screen.blit(platform_4, (530, 170))
        screen.blit(tree_bush, (540, 17))
        screen.blit(tree_double, (640, 65))
        screen.blit(tree_pine_cone, (740, 25))
        screen.blit(tree_pine_cone, (840, 25))
        screen.blit(tree_bush, (940, 17))

        screen.blit(tree_double, (410, 505))
        screen.blit(tree_pine_cone, (500, 465))
        screen.blit(tree_bush, (600, 457))
        screen.blit(tree_pine_cone, (700, 465))

        screen.blit(tree_bush, (900, 457))
        screen.blit(tree_bush, (1000, 457))
        screen.blit(tree_double, (1100, 505))
        screen.blit(tree_double, (100, 505))
        screen.blit(tree_double, (1400, 505))
        screen.blit(tree_double, (200, 505))

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
            screen.blit(jump, stikkrect)
        else:
            stikkrect = standing.get_rect(center=(xpos, ypos))
            screen.blit(standing, stikkrect)


        # update the display to show the new frame
        pygame.display.flip()

        # cap the framerate at 60 FPS.
        clock.tick(60)

def options(screen):
    pygame.init
    size = (1600, 800)
    screen = pygame.display.set_mode(size)
    done = False



    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When user clicked close
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # When user pressed ESC key
                    done = True



    pygame.quit()
