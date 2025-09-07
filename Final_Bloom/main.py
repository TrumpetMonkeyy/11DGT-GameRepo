# Final Bloom
# r4t0030 virtualvariant
# version 2.2
# 2025-09-1

import os
import sys
import pygame
import pytmx
from pytmx.util_pygame import load_pygame


pygame.init()

# display
import tkinter as tk

# sets the screen size
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(f"Screen resolution: {screen_width}x{screen_height}")
screen = ((screen_width, screen_height))
win = pygame.display.set_mode((screen), pygame.RESIZABLE)


# title
pygame.display.set_caption("Final Bloom")

# hides mouse cursor
pygame.mouse.set_visible(False)

# icons
image_path = os.path.join(os.path.dirname(__file__), 'assets', 'icons', 'icon.png')
game_icon = pygame.image.load(image_path)
pygame.display.set_icon(game_icon)
# load tilemap
tmx_path = os.path.join(os.path.dirname(__file__), 'maps', 'map1.tmx')
tmx_data = load_pygame(tmx_path)

# width and height for the sprite
sprite_width = 27
sprite_height = 44


scale = 2  # changes the scale 1=defalt
scaled_tiles = [] # the coordanets and image gets saved in this list
fence_rects = []

for layer in tmx_data.visible_layers:
    if isinstance(layer, pytmx.TiledTileLayer):
        for x_tile, y_tile, image in layer.tiles():
            # pulls the tiles from the file and skips the empty and non image tiles/code that helps the 3rd party aplacation
            if image:
                scaled_image = pygame.transform.scale(# resizeing the tiles
                    image,
                    (int(tmx_data.tilewidth * scale), int(tmx_data.tileheight * scale))
                )
                tile_x = x_tile * tmx_data.tilewidth * scale
                tile_y = y_tile * tmx_data.tileheight * scale
                scaled_tiles.append((scaled_image, tile_x, tile_y))

                # If it's the fence layer, store its rect (relative to map, not screen)
                if layer.name == "fences":
                    # Create smaller fence hitboxes (half size, centered)
                    fence_width = (tmx_data.tilewidth * scale) // 1.5
                    fence_height = (tmx_data.tileheight * scale) // 1.5
                    fence_x = tile_x + ((tmx_data.tilewidth * scale) - fence_width) // 1.5
                    fence_y = tile_y + ((tmx_data.tileheight * scale) - fence_height) // 2
                    fence_rects.append(pygame.Rect(fence_x, fence_y, fence_width, fence_height))


# set the co-ordinates of where the sprite will appear and its hight/width
x = screen_width / 2
y = screen_height / 2
hitbox_width = sprite_width // 2    # 27 // 2 = 13 pixels wide
hitbox_height = sprite_height // 2 - 10  # 44 // 2 = 22 pixels tall

# Center the hitbox within the sprite
hitbox_x = x + (sprite_width - hitbox_width) // 2   # Center horizontally
hitbox_y = y + (hitbox_height *2) # Center vertically

# Load player sprite's
player_front_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_front.png')# finds the player path
player_front_load = pygame.image.load(player_front_path).convert_alpha() # loads the sprite
player_front = pygame.transform.scale(player_front_load, (sprite_width, sprite_height)) # resize the sprite

player_right_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_right.png')
player_right_load = pygame.image.load(player_right_path).convert_alpha()
player_right = pygame.transform.scale(player_right_load, (sprite_width, sprite_height))

player_left_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_left.png')
player_left_load = pygame.image.load(player_left_path).convert_alpha()
player_left = pygame.transform.scale(player_left_load, (sprite_width, sprite_height))

player_back_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'player_back.png')
player_back_load = pygame.image.load(player_back_path).convert_alpha()
player_back = pygame.transform.scale(player_back_load, (sprite_width, sprite_height))

player_wind_left_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'windL.png')
player_wind_left_load = pygame.image.load(player_wind_left_path).convert_alpha()
sprite_animation_width, sprite_animation_height = player_wind_left_load.get_size()
player_wind_left = pygame.transform.scale(player_wind_left_load, (sprite_animation_width * 2, sprite_animation_height * 2))

# Load fire attack sprite
player_fire_left_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'fireL.png')
player_fire_left_load = pygame.image.load(player_fire_left_path).convert_alpha()
fire_animation_width, fire_animation_height = player_fire_left_load.get_size()
player_fire_left = pygame.transform.scale(player_fire_left_load, (fire_animation_width * 2, fire_animation_height * 2))

# Load earth attack sprite
player_earth_left_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'earthL.png')
player_earth_left_load = pygame.image.load(player_earth_left_path).convert_alpha()
earth_animation_width, earth_animation_height = player_earth_left_load.get_size()
player_earth_left = pygame.transform.scale(player_earth_left_load, (earth_animation_width * 2, earth_animation_height * 2))

# Load water attack sprite
player_water_left_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'waterL.png')
player_water_left_load = pygame.image.load(player_water_left_path).convert_alpha()
water_animation_width, water_animation_height = player_water_left_load.get_size()
player_water_left = pygame.transform.scale(player_water_left_load, (water_animation_width * 2, water_animation_height * 2))

# Load death sprite
death_left_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'deathR.png')
death_left_load = pygame.image.load(death_left_path).convert_alpha()
death_width, death_hight = death_left_load.get_size()
death_left = pygame.transform.scale(death_left_load, (death_width/4, death_hight/4))

# uis
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
earth_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'earth.png')
earth = pygame.image.load(earth_path).convert_alpha()
water_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'water.png')
water = pygame.image.load(water_path).convert_alpha()
empty_ui_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'empty_ui.png')
empty_ui = pygame.image.load(empty_ui_path).convert_alpha()

heart_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'heart_64x64.png')
heart = pygame.image.load(heart_path).convert_alpha()
heart_width, heart_height = heart.get_size()
dead_heart_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'ui', 'dead_heart_64x64.png')
dead_heart = pygame.image.load(dead_heart_path).convert_alpha()
# put a rectangle around the player for hitboxes
player_rect = player_front.get_rect(topleft=(x, y))

# load tomes - different sprite for each element
wind_tomb_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'wind.png')
fire_tomb_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'fire.png')
earth_tomb_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'earth.png')
water_tomb_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'water.png')
# Try to load individual tome sprites
wind_tomb_load = pygame.image.load(wind_tomb_path).convert_alpha()
wind_tomb_sprite = pygame.transform.scale(wind_tomb_load, (21*2+8, 29*2+8))
fire_tomb_load = pygame.image.load(fire_tomb_path).convert_alpha()
fire_tomb_sprite = pygame.transform.scale(fire_tomb_load, (271/5, 344/5))
earth_tomb_load = pygame.image.load(earth_tomb_path).convert_alpha()
earth_tomb_sprite = pygame.transform.scale(earth_tomb_load, (24*2, 32*2))
water_tomb_load = pygame.image.load(water_tomb_path).convert_alpha()
water_tomb_width, water_tomb_hight = water_tomb_load.get_size()
water_tomb_sprite = pygame.transform.scale(water_tomb_load, (water_tomb_width/5, water_tomb_hight/5))

#load walls
side_wall_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'wall_side.png')
flat_wall_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'wall_bottom.png')
side_wall_load = pygame.image.load(side_wall_path).convert_alpha()
flat_wall_load = pygame.image.load(flat_wall_path).convert_alpha()
flat_wall_width, flat_wall_hight = flat_wall_load.get_size()
side_wall_width, side_wall_hight = side_wall_load.get_size()
side_wall = pygame.transform.scale(side_wall_load, (side_wall_width*4, side_wall_hight*4))
flat_wall = pygame.transform.scale(flat_wall_load, (flat_wall_width*4, flat_wall_hight*4))

tombs = [90, 50, 200, 150, 300, 300, 80, 90]

# Wall system - list of wall positions and types
# Each wall entry: [x, y, wall_type] where wall_type is "side" or "flat"
wall_locations = [
    [80, 80, "side"],     # side wall at position (80, 80)
    [100, 100, "flat"],   # flat wall at position (100, 100)
    [200, 150, "side"],   # add more walls as needed
    [300, 200, "flat"],
    [400, 100, "side"],
]

# Create wall rectangles for collision detection
wall_rects = []
for wall_data in wall_locations:
    wall_x, wall_y, wall_type = wall_data
    if wall_type == "side":
        wall_width = side_wall_width * 4
        wall_height = side_wall_hight * 4
    else:  # flat wall
        wall_width = flat_wall_width * 4
        wall_height = flat_wall_hight * 4
    
    wall_rects.append({
        'rect': pygame.Rect(wall_x, wall_y, wall_width, wall_height),
        'type': wall_type,
        'x': wall_x,
        'y': wall_y
    })

# load enemys
enemy_path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', 'Efront.png')
enemy_load = pygame.image.load(enemy_path).convert_alpha()
# Set custom enemy dimensions (change these values to resize enemies)
enemy_width = 35  # Make enemies wider than player (was 27)
enemy_height = 50  # Make enemies taller than player (was 44)
enemy_sprite = pygame.transform.scale(enemy_load, (enemy_width, enemy_height))


# set velocity to control the speed of the sprite
vel = 200


# music
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

# abilitys
abilitys = []
abilitys_picked = 0


# difficultys
difficulty_settings = {
    'easy': [
        5,   # Number of enemies
        65,  # Enemy speed (units per frame)
        150, # Follow radius (pixels)
        3,   # Enemy health
        50,  # Base knockback strength
        8,   # Player health
    ],
    'medium': [
        10, # num of enemies
        100, # speed
        200, # player detection
        5,   # Enemy health
        40,  # Base knockback strength
        5,   # Player health
    ],
    'hard': [
        18, # num of enemies
        200, # speed
        350, # player detection
        8,   # Enemy health
        30,  # Base knockback strength
        3,   # Player health
    ],
}

# Ability damage and knockback values (damage, knockback_multiplier)
ability_stats = {
    'wind': {'damage': 0.5, 'knockback_multiplier': 10.0, 'description': 'low damage, high knockback'},
    'fire': {'damage': 2, 'knockback_multiplier': 0.7, 'description': 'High damage, low knockback'},
    'water': {'damage': 1, 'knockback_multiplier': 5.0, 'description': 'medium damage, high knockback'},
    'earth': {'damage': 3, 'knockback_multiplier': 0.5, 'description': 'Very high damage, very low knockback'}
}

difficulty = 'easy'

def diff_menu(): 
    global difficulty1
    difficulty1 = 1
    global difficulty
    # title
    pygame.display.set_caption("Difficulty")

    bg_trans_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'transparent_background.png')
    bg_trans = pygame.image.load(bg_trans_path).convert_alpha() # loads the filter for the background

    small_font = pygame.font.SysFont(None, 36)  # sets the fonts
    info_text = small_font.render("press 'E' to select easy mode. 'H', for hard mode and 'I' for impossible", True, (255, 255, 255)) # renders the fonts and sets the colors
    info_text_rect = info_text.get_rect(center = (screen_width/2, screen_height*.56))
    while True:
        clock.tick(60)
        for img, px, py in scaled_tiles:
            win.blit(img, (px, py)) # shows the map
        win.blit(bg_trans, (0, 0)) # applys the filter ontop
        win.blit(info_text, info_text_rect) # displays the text and places them at coordanets
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    difficulty = "easy"
                    return difficulty
                elif event.key == pygame.K_h:
                    difficulty = "medium"
                    return difficulty
                elif event.key == pygame.K_i:
                    difficulty = "hard"
                    return difficulty
current_difficulty = difficulty_settings.get(difficulty, {})
print(current_difficulty)

# Initialize attack rectangles (positions will be updated each frame)
attack_rect_r = pygame.Rect(0, 0, 70, 80)
attack_rect_l = pygame.Rect(0, 0, 60, 80)


# frame rate
clock = pygame.time.Clock()

difficulty1 = 0
# main menu
def show_main_menu():
    # title
    pygame.display.set_caption("main menu")

    bg_trans_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'transparent_background.png')
    bg_trans = pygame.image.load(bg_trans_path).convert_alpha() # loads the filter for the background

    title_font_path = os.path.join(os.path.dirname(__file__), 'assets', 'fonts', 'CASTELAR.ttf')
    title_font = pygame.font.Font(title_font_path, 72) # sets the fonts
    small_font = pygame.font.SysFont(None, 36)

    title_text = title_font.render("Final Bloom", True, (200, 200, 200)) # renders the fonts and sets the colors
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
            win.blit(img, (px, py)) # shows the map
        win.blit(bg_trans, (0, 0)) # applys the filter ontop

        win.blit(title_text, title_text_rect) # places out the text in the coordanets
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
    # title
    pygame.display.set_caption("HELP ME")

    bg_trans_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'transparent_background.png')
    bg_trans = pygame.image.load(bg_trans_path).convert_alpha() # loads the filter for the background


    small_font = pygame.font.SysFont(None, 36)  # sets the fonts

    help_text = small_font.render("Use arrow keys or WASD keys to move", True, (255, 255, 255))
    help_text_rect = help_text.get_rect(center=(screen_width // 2, screen_height // 2 - 70))

    help_text1 = small_font.render("To attack an enemy use [E or /] depending on your movement keys", True, (255, 255, 255))
    help_text1_rect = help_text1.get_rect(center=(screen_width // 2, screen_height // 2 - 30))

    info_text1 = small_font.render("To collect tomes press 'B' while on top of one", True, (255, 255, 255))
    info_text_rect1 = info_text1.get_rect(center=(screen_width // 2, screen_height // 2 + 10))

    ability_info_text1 = small_font.render("Wind: low damage, very high knockback | Fire: High damage, low knockback", True, (255, 255, 255))
    ability_info_text_rect1 = ability_info_text1.get_rect(center=(screen_width // 2, screen_height // 2 - 300))
    ability_info_text2 = small_font.render("Water: medium damage, high knockback | Earth: Very high damage, very low knockback", True, (255, 255, 255))
    ability_info_text_rect2 = ability_info_text2.get_rect(center=(screen_width // 2, screen_height // 2 - 260))
    ability_info_text3 = small_font.render("These are diffrent eliments you will get to obtane along your jerny.", True, (255, 255, 255))
    ability_info_text_rect3 = ability_info_text3.get_rect(center=(screen_width // 2, screen_height // 2 - 220))
    ability_info_text4 = small_font.render(" Take the time to get used to the goods and bads of each of them.", True, (255, 255, 255))
    ability_info_text_rect4 = ability_info_text4.get_rect(center=(screen_width // 2, screen_height // 2 - 180))

    info_text = small_font.render("Press ENTER to start playing, or ESC to go back to the menu", True, (255, 255, 255))
    info_text_rect = info_text.get_rect(center=(screen_width // 2, screen_height // 2 + 90))

    while True:
        # win.fill((0, 0, 0)) # sets the background to black  
        clock.tick(60)
        for img, px, py in scaled_tiles:
            win.blit(img, (px, py)) # shows the map
        win.blit(bg_trans, (0, 0)) # applys the filter ontop

        win.blit(help_text, help_text_rect) # displays the text and places them at coordanets
        win.blit(info_text, info_text_rect)
        win.blit(help_text1, help_text1_rect)
        win.blit(info_text1, info_text_rect1)
        
        win.blit(ability_info_text1, ability_info_text_rect1)
        win.blit(ability_info_text2, ability_info_text_rect2)
        win.blit(ability_info_text3, ability_info_text_rect3)  
        win.blit(ability_info_text4, ability_info_text_rect4)
        for event in pygame.event.get(): # looks for key presses and sets them to do somthing
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return
        if keys[pygame.K_ESCAPE]:
            show_main_menu()
       
        pygame.display.update()

def game_over():
    # title
    pygame.display.set_caption("Game Over")

    bg_trans_path = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'transparent_background.png')
    bg_trans = pygame.image.load(bg_trans_path).convert_alpha() # loads the filter for the background

    small_font = pygame.font.SysFont(None, 36)  # sets the fonts

    help_text = small_font.render("your jerny has sadly come to an end", True, (255, 255, 255))
    help_text_rect = help_text.get_rect(center=(screen_width // 2, screen_height // 2 - 80))
    help_text1 = small_font.render("you have failed to save New Zealand from 'Death'", True, (255, 255, 255))
    help_text1_rect = help_text1.get_rect(center=(screen_width // 2, screen_height // 2 - 40))
    info_text1 = small_font.render("to restart press 'R'", True, (255, 255, 255))
    info_text_rect1 = info_text1.get_rect(center=(screen_width // 2, screen_height // 2))
    info_text2 = small_font.render("or press 'esc' to quit", True, (255, 255, 255))
    info_text_rect2 = info_text2.get_rect(center=(screen_width // 2, screen_height // 2 + 40))

    while True:
        clock.tick(60)
        for img, px, py in scaled_tiles:
            win.blit(img, (px, py)) # shows the map
        win.blit(bg_trans, (0, 0)) # applys the filter ontop

        win.blit(help_text, help_text_rect) # displays the text and places them at coordanets
        win.blit(help_text1, help_text1_rect)
        win.blit(info_text1, info_text_rect1)
        win.blit(info_text2, info_text_rect2)
        
        for event in pygame.event.get(): # looks for key presses and sets them to do somthing
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return "restart"  # Return a signal to restart the game
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
       
        pygame.display.update()


show_main_menu() # runs the start menu before the game runs
# enemy settings

current_difficulty = difficulty_settings.get(difficulty, {})
num_enemies = current_difficulty[0]  # Number of enemies
enemy_speed = current_difficulty[1] # Enemy speed based on difficulty
follow_radius = current_difficulty[2]  # enemies only follow player within this distance
enemy_max_health = current_difficulty[3]  # Enemy health
knockback_strength = current_difficulty[4]  # Knockback strength
player_max_health = current_difficulty[5]  # Player health from difficulty
print(f"Difficulty: {difficulty}")

# Initialize player health system
player_health = player_max_health

# enemy positions and data - using a more organized structure
enemy = []
enemies = []
enemy_spawn_points = [
    [400, 300], [600, 400], [800, 200], [300, 500], 
    [700, 300], [500, 600], [200, 200], [900, 500],
    [100, 400], [750, 150], [350, 700], [550, 100]
]

# Create enemies with health, position, and flash data
for i in range(num_enemies):
    if i < len(enemy_spawn_points):
        enemies.append({
            'x': enemy_spawn_points[i][0],
            'y': enemy_spawn_points[i][1], 
            'health': enemy_max_health,
            'max_health': enemy_max_health,
            'flash_time': 0,  # For white flash effect
            'knockback_x': 0,  # Knockback velocity
            'knockback_y': 0
        })

# game loop
debug = False # setting up all the verables needed to do things
collide = False
done = True
wind_tomb = True
fire_tomb = True
earth_tomb = True
water_tomb = True
w_attack = None
f_attack = None
e_attack = None
a_attack = None
# allow the tilemap to move with the player
cam_x = 0
cam_y = 0

last_enemy_hit_time = 0 # the time when the enemy hit the player last
animation_time = 0
while done:
    # allows key inputs to actually be able to do things
    keys = pygame.key.get_pressed()
    # title
    pygame.display.set_caption("Final Bloom")
    dt = clock.tick(60) / 1000.0 # Limit to 60 frames per second and get delta time in seconds # Limit to 60 frames per second # controls the frame rate
    
    # Update attack rectangles first, before processing events
    attack_rect_r.topleft = (x + sprite_width/2, y - sprite_height/2)
    attack_rect_l.topleft = (x - 45, y - sprite_height/2)
    
    # quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        # debug mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                debug = not debug
            # sets a verable that changes the ability you selected
            elif event.key == pygame.K_1:
                abilitys_picked = 1
            elif event.key == pygame.K_2:
                abilitys_picked = 2
            elif event.key == pygame.K_3:
                abilitys_picked = 3
            elif event.key == pygame.K_4:
                abilitys_picked = 4
            
        # abilatys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e or event.key == pygame.K_SLASH:
                # Determine which ability to use based on selection
                current_ability = None
                if "wind" in abilitys and abilitys_picked == 1:
                    current_ability = "wind"
                elif "fire" in abilitys and abilitys_picked == 2:
                    current_ability = "fire"
                elif "water" in abilitys and abilitys_picked == 3:
                    current_ability = "water"
                elif "earth" in abilitys and abilitys_picked == 4:
                    current_ability = "earth"
                
                if current_ability:
                    # Get ability stats
                    ability_damage = ability_stats[current_ability]['damage']
                    ability_knockback = ability_stats[current_ability]['knockback_multiplier']
                    
                    # Check if any enemy is inside the attack hitbox
                    enemies_to_remove = []
                    for i, enemy in enumerate(enemies):
                        # Convert enemy world coordinates to screen coordinates
                        enemy_screen_x = enemy['x'] + cam_x
                        enemy_screen_y = enemy['y'] + cam_y
                        enemy_rect = pygame.Rect(enemy_screen_x, enemy_screen_y, enemy_width, enemy_height)
                        
                        hit_direction = None
                        # Check for collision with attack rectangles
                        if attack_rect_r.colliderect(enemy_rect):
                            hit_direction = "right"
                        elif attack_rect_l.colliderect(enemy_rect):
                            hit_direction = "left"
                        
                        if hit_direction:
                            # Deal damage based on ability
                            enemy['health'] -= ability_damage
                            enemy['flash_time'] = pygame.time.get_ticks()  # Start white flash
                            
                            # Calculate knockback direction (away from player)
                            dx = enemy['x'] - (x - cam_x)  # World coordinates
                            dy = enemy['y'] - (y - cam_y)
                            distance = max(1, (dx**2 + dy**2)**0.5)  # Prevent division by zero
                            
                            # Apply knockback with ability-specific multiplier
                            final_knockback = knockback_strength * ability_knockback
                            enemy['knockback_x'] = (dx / distance) * final_knockback
                            enemy['knockback_y'] = (dy / distance) * final_knockback
                            
                            # Set attack animation
                            if current_ability == "wind":
                                w_attack = hit_direction
                            elif current_ability == "fire":
                                f_attack = hit_direction
                            elif current_ability == "earth":
                                e_attack = hit_direction
                            elif current_ability == "water":
                                a_attack = hit_direction
                            animation_time = pygame.time.get_ticks()
                            player_attack_sounds()
                            
                            # Print damage info
                            if debug == True:
                                print(f"{current_ability.capitalize()} attack Damage: {ability_damage}, Health: {enemy['health']}/{enemy['max_health']}")
                                                        
                            # Mark for removal if health <= 0
                            if enemy['health'] <= 0:
                                enemies_to_remove.append(i)
                                if debug == True:
                                    print(f"Enemy defeated by {current_ability}!")
                    
                    # Remove defeated enemies (from back to front to avoid index issues)
                    for i in reversed(enemies_to_remove):
                        del enemies[i]

    # draw the tilemap
    for img, px, py in scaled_tiles:
        win.blit(img, (px + cam_x, py + cam_y))
    # win.blit(vignette, (0, 0))
    # applies a rectangle to the player
    # draw sprites

    # Create the custom hitbox
    player_rect = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)
    win.blit(player_front, (x, y))

    # Draw all walls from the wall_locations list
    for wall_data in wall_locations:
        wall_x, wall_y, wall_type = wall_data
        if wall_type == "side":
            win.blit(side_wall, (wall_x + cam_x, wall_y + cam_y))
        else:  # flat wall
            win.blit(flat_wall, (wall_x + cam_x, wall_y + cam_y))
    # Create tomb rectangles for collision detection
    wind_tomb_rect = pygame.Rect(tombs[0] + cam_x, tombs[1] + cam_y, 84, 68)
    fire_tomb_rect = pygame.Rect(tombs[2] + cam_x, tombs[3] + cam_y, 84, 68)
    earth_tomb_rect = pygame.Rect(tombs[4] + cam_x, tombs[5] + cam_y, 84, 68)
    water_tomb_rect = pygame.Rect(tombs[6] + cam_x, tombs[7] + cam_y, 84, 68)
    
    # Check wall collisions
    for wall in wall_rects:
        # Adjust wall position by camera offset for collision detection
        wall_screen_rect = wall['rect'].move(cam_x, cam_y)
        if player_rect.colliderect(wall_screen_rect):
            collide = True

    # Check fence collisions
    for fence in fence_rects:
        # Adjust fence position by camera offset for collision detection
        fence_screen_rect = fence.move(cam_x, cam_y)
        if player_rect.colliderect(fence_screen_rect):
            collide = True
    # displays the diff tombs to the screen with unique sprites
    if wind_tomb:
        win.blit(wind_tomb_sprite, (tombs[0] + cam_x, tombs[1]+ cam_y))
    if fire_tomb:
        win.blit(fire_tomb_sprite, (tombs[2] + cam_x, tombs[3] + cam_y))
    if earth_tomb:
        win.blit(earth_tomb_sprite, (tombs[4] + cam_x, tombs[5] + cam_y))
    if water_tomb:
        win.blit(water_tomb_sprite, (tombs[6] + cam_x, tombs[7] + cam_y))

    # Update and draw enemies with health, knockback, and flash effects
    current_time = pygame.time.get_ticks()
    
    for enemy in enemies:
        # Apply knockback (gradually reduce it)
        enemy['x'] += enemy['knockback_x'] * dt
        enemy['y'] += enemy['knockback_y'] * dt
        enemy['knockback_x'] *= 0.85  # Reduce knockback over time
        enemy['knockback_y'] *= 0.85
        
        # Convert to screen coordinates
        enemy_screen_x = enemy['x'] + cam_x
        enemy_screen_y = enemy['y'] + cam_y
        
        # Check distance to player for movement
        x_distance = abs(x - enemy_screen_x)
        y_distance = abs(y - enemy_screen_y)
        
        # Move towards player if within follow radius and knockback is minimal
        if (x_distance < follow_radius and y_distance < follow_radius and 
            abs(enemy['knockback_x']) < 5 and abs(enemy['knockback_y']) < 5):
            
            # Store original position for collision checking
            original_x = enemy['x']
            original_y = enemy['y']
            
            # Move enemy towards player
            if x > enemy_screen_x:
                enemy['x'] += enemy_speed * dt
            elif x < enemy_screen_x:
                enemy['x'] -= enemy_speed * dt
            if y > enemy_screen_y:
                enemy['y'] += enemy_speed * dt
            elif y < enemy_screen_y:
                enemy['y'] -= enemy_speed * dt
            

            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], enemy_width, enemy_height)
            collision_detected = False
            
            for fence in fence_rects:
                if enemy_rect.colliderect(fence):
                    collision_detected = True
                    break
                        # Check wall collision
            if not collision_detected:
                for wall in wall_rects:
                    if enemy_rect.colliderect(wall['rect']):
                        collision_detected = True
                        break
                    
            if collision_detected:
                # Revert to original position
                enemy['x'] = original_x
                enemy['y'] = original_y
        
        # Create enemy sprite (white flash effect)
        enemy_surface = enemy_sprite.copy()
        if current_time - enemy['flash_time'] < 200:  # Flash for 200ms
            # Create white flash effect
            white_surface = pygame.Surface(enemy_surface.get_size())
            white_surface.fill((255, 255, 255))
            white_surface.set_alpha(180)  # Semi-transparent white
            enemy_surface.blit(white_surface, (0, 0), special_flags=pygame.BLEND_ADD)
        
        # Draw enemy
        win.blit(enemy_surface, (enemy_screen_x, enemy_screen_y))
        
        # Draw health bar above enemy 
        if enemy['health'] < enemy['max_health']:
            bar_width = 30
            bar_height = 5
            bar_x = enemy_screen_x + (enemy_width - bar_width) // 2
            bar_y = enemy_screen_y - 8
            
            # Background (red)
            pygame.draw.rect(win, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
            # Health (green)
            health_width = int((enemy['health'] / enemy['max_health']) * bar_width)
            pygame.draw.rect(win, (0, 255, 0), (bar_x, bar_y, health_width, bar_height))
    
    # Check if wind attack animation should be hidden after 1 second
    if w_attack == "left" and current_time - animation_time > 1000:
        w_attack = None
    if w_attack == "right" and current_time - animation_time > 1000:
        w_attack = None
    
    # Fire attack timeout
    if f_attack == "left" and current_time - animation_time > 1000:
        f_attack = None
    if f_attack == "right" and current_time - animation_time > 1000:
        f_attack = None
    
    # Earth attack timeout
    if e_attack == "left" and current_time - animation_time > 1000:
        e_attack = None
    if e_attack == "right" and current_time - animation_time > 1000:
        e_attack = None
    
    # Water attack timeout
    if a_attack == "left" and current_time - animation_time > 1000:
        a_attack = None
    if a_attack == "right" and current_time - animation_time > 1000:
        a_attack = None

    # Check collision with enemies
    for i, enemy in enumerate(enemies):
        enemy_screen_x = enemy['x'] + cam_x
        enemy_screen_y = enemy['y'] + cam_y
        if (enemy_screen_x - 20) <= x <= (enemy_screen_x + 20) and (enemy_screen_y - 20) <= y <= (enemy_screen_y + 20):
            # Only print if at least 1 second has passed since last hit
            if current_time - last_enemy_hit_time > 1000:
                if debug == True:
                    print(f"Hit by enemy {i + 1}!")
                player_health -= 1
                last_enemy_hit_time = current_time

    for fence in fence_rects:
        # Adjust fence position by camera offset for collision detection
        fence_screen_rect = fence.move(cam_x, cam_y)
        if player_rect.colliderect(fence_screen_rect):
            collide = True



    # tome collision
    if collide == True:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            cam_y -= vel * dt
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            cam_x -= vel * dt
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            cam_y += vel * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            cam_x += vel * dt
        collide = False
   

    # movement code
    # moves character for as long as the key gets held down in whatever direction i choose
    # set up a list to do this
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and collide == False or keys[pygame.K_w] and collide == False:
        cam_y += vel * dt
        win.blit(player_back, (x, y))
    if keys[pygame.K_LEFT] and collide == False or keys[pygame.K_a] and collide == False:
        cam_x += vel * dt
        win.blit(player_left, (x, y))
    if keys[pygame.K_RIGHT] and collide == False or keys[pygame.K_d] and collide == False:
        cam_x -= vel * dt
        win.blit(player_right, (x, y))
    if keys[pygame.K_DOWN] and collide == False or keys[pygame.K_s] and collide == False:
        cam_y -= vel * dt
        win.blit(player_front, (x, y))
    if keys[pygame.K_ESCAPE]:
        show_main_menu()
       
    if debug == True: # debug menu
        pygame.draw.rect(win, (255, 0, 0), attack_rect_r)  # Draws a red rectangle for attack_rect
        pygame.draw.rect(win, (255, 255, 0), attack_rect_l)  # Draws a rectangle for attack_rect
        
        # Draw fence hitboxes
        for rect in fence_rects:
            fence_screen_rect = rect.move(cam_x, cam_y)
            pygame.draw.rect(win, (255, 255, 255), fence_screen_rect, 2)
        
        # Draw wall hitboxes
        for wall in wall_rects:
            wall_screen_rect = wall['rect'].move(cam_x, cam_y)
            pygame.draw.rect(win, (0, 255, 255), wall_screen_rect, 2)  # Cyan for walls
        
        win.blit(player_front, (x,y))
        # Draw the player's hitbox for debugging/visualization
        pygame.draw.rect(win, (0, 255, 0), player_rect, 2)
        # Draw enemy positions and follow radius
        for enemy in enemies:
            enemy_x = enemy['x'] + cam_x
            enemy_y = enemy['y'] + cam_y
            pygame.draw.rect(win, (255, 0, 0), (enemy_x, enemy_y, enemy_width, enemy_height), 2)
            pygame.draw.circle(win, (255, 255, 0), (int(enemy_x + enemy_width/2), int(enemy_y + enemy_height/2)), follow_radius, 1)


    # ui
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
    
    # Display current ability stats
    if abilitys_picked > 0:
        ability_names = ["", "wind", "fire", "water", "earth"]
        if abilitys_picked <= 4:
            current_ability_name = ability_names[abilitys_picked]
            if current_ability_name in abilitys and current_ability_name in ability_stats:
                stats = ability_stats[current_ability_name]
                font_small = pygame.font.SysFont(None, 25)
                
                # Display ability info
                ability_text = font_small.render(f"{current_ability_name.upper()}: DMG {stats['damage']} | KB {stats['knockback_multiplier']}x", True, (0, 0, 0))
                win.blit(ability_text, (10, screen_height - 25))
    


    # Current health (green)
    if player_health > 0:
        # Draw dead hearts for max health
        heart_spacing = 3  # Space between hearts
        for i in range(player_max_health):
            x_pos = screen_width - (heart_width + heart_spacing) * (i + 1)
            win.blit(dead_heart, (x_pos, 0))
        # Draw live hearts for current health
        for i in range(player_health):
            x_pos = screen_width - (heart_width + heart_spacing) * (i + 1)
            win.blit(heart, (x_pos, 0))

    if player_health <= 0:
        restart_signal = game_over()
        if restart_signal == "restart":
            # Force difficulty selection on restart
            diff_menu()  # Call difficulty menu directly
            
            # Update difficulty and related variables after menu selection
            current_difficulty = difficulty_settings.get(difficulty, {})
            num_enemies = current_difficulty[0]
            enemy_speed = current_difficulty[1]
            follow_radius = current_difficulty[2]
            enemy_max_health = current_difficulty[3]
            knockback_strength = current_difficulty[4]
            player_max_health = current_difficulty[5]
            
            # Reset all game variables for restart
            player_health = player_max_health


            # Reset player position and camera
            x = screen_width / 2
            y = screen_height / 2
            cam_x = 0
            cam_y = 0

            # Reset abilities and tombs
            abilitys.clear()
            abilitys_picked = 0
            wind_tomb = True
            fire_tomb = True
            earth_tomb = True
            water_tomb = True
            w_attack = None
            f_attack = None
            e_attack = None
            a_attack = None
            
            # Reset enemies with new difficulty settings
            enemies.clear()
            for i in range(num_enemies):
                if i < len(enemy_spawn_points):
                    enemies.append({
                        'x': enemy_spawn_points[i][0],
                        'y': enemy_spawn_points[i][1], 
                        'health': enemy_max_health,
                        'max_health': enemy_max_health,
                        'flash_time': 0,
                        'knockback_x': 0,
                        'knockback_y': 0
                    })
            
            print(f"Game restarted with difficulty: {difficulty}")
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

    # Display wind attack animations
    if w_attack == "left":
        win.blit(player_wind_left, (x - 50, y - 5))
    if w_attack == "right":
        win.blit(pygame.transform.flip(player_wind_left, True, False), (x, y - 5))
    
    # Fire attack animations
    if f_attack == "left":
        win.blit(player_fire_left, (x - 50, y - 5))
    if f_attack == "right":
        win.blit(pygame.transform.flip(player_fire_left, True, False), (x, y - 5))
    
    # Earth attack animations
    if e_attack == "left":
        win.blit(player_earth_left, (x - 90, y - 5))
    if e_attack == "right":
        win.blit(pygame.transform.flip(player_earth_left, True, False), (x - 5, y - 5))
    
    # Water attack animations
    if a_attack == "left":
        win.blit(player_water_left, (x - 60, y - 5))
    if a_attack == "right":
        win.blit(pygame.transform.flip(player_water_left, True, False), (x - 5, y - 5))
    win.blit(death_left, (0,0))
    # update the display
    pygame.display.update()

pygame.quit() # quit the game
exit()