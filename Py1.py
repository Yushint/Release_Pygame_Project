import pygame
import os
from pygame.sprite import Sprite
from pygame import Surface
from pygame.sprite import Sprite, collide_rect
size = (640, 480)

window = pygame.display.set_mode(size)
screen = pygame.Surface(size) # game window
pygame.display.set_caption('LEVEL 1')
pygame.font.init() 
font = pygame.font.SysFont('Comic Sans', 30)  
text_gate = font.render('Gate -->', True, (255, 0, 0))


# platforms
class Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill((136,69,53))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Player
class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((27,32))
        self.image.fill((65,34,39))
        #self.image = pygame.image.load('Lapras.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.xn = 0
        self.yn = 0
        self.rect.y = y
        self.onGround = False       
            
    def update(self, left, right,  plate):
        if left:
            self.xn = -move_speed
        if right:
            self.xn = move_speed
        if not (left or right):
            self.xn = 0
        if not self.onGround:
            self.yn += gravity
        self.rect.y += self.yn
        self.rect.x += self.xn 
        self.collide(self.xn, 0, plate)
        self.collide(0, self.yn, plate)
        #if self.rect.x == 500 and self.rect.y == 415:
            #os.system('Py2.py')
         
    def collide(self, xn, yn, plate):
        for pl in plate:
            if collide_rect(self, pl):
                #if xvel > 0:
                    #self.rect.right = pl.rect.left
                #if xvel < 0:
                    #self.rect.left = pl.rect.right
                if yn > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                if yn < 0:
                    self.rect.top = pl.rect.bottom
                    self.yn = 0
                    self.onGround = True
                    
                pygame.display.flip()
#make hero
hero = Player(170,55)
left = False
right = False
up = False
down = False
        
level = [
    '---- -----------',
    '-              -',
    '-              -',
    '-------------- -',
    '-              -',
    '- --------------',
    '-              -',
    '-------------- -',
    '-              -',
    '- --------------',
    '-               ',
    '---------------- ',]

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
plate = []


x = 0 
y = 0
for row in level:
    for col in row:
        if col == '-':
            pl = Platform(x,y)
            sprite_group.add(pl)
            plate.append(pl)
        x += 40 # сдвиг на следующую ячейку
    y += 40
    x = 0 # сдвиг на начало новой строки
        
#straws
straw = pygame.Surface((15,15))
straw.fill((255,0,0))


#hero options
move_speed = 7
gravity = 0.4
up = 7
down = 7


# main 
running = True
timer = pygame.time.Clock()
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_2:
                os.system('Py2.py')
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            
                
    screen.fill((66,170,255))
    
    hero.update(left,right, plate)
    sprite_group.draw(screen)
    window.blit(screen,(0,0)) # отображение рабочей поверхности в окне
    window.blit(text_gate,(500,415))
    pygame.display.flip()
    timer.tick(40)