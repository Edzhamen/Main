import pygame
import random

pygame.init()

# Set up the display
window = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Kruķītie aparāti!!!")

# Load the spaceship image
SPACESHIP = pygame.image.load('OIP.jpg')

# Initialize spaceship position
spaceship_top = 100
spaceship_left = 100

# Initialize movement changes
spaceship_left_change = 0
spaceship_top_change = 0

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # Ensure the script exits completely

        # Keydown events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                spaceship_left = random.randint(0, 400 - 64)
                spaceship_top = random.randint(0, 800 - 64)
            # Movement keys
            if event.key == pygame.K_a:
                spaceship_left_change = -0.3
            elif event.key == pygame.K_d:
                spaceship_left_change = 0.3
            elif event.key == pygame.K_w:
                spaceship_top_change = -0.3
            elif event.key == pygame.K_s:
                spaceship_top_change = 0.3

        # Keyup events
        if event.type == pygame.KEYUP:
            # Stop moving when the key is released
            if event.key in [pygame.K_a, pygame.K_d]:
                spaceship_left_change = 0
            if event.key in [pygame.K_w, pygame.K_s]:
                spaceship_top_change = 0

    # Update spaceship position
    spaceship_top += spaceship_top_change
    spaceship_left += spaceship_left_change

    # Boundary checking
    if spaceship_left < 0 or spaceship_left > 736:
        spaceship_left_change = -spaceship_left_change
    if spaceship_top < 0 or spaceship_top > 736:
        spaceship_top_change = -spaceship_top_change

    # Drawing
    window.fill([0, 0, 0])  # Clear screen
    window.blit(SPACESHIP, [spaceship_left, spaceship_top])  # Draw spaceship

    pygame.display.update()  # Update the display
