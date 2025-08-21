#Final Bloom
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

#uis
ui_1_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'ui_1.png')
ui_1 = pygame.image.load(ui_1_path).convert_alpha()
ui_2_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'ui_2.png')
ui_2 = pygame.image.load(ui_2_path).convert_alpha()
ui_3_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'ui_3.png')
ui_3 = pygame.image.load(ui_3_path).convert_alpha()
ui_4_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'ui_4.png')
ui_4 = pygame.image.load(ui_4_path).convert_alpha()

wind_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'wind.png')
wind = pygame.image.load(wind_path).convert_alpha()
fire_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'fire.png')
fire = pygame.image.load(fire_path).convert_alpha()
earth_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'fire.png')
earth = pygame.image.load(earth_path).convert_alpha()
water_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'fire.png')
water = pygame.image.load(water_path).convert_alpha()

empty_ui_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'empty_ui.png')
empty_ui = pygame.image.load(empty_ui_path).convert_alpha()
#put a rectangle around the player
player_rect = player_front.get_rect(topleft=(x, y))

# load rest of the sprites
tomb_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'tomb.png')
tomb_load = pygame.image.load(tomb_path).convert_alpha()
tomb = pygame.transform.scale(tomb_load, (84.25, 68.5))
tombs = [90, 50, 200, 150, 300, 300, 80, 90]

# Create tomb rectangles for collision detection
wind_tomb_rect = pygame.Rect(tombs[0], tombs[1], 84, 68)
fire_tomb_rect = pygame.Rect(tombs[2], tombs[3], 84, 68)
earth_tomb_rect = pygame.Rect(tombs[4], tombs[5], 84, 68)
water_tomb_rect = pygame.Rect(tombs[6], tombs[7], 84, 68)
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
abilitys_picked = 0

#enemies
#difficultys
difficulty_settings = {
    'easy': [
        5,
        65,  # Units per frame
        150, # Pixels
    ],
    'medium': [
        10,
        100,
        200,
    ],
    'hard': [
        18,
        200,
        350,
    ],
}

difficulty = 'easy'


def diff_menu(): 
    global difficulty1
    difficulty1 = 1
    global difficulty
    #title
    pygame.display.set_caption("Difficulty")

    bg_trans_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'transparent_background.png')
    bg_trans = pygame.image.load(bg_trans_path).convert_alpha() #loads the filter for the background

    small_font = pygame.font.SysFont(None, 36)  #sets the fonts
    info_text = small_font.render("press 'E' to select easy mode. 'H', for hard mode and 'I' for impossible", True, (255, 255, 255)) #renders the fonts and sets the colors
    info_text_rect = info_text.get_rect(center = (screen_width/2, screen_height*.56))
    while True:
        clock.tick(60)
        for img, px, py in scaled_tiles:
            win.blit(img, (px, py)) #shows the map
        win.blit(bg_trans, (0, 0)) #applys the filter ontop
        win.blit(info_text, info_text_rect) #displays the text and places them at coordanets
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    difficulty = "easy"
                    return difficulty
                if event.key == pygame.K_h:
                    difficulty = "medium"
                    return difficulty
                if event.key == pygame.K_i:
                    difficulty = "hard"
                    return difficulty
                return difficulty1
print(difficulty)
current_difficulty = difficulty_settings.get(difficulty, {})
print (current_difficulty)


enemy_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_front.png')
enemy_load = pygame.image.load(enemy_path).convert_alpha()
enemy = pygame.transform.scale(enemy_load, (sprite_width, sprite_height))



    
#frame rate
clock = pygame.time.Clock()

difficulty1 = 0
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
            if difficulty1 == 0:
                diff_menu()
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
# enemy settings

current_difficulty = difficulty_settings.get(difficulty, {})
num_enemies = current_difficulty[0]  # Change this number to add/remove enemies
enemy_speed = current_difficulty[1]
follow_radius = current_difficulty[2]  # enemies only follow player within this distance

# enemy positions - will auto-generate based on num_enemies
enemies = []
enemy_spawn_points = [
    [400, 300], [600, 400], [800, 200], [300, 500], 
    [700, 300], [500, 600], [200, 200], [900, 500],
    [100, 400], [750, 150], [350, 700], [550, 100]
]

# create enemies based on num_enemies setting
for i in range(num_enemies):
    if i < len(enemy_spawn_points):
        enemies.extend(enemy_spawn_points[i])  # adds x, y to the list

#game loop
debug = False
collide = False
done = True
wind_tomb = True
fire_tomb = True
earth_tomb = True
water_tomb = True


print(current_difficulty)
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
            # Move ability selection to event handling for immediate response
            elif event.key == pygame.K_1:
                abilitys_picked = 1
            elif event.key == pygame.K_2:
                abilitys_picked = 2
            elif event.key == pygame.K_3:
                abilitys_picked = 3
            elif event.key == pygame.K_4:
                abilitys_picked = 4
            
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


    #draw sprites and gets a rectangle around the player
    player_rect = player_front.get_rect(topleft=(x, y))

    if wind_tomb:
        win.blit(tomb, (tombs[0], tombs[1]))
        tomb.get_rect()
    if fire_tomb:
        win.blit(tomb, (tombs[2], tombs[3]))
    if earth_tomb:
        win.blit(tomb, (tombs[4], tombs[5]))
    if water_tomb:
        win.blit(tomb, (tombs[6], tombs[7]))

    # draw enemies
    for i in range(0, len(enemies), 2):
        win.blit(enemy, (enemies[i], enemies[i + 1]))

    # move enemies towards player (only if within follow radius)
    for i in range(0, len(enemies), 2):
        enemy_x = enemies[i]
        enemy_y = enemies[i + 1]
        
        # simple distance check (no complex math)
        x_distance = abs(x - enemy_x)
        y_distance = abs(y - enemy_y)
        
        # only move if close enough (simple rectangle check)
        if x_distance < follow_radius and y_distance < follow_radius:
            if x > enemy_x:
                enemies[i] += enemy_speed * dt
            if x < enemy_x:
                enemies[i] -= enemy_speed * dt
            if y > enemy_y:
                enemies[i + 1] += enemy_speed * dt
            if y < enemy_y:
                enemies[i + 1] -= enemy_speed * dt

    # Check collision with enemies
    for i in range(0, len(enemies), 2):
        if (enemies[i] - 20) <= x <= (enemies[i] + 20) and (enemies[i + 1] - 20) <= y <= (enemies[i + 1] + 20):
            print(f"Hit by enemy {i//2 + 1}!")

    for fence in fence_rects:
        if player_rect.colliderect(fence):
            collide = True



    #collision
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
    if not keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_LEFT] or keys[pygame.K_a]:
        win.blit(player_front, (x, y))
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= vel * dt
        win.blit(player_left, (x, y))
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel * dt
        win.blit(player_right, (x, y))
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel * dt
        win.blit(player_back, (x, y))
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += vel * dt

    if keys[pygame.K_ESCAPE]:
        show_main_menu()
       
    if debug == True:
        for rect in fence_rects:
            pygame.draw.rect(win, (255, 255, 255), rect, 2)
        # Draw enemy positions and follow radius
        for i in range(0, len(enemies), 2):
            enemy_x = enemies[i]
            enemy_y = enemies[i + 1]
            pygame.draw.rect(win, (255, 0, 0), (enemy_x, enemy_y, sprite_width, sprite_height), 2)
            pygame.draw.circle(win, (255, 255, 0), (int(enemy_x + sprite_width/2), int(enemy_y + sprite_height/2)), follow_radius, 1)

    if abilitys_picked == 0:
        win.blit(empty_ui, (0, 0))
    if abilitys_picked == 1:
        win.blit(ui_1, (0, 0))
    if abilitys_picked == 2:
        win.blit(ui_2, (0, 0))
    if abilitys_picked == 3:
        win.blit(ui_3, (0, 0))
    if abilitys_picked == 4:
        win.blit(ui_4, (0, 0))

    if "wind" in abilitys:
        win.blit(wind, (6, 6))
    if "fire" in abilitys:
        win.blit(fire, (81, 6))
    if "water" in abilitys:
        win.blit(water, (156, 6))
    if "earth" in abilitys:
        win.blit(earth, (231, 6))
    if player_rect.colliderect(wind_tomb_rect):
        if keys[pygame.K_b] and "wind" not in abilitys:
            wind_tomb = False
            abilitys.append("wind")
    if player_rect.colliderect(fire_tomb_rect):
        if keys[pygame.K_b] and "fire" not in abilitys:
            fire_tomb = False
            abilitys.append("fire")  
    if player_rect.colliderect(earth_tomb_rect):
        if keys[pygame.K_b] and "earth" not in abilitys:
            earth_tomb = False
            abilitys.append("earth")
    if player_rect.colliderect(water_tomb_rect):
        if keys[pygame.K_b] and "water" not in abilitys:
            water_tomb = False
            abilitys.append("water")
    #update the display
    pygame.display.update()

pygame.quit() #quit the game
exit()