#platformer demo
#r4t0030
#version 1.1
#2025-06-24
# TODO: make the main window and sprite to move
import pygame
pygame.init()

#display
win = pygame.display.set_mode((500, 500))
#title
pygame.display.set_caption("Platformer Demo")

# set the co-ordinates of where the sprite will appear and its hight/width
x = 50
y = 50
#width and hight
width = 50
height = 50

# set velocity to control the speed of the sprite
vel = 1.5

#game loop
done = True
while done:
    pygame.time.delay(5) #controls the frame rate

    #quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    
    #movement code
    #moves charactoer for as long as the key gets held down in whatever direction i choose
    #set up a list to do this
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_ESCAPE]:
        done = False
    #draw over the rectangle to cover up its tracks
    win.fill((0, 255, 255)) #fill the window with black
    
    #draw the sprite
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    #update the display
    pygame.display.update()

pygame.quit() #quit the game