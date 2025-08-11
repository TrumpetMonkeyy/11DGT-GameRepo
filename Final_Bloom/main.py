#Final Bloom
#r4t0030
#version 1.2
#2025-07-22
# TODO: make the cam follow the sprite/hitboxes and fix all the bugs
import os
import sys#Final Bloom
#r4t0030 virtualvariant
#version 1.2
#2025-08-11
# TODO: make the cam follow the sprite
import os
import sys
import pygame
import pytmx
from pytmx.util_pygame import load_pygame


pygame.init()

#display
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(f"Screen resolution: {screen_width}x{screen_height}")
screen = ((screen_width, screen_height))
win = pygame.display.set_mode((screen), pygame.RESIZABLE)


#title
pygame.display.set_caption("Final Bloom")

#hides mouse cursor
pygame.mouse.set_visible(False)

#icons
image_path = os.path.join(os.path.dirname(__file__), 'assets', 'icons', 'icon.png')
game_icon = pygame.image.load(image_path)
pygame.display.set_icon(game_icon)
#load tilemap
tmx_path = os.path.join(os.path.dirname(__file__), 'maps', 'map1.tmx')
tmx_data = load_pygame(tmx_path)

#width and height for the sprite
sprite_width = 28
sprite_height = 44

# Load player sprite
sprite_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player.png')
player_sprite = pygame.image.load(sprite_path).convert_alpha()
player_sprite = pygame.transform.scale(player_sprite, (sprite_width, sprite_height))


scale = 2  #changes the scale 1=defalt
scaled_tiles = [] #the coordanets and image gets saved in this list
fence_rects = []

for layer in tmx_data.visible_layers:
    if isinstance(layer, pytmx.TiledTileLayer):
        for x_tile, y_tile, image in layer.tiles():
            #pulls the tiles from the file and skips the empty and non image tiles/code that helps the 3rd party aplacation
            if image:
                scaled_image = pygame.transform.scale(#resizeing the tiles
                    image,
                    (int(tmx_data.tilewidth * scale), int(tmx_data.tileheight * scale))
                )
                tile_x = x_tile * tmx_data.tilewidth * scale
                tile_y = y_tile * tmx_data.tileheight * scale
                scaled_tiles.append((scaled_image, tile_x, tile_y))

                # If it's the fence layer, store its rect
                if layer.name == "fences":
                    fence_rects.append(pygame.Rect(tile_x, tile_y, tmx_data.tilewidth * scale, tmx_data.tileheight * scale))


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

#put a rectangle around the player
player_rect = player_front.get_rect(topleft=(x, y))
# load rest of the sprites
tomb_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'tomb.png')
tomb_load = pygame.image.load(tomb_path).convert_alpha()
tomb = pygame.transform.scale(tomb_load, (84.25, 68.5))
tombs = [90, 50, 200, 150]

# Create tomb rectangles for collision detection
wind_tomb_rect = pygame.Rect(tombs[0], tombs[1], 84, 68)
fire_tomb_rect = pygame.Rect(tombs[2], tombs[3], 84, 68)
# set velocity to control the speed of the sprite
vel = 200

# set the co-ordinates of where the sprite will appear and its hight/width
x = screen[0]/2 - screen_width/2
y = screen[1]/2 - screen_height/2

#music
background_music_path = os.path.join(os.path.dirname(__file__), 'assets', 'audio', 'background_music.mp3')
e_hit_path = os.path.join(os.path.dirname(__file__), 'assets', 'audio', 'woush.flac')
background_music_sound = pygame.mixer.Sound(background_music_path)
e_hit_sound = pygame.mixer.Sound(e_hit_path)
background_music_channel = pygame.mixer.Channel(0)
e_hit_channel = pygame.mixer.Channel(1)

def play_background_music():
    background_music_channel.play(background_music_sound, loops=-1)
    background_music_channel.set_volume(0.25)
play_background_music()

def player_attack_sounds():
    e_hit_channel.play(e_hit_sound)
#abilitys
abilitys = []
abilitys_picked = 1

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
            show_help_menu()

def show_help_menu():
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
debug = False
collide = False
done = True
wind_tomb = True
fire_tomb = True


while done:
    #allows key inputs to actually be able to do things
    keys = pygame.key.get_pressed()
    #title
    pygame.display.set_caption("Final Bloom")
    dt = clock.tick(60) / 1000.0 # Limit to 60 frames per second and get delta time in seconds # Limit to 60 frames per second #controls the frame rate
    #quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        #debug mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                debug = not debug
            
        #abilatys
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button
                if "wind" in abilitys and abilitys_picked == 1:
                    player_attack_sounds()
                if "fire" in abilitys and abilitys_picked == 2:
                    print("fire")
               
    #draw the tilemap
    for img, px, py in scaled_tiles:
        win.blit(img, (px, py))

    #applys a rectangle to the player
    player_front_rect = player_front.get_rect(topleft=(x, y))
   
    #draw sprites
    player_rect = player_front.get_rect(topleft=(x, y))
    win.blit(player_front, (x, y))

    if wind_tomb:
        win.blit(tomb, (tombs[0], tombs[1]))
        tomb.get_rect()
    if fire_tomb:
        win.blit(tomb, (tombs[2], tombs[3]))

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
   



    #movement code
    #moves character for as long as the key gets held down in whatever direction i choose
    #set up a list to do this

    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= vel * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel * dt
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel * dt

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= vel * dt
        win.blit(player_left, (x, y))
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel * dt
        win.blit(player_right, (x, y))
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel * dt
        win.blit(player_back, (x, y))
    if keys[pygame.K_DOWN]:
        y += vel * dt
    if keys[pygame.K_ESCAPE]:
        show_main_menu()
       
    if debug == True:
        for rect in fence_rects:
            pygame.draw.rect(win, (255, 255, 255), rect, 2)

# abilitys
    if keys[pygame.K_1]:
        if "wind" in abilitys:
            abilitys_picked = 1
    
    if keys[pygame.K_2]:
        if "fire" in abilitys:
            abilitys_picked = 2

    print(abilitys_picked)
    print(abilitys)

    if player_rect.colliderect(wind_tomb_rect):
        if keys[pygame.K_b] and "wind" not in abilitys:
            wind_tomb = False
            abilitys.append("wind")
    if player_rect.colliderect(fire_tomb_rect):
        if keys[pygame.K_b] and "fire" not in abilitys:
            fire_tomb = False
            abilitys.append("fire")
    #update the display
    pygame.display.update()

pygame.quit() #quit the game
exit()
import pygame
import pytmx
from pytmx.util_pygame import load_pygame
import time
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
# set the co-ordinates of where the sprite will appear and its hight/width
x = screen[0]/2 - width/2 - 150
y = screen[1]/2 - height/2 - 20

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

player_rect = player_front.get_rect(topleft=(x, y))

# load rest of the sprites
tomb_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'tomb.png')
tomb_load = pygame.image.load(tomb_path).convert_alpha()
tomb = pygame.transform.scale(tomb_load, (84.25, 68.5))
tombs = [90, 50, 200, 150]

# Create tomb rectangles for collision detection
wind_tomb_rect = pygame.Rect(tombs[0], tombs[1], 84, 68)
fire_tomb_rect = pygame.Rect(tombs[2], tombs[3], 84, 68)
# set velocity to control the speed of the sprite
vel = 200



#music
background_music_path = os.path.join(os.path.dirname(__file__), 'assets', 'audio', 'background_music.mp3')
e_hit_path = os.path.join(os.path.dirname(__file__), 'assets', 'audio', 'woush.flac')
background_music_sound = pygame.mixer.Sound(background_music_path)
e_hit_sound = pygame.mixer.Sound(e_hit_path)
background_music_channel = pygame.mixer.Channel(0)
e_hit_channel = pygame.mixer.Channel(1)

def play_background_music():
    background_music_channel.play(background_music_sound, loops=-1)
    background_music_channel.set_volume(0.25)
play_background_music()

def player_attack_sounds():
    e_hit_channel.play(e_hit_sound)
#abilitys
abilitys = []
abilitys_picked = 1
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
wind_tomb = True
fire_tomb = True
while done:
    #title
    pygame.display.set_caption("Final Bloom")
    dt = clock.tick(60) / 1000.0 # Limit to 60 frames per second and get delta time in seconds # Limit to 60 frames per second #controls the frame rate
    #quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button
                if "wind" in abilitys and abilitys_picked == 1:
                    player_attack_sounds()
                if "fire" in abilitys and abilitys_picked == 2:
                    print("fire")

    #draw the tilemap
    for img, px, py in scaled_tiles:
        win.blit(img, (px, py))

    #draw the sprite
    if wind_tomb:
        win.blit(tomb, (tombs[0], tombs[1]))
        tomb.get_rect()
    if fire_tomb:
        win.blit(tomb, (tombs[2], tombs[3]))

    win.blit(player_front,(x, y))
    player_rect.topleft = (x, y)
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
    if keys[pygame.K_1]:
        if "wind" in abilitys:
            abilitys_picked = 1
    
    if keys[pygame.K_2]:
        if "fire" in abilitys:
            abilitys_picked = 2

    print(abilitys_picked)


    print(abilitys)

    if player_rect.colliderect(wind_tomb_rect):
        if keys[pygame.K_b] and "wind" not in abilitys:
            wind_tomb = False
            abilitys.append("wind")
    if player_rect.colliderect(fire_tomb_rect):
        if keys[pygame.K_b] and "fire" not in abilitys:
            fire_tomb = False
            abilitys.append("fire")
    #update the display
    pygame.display.update()

pygame.quit() #quit the game
