import pygame
from Main import main_game
from Main import options

# Define some colors
AQUA = (0, 255, 255)
red = (199, 52, 42)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255, 0)
sky = pygame.image.load("Sky1.png")
platform_1 = pygame.image.load("ground1.png")
tree_bush = pygame.image.load("tree_bush.png")
tree_double = pygame.image.load("tree_double.png")
tree_pine_cone = pygame.image.load("tree_pine_cone.png")
cloud_small = pygame.image.load("small_cloud.png")
cloud_big = pygame.image.load("cloud_big.png")
cloud_sun = pygame.image.load("cloud_sun.png")
cloud_rain = pygame.image.load("cloud_rain.png")
platform_flowers = pygame.image.load("platform_flowers.png")
# This function is used to display text on the screen


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# The main function that creates and controls the menu


def game_menu():
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (1600, 800)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Fire it Out")

    # Loop until the user clicks the close button or press the ESC key
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When user clicked close
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # When user pressed ESC key
                    done = True

            # User click the mouse get the position
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_button.collidepoint(x, y):
                    main_game(screen)
                if options_button.collidepoint(x, y):
                      options(screen)
                if quit_button.collidepoint(x, y):
                    done = True

        # --- Drawing code should go here
          # clouds and sky
        screen.blit(sky, (0, 0))
        screen.blit(cloud_small, (100, 60))
        screen.blit(cloud_rain, (100, 150))

        screen.blit(cloud_big, (300, 50))
        screen.blit(cloud_small, (530, 50))
        screen.blit(cloud_rain, (530, 140))

        screen.blit(cloud_big, (800, 20))
        screen.blit(cloud_rain, (825, 140))

        screen.blit(cloud_small, (1100, 90))
        screen.blit(cloud_sun, (1300, 80))
        screen.blit(cloud_rain, (1350, 225))
        # platforms and trees and flowers and grass
        screen.blit(platform_1, (100, 600))
        screen.blit(platform_flowers, (100, 550))
        screen.blit(platform_flowers, (250, 550))
        screen.blit(platform_flowers, (400, 550))
        screen.blit(tree_pine_cone, (100, 455))
        screen.blit(tree_pine_cone, (200, 455))
        screen.blit(tree_bush, (300, 448))
        screen.blit(tree_double, (380, 495))
        screen.blit(tree_pine_cone, (470, 455))

        screen.blit(platform_1, (1050, 600))
        screen.blit(platform_flowers, (1050, 550))
        screen.blit(platform_flowers, (1200, 550))
        screen.blit(platform_flowers, (1350, 550))
        screen.blit(tree_bush, (1050, 448))
        screen.blit(tree_bush, (1150, 448))
        screen.blit(tree_pine_cone, (1250, 455))
        screen.blit(tree_pine_cone, (1350, 455))
        screen.blit(tree_double, (1420, 495))

        largeText = pygame.font.Font('freesansbold.ttf', 100)
        smallText = pygame.font.Font('freesansbold.ttf', 35)

        TextSurf, TextRect = text_objects("FIRE IT OUT", largeText, red)
        TextRect.center = ((size[0] / 2), (size[1] / 2 - 100))
        screen.blit(TextSurf, TextRect)

        startSurf, startRect = text_objects("START", smallText, BLACK)
        startRect.center = ((size[0] / 2), (size[1] / 2))
        start_button = pygame.draw.rect(screen, WHITE, startRect,)
        screen.blit(startSurf, startRect)

        optionsSurf, optionsRect = text_objects("OPTIONS", smallText, BLACK)
        optionsRect.center = ((size[0] / 2), (size[1] / 2 + 50))
        options_button = pygame.draw.rect(screen, WHITE, optionsRect,)
        screen.blit(optionsSurf, optionsRect)

        quitSurf, quitRect = text_objects("QUIT", smallText, BLACK)
        quitRect.center = ((size[0] / 2), (size[1] / 2 + 100))
        quit_button = pygame.draw.rect(screen, WHITE, quitRect)
        screen.blit(quitSurf, quitRect)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    game_menu()
