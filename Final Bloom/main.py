#platformer demo
#r4t0030
#version 1.2
#2025-06-24
# TODO: optimise an make a jump buttion
import pygame
pygame.init()

#display
screen = ((500, 500))
win = pygame.display.set_mode((screen))

#useing this to set border collisions
screen_width = 500

#title
pygame.display.set_caption("Platformer Demo")

#frame rate
clock = pygame.time.Clock()
#width and hight for the sprite
width = 50
height = 50
# set velocity to control the speed of the sprite
vel = 200

# set the co-ordinates of where the sprite will appear and its hight/width
x = screen[0]/2 - width/2
y = screen[1]/2 - height/2

#jump code
isJump = False
jumpHight = 10

#game loop
done = True
while done:
    dt = clock.tick(60) / 1000.0 # Limit to 60 frames per second and get delta time in seconds # Limit to 60 frames per second #controls the frame rate
    print("FPS:", int(clock.get_fps()))

    #quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    
    #movement code
    #moves charactoer for as long as the key gets held down in whatever direction i choose
    #set up a list to do this
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel * dt
    if keys[pygame.K_RIGHT]:
        x += vel * dt
    if keys[pygame.K_UP]:
        y -= vel * dt
    if keys[pygame.K_DOWN]:
        y += vel * dt
    if keys[pygame.K_ESCAPE]:
        done = False
    #draw over the rectangle to cover up its tracks
    win.fill((0, 255, 255)) #fill the window with black
    
    #draw the sprite
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    #update the display
    pygame.display.update()

pygame.quit() #quit the game
