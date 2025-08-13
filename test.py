import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Toggle Key Example")

keys = pygame.key.get_pressed()

# Initialize the toggle state
debug = False

done = True

keys = pygame.key.get_pressed()
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                debug = not debug


    # Game logic based on the toggle state
    if debug:
        screen.fill((0, 100, 0))  # Green background when toggled
    else:
        screen.fill((100, 0, 0))  # Red background when not toggled

    pygame.display.flip()

pygame.quit()