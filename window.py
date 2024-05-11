import pygame
import sys

# Initialization
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pysteroid ☄")
clock = pygame.time.Clock()

# Game Loop
running = True

while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate delta time
    delta_time = clock.tick() / 1000

    # Draw the frame
    pygame.display.update()


pygame.quit()
sys.exit(0)


