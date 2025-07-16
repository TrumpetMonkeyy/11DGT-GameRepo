#platformer demo
#r4t0030
#version 1.2
#2025-06-24
# TODO: make the cam follow the sprite
import pygame
import os
import subprocess
import sys
import pytmx
from pytmx.util_pygame import load_pygame

#check if user has requirements installed
def check_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    
    if os.path.exists(req_path):
        try:
            print("All requirements installed. proceeding to run the game.")
        except subprocess.CalledProcessError:
            print("Failed to find requirements please run setup.py.")
        
check_requirements()

pygame.init()

#display
screen = ((800, 600))
win = pygame.display.set_mode((screen), pygame.RESIZABLE)

#title
pygame.display.set_caption("Final Bloom")

#icon 
image_path = os.path.join(os.path.dirname(__file__), 'assets', 'icons', 'icon.png')
game_icon = pygame.image.load(image_path)
pygame.display.set_icon(game_icon)

#frame rate
clock = pygame.time.Clock()
#width and hight for the sprite
width = 50
height = 50

#load tilemap
tmx_path = os.path.join(os.path.dirname(__file__), 'maps', 'map1.tmx')
tmx_data = load_pygame(tmx_path)


# Load player sprite
sprite_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player.png')
player_sprite = pygame.image.load(sprite_path).convert_alpha()
player_sprite = pygame.transform.scale(player_sprite, (width, height))

# set velocity to control the speed of the sprite
vel = 200

# set the co-ordinates of where the sprite will appear and its hight/width
x = screen[0]/2 - width/2
y = screen[1]/2 - height/2


#game loop
done = True
while done:
    dt = clock.tick(120) / 1000.0 # Limit to 60 frames per second and get delta time in seconds # Limit to 60 frames per second #controls the frame rate
    print("FPS:", int(clock.get_fps()))

    #quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    
    #draw the tilemap
    scale = 2  # Try 2 for double size, or 1.5 for a mild zoom
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x_tile, y_tile, image in layer.tiles():
                if image:
                    # Scale the tile image
                    scaled_image = pygame.transform.scale(
                        image, 
                        (int(tmx_data.tilewidth * scale), int(tmx_data.tileheight * scale))
                    )
                    # Draw scaled image at the new position
                    win.blit(
                        scaled_image, 
                        (x_tile * tmx_data.tilewidth * scale, y_tile * tmx_data.tileheight * scale)
                    )



    #draw the sprite
    win.blit(player_sprite, (x, y))

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

    

    #update the display
    pygame.display.update()

pygame.quit() #quit the game
