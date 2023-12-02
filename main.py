import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
yarni = pygame.image.load("images/yarni.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  
    screen.blit(yarni, (0, 0)) 

    pygame.display.flip()  

pygame.quit()