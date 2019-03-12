import pygame
import os
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.mixer.init()
pygame.mixer.music.load("file.mp3")
pygame.mixer.music.play(0)
pygame.font.init() 
font = pygame.font.SysFont('Comic Sans', 55)  
text = font.render('IG PRODUCTION', True, (255, 0, 0))
text2 = font.render('Press S to Start', True, (255, 0, 0))
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                os.system("Py1.py")
            if event.key == pygame.K_p:
                pygame.mixer.music.pause()
    screen.blit(text,(200,200))
    screen.blit(text2,(200,300))
    pygame.display.flip()