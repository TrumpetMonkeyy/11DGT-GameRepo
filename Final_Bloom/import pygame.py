import pygame
import os
import math
import random  # Added missing import

#width and height for the sprite
sprite_width = 28
sprite_height = 44

# --- Define missing variables ---
screen_width = 800
screen_height = 600

# Initialize pygame and create a screen
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

# Create a dummy player sprite for demonstration
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((sprite_width, sprite_height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)

player = Player()

# Create all_sprites group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

print(Player)
# --- Enemy Class ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, player_ref):
        super().__init__()
        # Store a reference to the player. This is crucial for tracking.
        self.player = player_ref

        # Create a simple enemy image (red square for now)
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()

        # Set spawn position
        self.rect.x = x
        self.rect.y = y

        self.speed = random.uniform(30, 60)  # pixels per second
        self.health = 100

    def update(self, dt):
        # --- Movement Logic ---
        # Calculate the vector from the enemy to the player
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery
        
        # Calculate the distance to the player
        distance = math.sqrt(dx**2 + dy**2)

        # Only move if enemy is close enough to player (within 200 pixels)
        if distance > 0 and distance < 200:
            # Normalize the vector (make its length 1)
            dx /= distance
            dy /= distance

            # Move the enemy along the normalized vector
            self.rect.x += dx * self.speed * dt
            self.rect.y += dy * self.speed * dt

# --- Enemy Spawn Locations ---
enemy_spawn_locations = [
    (100, 100),   # Top-left area
    (700, 100),   # Top-right area
    (100, 500),   # Bottom-left area
    (700, 500),   # Bottom-right area
    (400, 50),    # Top-center
    (400, 550),   # Bottom-center
    (50, 300),    # Left-center
    (750, 300),   # Right-center
]

# --- Create Enemies at Specific Locations ---
enemy_list = pygame.sprite.Group()
for i, (x, y) in enumerate(enemy_spawn_locations):
    enemy = Enemy(x, y, player)  # Pass spawn coordinates and player object
    enemy_list.add(enemy)
    all_sprites.add(enemy)

# --- Game Loop Example ---
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60) / 1000.0  # Delta time in seconds
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update all sprites
    all_sprites.update(dt)
    
    # --- Collision Detection ---
    # Check if the player has collided with any enemy
    collided_enemies = pygame.sprite.spritecollide(player, enemy_list, False)
    if collided_enemies:
        # Simple collision response: print a message
        print("Player collided with an enemy!")
    
    # Clear screen
    screen.fill((0, 0, 0))
    
    # Draw all sprites
    all_sprites.draw(screen)
    
    # Update display
    pygame.display.flip()

pygame.quit()