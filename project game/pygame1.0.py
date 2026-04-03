import pygame



pygame.init()


width = 800
height = 600
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("My First Game")


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    screen.fill((30, 30, 30))

    
    pygame.display.update()

pygame.quit()