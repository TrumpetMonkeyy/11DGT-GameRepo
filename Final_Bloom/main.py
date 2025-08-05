#The Final Bloom
#r4t0030 virtualvariant
#version 1.2
#2025-06-24
# TODO: make the cam follow the sprite
<<<<<<< Updated upstream
=======
import os
import subprocess
import sys

#check if user has requirements installed
req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt') #finds the full path of the requirements.txt file
if os.path.exists(req_path):
    try:
        print("Checking and installing requirements...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_path]) #found from reddit to install the requirements
        print("Requirements are up to date.")
        os.remove(req_path)
    except subprocess.CalledProcessError:
        print("Failed to install requirements. please install them manually")
        os.system('pause')
        sys.exit()
else:
    print("requirements.txt not found. continuing")

#importing liberys
>>>>>>> Stashed changes
import pygame
import os
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()

#display
import tkinter as tk

root = tk.Tk()
<<<<<<< Updated upstream
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"Screen resolution: {width}x{height}")
screen = ((width, height))
=======
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(f"Screen resolution: {screen_width}x{screen_height}")
screen = ((screen_width, screen_height))
>>>>>>> Stashed changes
win = pygame.display.set_mode((screen), pygame.RESIZABLE)


#title
pygame.display.set_caption("Final Bloom")

#icons
image_path = os.path.join(os.path.dirname(__file__), 'assets', 'icons', 'icon.png')
game_icon = pygame.image.load(image_path)
pygame.display.set_icon(game_icon)

#frame rate
clock = pygame.time.Clock()
#width and height for the sprite
width = 50
height = 50

#load tilemap
tmx_path = os.path.join(os.path.dirname(__file__), 'maps', 'map1.tmx')
tmx_data = load_pygame(tmx_path)


<<<<<<< Updated upstream

# Load player sprite
sprite_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player.png')
player_sprite = pygame.image.load(sprite_path).convert_alpha()
player_sprite = pygame.transform.scale(player_sprite, (width, height))

=======
scaled_tiles = [] #the coordanets and image gets saved in this list
fence_rects = []

for layer in tmx_data.visible_layers:
    if isinstance(layer, pytmx.TiledTileLayer):
        for x_tile, y_tile, image in layer.tiles():
            if image:
                scaled_image = pygame.transform.scale(
                    image,
                    (int(tmx_data.tilewidth * scale), int(tmx_data.tileheight * scale))
                )
                tile_x = x_tile * tmx_data.tilewidth * scale
                tile_y = y_tile * tmx_data.tileheight * scale
                scaled_tiles.append((scaled_image, tile_x, tile_y))

                # If it's the fence layer, store its rect
                if layer.name == "fences":
                    fence_rects.append(pygame.Rect(tile_x, tile_y, tmx_data.tilewidth * scale, tmx_data.tileheight * scale))
                    
#width and height for the sprite
sprite_width = 28
sprite_height = 44


# set the co-ordinates of where the sprite will appear and its hight/width
x = screen_width / 2
y = screen_height / 2

# Load player sprite
player_front_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_front.png')#finds the player path
player_front_load = pygame.image.load(player_front_path).convert_alpha() #loads the sprite
player_front = pygame.transform.scale(player_front_load, (sprite_width, sprite_height)) #resize the sprite



player_right_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_right.png')
player_right_load = pygame.image.load(player_right_path).convert_alpha()
player_right = pygame.transform.scale(player_right_load, (sprite_width, sprite_height))


player_left_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_left.png')
player_left_load = pygame.image.load(player_left_path).convert_alpha()
player_left = pygame.transform.scale(player_left_load, (sprite_width, sprite_height))

player_back_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_back.png')
player_back_load = pygame.image.load(player_back_path).convert_alpha()
player_back = pygame.transform.scale(player_back_load, (sprite_width, sprite_height))
>>>>>>> Stashed changes
# set velocity to control the speed of the sprite
vel = 200

# set the co-ordinates of where the sprite will appear and its hight/width
x = screen[0]/2 - width/2
y = screen[1]/2 - height/2

<<<<<<< Updated upstream

#game loop
done = True
while done:
    dt = clock.tick(120) / 1000.0 # Limit to 60 frames per second and get delta time in seconds # Limit to 60 frames per second #controls the frame rate
    print("FPS:", int(clock.get_fps()))

=======
#frame rate
clock = pygame.time.Clock()

#main menu
def show_main_menu():
    #title
    pygame.display.set_caption("main menu")

    bg_trans_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'transparent_background.png')
    bg_trans = pygame.image.load(bg_trans_path).convert_alpha() #loads the filter for the background

    title_font_path = os.path.join(os.path.dirname(__file__), 'assets', 'fonts', 'CASTELAR.ttf')
    title_font = pygame.font.Font(title_font_path, 72) #sets the fonts
    small_font = pygame.font.SysFont(None, 36)

    title_text = title_font.render("Final Bloom", True, (200, 200, 200)) #renders the fonts and sets the colors
    title_text_rect = title_text.get_rect(center = (screen_width/2, screen_height*.43))
	
    play_text = small_font.render("Press ENTER to Play", True, (180, 180, 180))
    play_text_rect = play_text.get_rect(center = (screen_width/2, screen_height*.52))

    quit_text = small_font.render("Press Q to Quit", True, (180, 180, 180))
    quit_text_rect = quit_text.get_rect(center = (screen_width/2, screen_height*.6))

    help_text = small_font.render("Press H to show help menu", True, (180, 180, 180))
    help_text_rect = help_text.get_rect(center = (screen_width/2, screen_height*.56))

    while True:
        clock.tick(60)
        for img, px, py in scaled_tiles:
            win.blit(img, (px, py)) #shows the map
        win.blit(bg_trans, (0, 0)) #applys the filter ontop

        win.blit(title_text, title_text_rect) #places out the text in the coordanets
        win.blit(play_text, play_text_rect)
        win.blit(quit_text, quit_text_rect)
        win.blit(help_text, help_text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return
        elif keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
        elif keys[pygame.K_h]:
            show_help_menu_start()

def show_help_menu_start():
    #title
    pygame.display.set_caption("HELP ME")

    bg_trans_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'transparent_background.png')
    bg_trans = pygame.image.load(bg_trans_path).convert_alpha() #loads the filter for the background


    small_font = pygame.font.SysFont(None, 36)  #sets the fonts
    help_text = small_font.render("Use arrow keys or WASD keys to move", True, (255, 255, 255)) #renders the fonts and sets the colors
    help_text_rect = help_text.get_rect(center = (screen_width/2, screen_height*.48))

    info_text = small_font.render("press ENTER to start playing, or ESC to go back to the menu", True, (255, 255, 255))
    info_text_rect = info_text.get_rect(center = (screen_width/2, screen_height*.52))

    while True: 
        #win.fill((0, 0, 0)) #sets the background to black   
        clock.tick(60)
        for img, px, py in scaled_tiles:
            win.blit(img, (px, py)) #shows the map
        win.blit(bg_trans, (0, 0)) #applys the filter ontop

        win.blit(help_text, help_text_rect) #displays the text and places them at coordanets
        win.blit(info_text, info_text_rect)



        
        for event in pygame.event.get(): #looks for key presses and sets them to do somthing
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return
        if keys[pygame.K_ESCAPE]:
            show_main_menu()
        
        pygame.display.update()


show_main_menu() #runs the start menu before the game runs

#game loop
running = True
debug = False
collide = False



while running:
        #allows key inputs to actually be able to do things
    keys = pygame.key.get_pressed()
    #title
    pygame.display.set_caption("Final Bloom")
    dt = clock.tick(60) / 1000.0 # Limit to 60 frames per second and get delta time in seconds # Limit to 60 frames per second #controls the frame rate
>>>>>>> Stashed changes
    #quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            #debug mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                debug = not debug
                
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



<<<<<<< Updated upstream
    #draw the sprite
    win.blit(player_sprite, (x, y))
=======

    #draw the sprite
    
    player_rect = player_front.get_rect(topleft=(x, y))
    win.blit(player_front, (x, y)) 

    for fence in fence_rects:
        if player_rect.colliderect(fence):
            collide = True

    if collide == True:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y = y + 25
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x = x + 25
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y = y - 25
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x = x - 25
        collide = False
    

>>>>>>> Stashed changes

    #movement code
    #moves character for as long as the key gets held down in whatever direction i choose
    #set up a list to do this
<<<<<<< Updated upstream
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= vel * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel * dt
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel * dt
=======
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= vel * dt
        win.blit(player_left, (x, y))
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel * dt
        win.blit(player_right, (x, y))
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel * dt
        win.blit(player_back, (x, y))
>>>>>>> Stashed changes
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += vel * dt
    if keys[pygame.K_ESCAPE]:
<<<<<<< Updated upstream
     done = False
=======
        show_main_menu()
        
    if debug == True:
        for rect in fence_rects:
            pygame.draw.rect(win, (255, 255, 255), rect, 2)
>>>>>>> Stashed changes

    

    #update the display
    pygame.display.update()

pygame.quit() #quit the game
exit()
