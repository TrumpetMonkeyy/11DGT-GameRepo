#Final Bloom
#r4t0030
#version 1.2
#2025-07-22
# TODO: make the cam follow the sprite
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
        sys.exit(1)
else:
    print("requirements.txt not found. continuing")

#importing liberys
import pygame
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init() #start pygame

#display
screen = ((1105, 625))
win = pygame.display.set_mode((screen), pygame.RESIZABLE)

#hides mouse cursor
pygame.mouse.set_visible(False)

#icons
window_icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icons', 'icon.png')
game_icon = pygame.image.load(window_icon_path)
pygame.display.set_icon(game_icon)

#load tilemap
tmx_path = os.path.join(os.path.dirname(__file__), 'maps', 'map1.tmx')
tmx_data = load_pygame(tmx_path)

#scail tilemap
scale = 2  #changes the scale 1=defalt

scaled_tiles = [] #the coordanets and image gets saved in this list
for layer in tmx_data.visible_layers:
    if isinstance(layer, pytmx.TiledTileLayer):
        for x_tile, y_tile, image in layer.tiles():  #pulls the tiles from the file and skips the empty and non image tiles/code that helps the 3rd party aplacation
            if image:
                scaled_image = pygame.transform.scale(#resizeing the tiles
                    image,
                    (int(tmx_data.tilewidth * scale), int(tmx_data.tileheight * scale))
                )
                scaled_tiles.append((scaled_image, x_tile * tmx_data.tilewidth * scale, y_tile * tmx_data.tileheight * scale))#calculating the tiles posision and coordinates and store with image

#width and hight for the sprite
width = 28
height = 44

# Load player sprite
player_front_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_front.png')#finds the player path
player_front_load = pygame.image.load(player_front_path).convert_alpha() #loads the sprite
player_front = pygame.transform.scale(player_front_load, (width, height)) #resize the sprite

player_right_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_right.png')
player_right_load = pygame.image.load(player_right_path).convert_alpha()
player_right = pygame.transform.scale(player_right_load, (width, height))

player_left_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_left.png')
player_left_load = pygame.image.load(player_left_path).convert_alpha()
player_left = pygame.transform.scale(player_left_load, (width, height))

player_back_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_back.png')
player_back_load = pygame.image.load(player_back_path).convert_alpha()
player_back = pygame.transform.scale(player_back_load, (width, height))
# set velocity to control the speed of the sprite
vel = 200

# set the co-ordinates of where the sprite will appear and its hight/width
x = screen[0]/2 - width/2 - 150
y = screen[1]/2 - height/2 - 20

#music
background_music_path = os.path.join(os.path.dirname(__file__), 'assets', 'audio', 'background_music.mp3')
def play_background_music():
    pygame.mixer.music.load(background_music_path)
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=0)
    pygame.mixer.music.set_volume(0.25)
play_background_music()
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
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
    title_text_rect = title_text.get_rect(center = (552.5, 150))
	
    play_text = small_font.render("Press ENTER to Play", True, (180, 180, 180))
    play_text_rect = play_text.get_rect(center = (552.5, 300))

    quit_text = small_font.render("Press Q to Quit", True, (180, 180, 180))
    quit_text_rect = quit_text.get_rect(center = (552.5, 340))

    help_text = small_font.render("Press H to show help menu", True, (180, 180, 180))
    help_text_rect = help_text.get_rect(center = (552.5, 380))

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
            show_help_menu()


def show_help_menu():
    #title
    pygame.display.set_caption("HELP ME")

    bg_trans_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'transparent_background.png')
    bg_trans = pygame.image.load(bg_trans_path).convert_alpha() #loads the filter for the background


    small_font = pygame.font.SysFont(None, 36)  #sets the fonts
    help_text = small_font.render("Use arrow keys or w, a, s, d keys to move", True, (255, 255, 255)) #renders the fonts and sets the colors
    help_text_rect = help_text.get_rect(center = (552.5, 150))

    info_text = small_font.render("press enter to go back, or esc to show main menu", True, (255, 255, 255))
    info_text_rect = info_text.get_rect(center = (552.5, 200))

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
done = True
while done:
    #title
    pygame.display.set_caption("Final Bloom")
    dt = clock.tick(60) / 1000.0 # Limit to 60 frames per second and get delta time in seconds # Limit to 60 frames per second #controls the frame rate
    #quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    
    #draw the tilemap
    for img, px, py in scaled_tiles:
        win.blit(img, (px, py))

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

    player_front_rect = player_front.get_rect(topleft=(x, y))
    player_right_rect = player_right.get_rect(topleft=(x, y))
    #draw the sprite
<<<<<<< Updated upstream
    win.blit(player_front, player_front_rect)
=======
    win.blit(player_front,(x, y))
>>>>>>> Stashed changes
    #movement code
    #moves charactoer for as long as the key gets held down in whatever direction i choose
    #set up a list to do this
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0: #checks the 
        x -= vel * dt
        win.blit(player_left, (x, y))
    if keys[pygame.K_RIGHT] and x < 1105:
        x += vel * dt
        win.blit(player_right, (x, y))
    if keys[pygame.K_UP]:
        y -= vel * dt
        win.blit(player_back, (x, y))
    if keys[pygame.K_DOWN]:
        y += vel * dt
        win.blit(player_front, (x, y))
    if keys[pygame.K_ESCAPE]:
        show_main_menu()


    #update the display
    pygame.display.update()

pygame.quit() #quit the game
