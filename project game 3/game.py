import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangle Edge Color Game")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Triangle settings
x = 400
y = 300
size = 40
color = WHITE
speed = 5

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movement
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Edge detection and color change
    if y <= 0:
        y = 0
        color = BLUE

    if y >= HEIGHT - size:
        y = HEIGHT - size
        color = GREEN

    if x <= 0:
        x = 0
        color = WHITE

    if x >= WIDTH - size:
        x = WIDTH - size
        color = RED

    # Background
    screen.fill(BLACK)

    # Draw triangle
    points = [
        (x, y),
        (x + size, y),
        (x + size / 2, y - size)
    ]
    pygame.draw.polygon(screen, color, points)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()