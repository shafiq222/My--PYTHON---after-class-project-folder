import pygame
import sys

# Start pygame
pygame.init()

# Screen size
width = 800
height = 600

# Create screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Add Elements to My Screen")

# Colors
white = (255, 255, 255)
blue = (0, 100, 255)
red = (255, 60, 60)
black = (0, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 40)

# Text
text = font.render("My Game Screen", True, black)

# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill(white)

    # Rectangle element
    pygame.draw.rect(screen, blue, (200, 150, 400, 200))

    # Another rectangle
    pygame.draw.rect(screen, red, (50, 500, 200, 50))

    # Add text
    screen.blit(text, (250, 50))

    # Update screen
    pygame.display.update()

pygame.quit()
sys.exit()