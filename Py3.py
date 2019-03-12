import pygame
import os
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('ENDING')
pygame.font.init() 
font = pygame.font.SysFont('Comic Sans', 55)  
text = font.render('You Win', True, (255, 0, 0))
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(text,(250,200))
    pygame.display.flip()