import pygame
import random
from pygame.locals import *

class Foe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Assets/alien-2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#initilze the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Mars Invaders")
icon = pygame.image.load('Assets/mars-2.png')
pygame.display.set_icon(icon)

#Player
player_img = pygame.image.load('Assets/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

#Foe
foe_img = pygame.image.load('Assets/alien-2.png')
foeX = random.randint(0, 800)
foeY = random.randint(50, 150)
foeX_change = 0.3
foeY_change = 10

#Background resisizing
back_img = pygame.image.load('Assets/marsat4.png')
back_img = pygame.transform.scale(back_img, (800, 600))

def player(x, y):
    screen.blit(player_img, (x, y)) #blit means to draw

def foe(x, y):
    screen.blit(foe_img, (x, y)) #blit means to draw

#Game loop
running = True
speed = 5
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                playerX_change = speed
            if event.key == pygame.K_LEFT:
                playerX_change = -speed
            if event.key == pygame.K_UP:
                playerY_change = -speed
            if event.key == pygame.K_DOWN:
                playerY_change = speed
        if event.type == pygame.KEYUP:
            #keystroke has been released
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    #RGB - Red, Green, Blue
    screen.fill((75, 32, 16))

    #Draw background
    screen.blit(back_img, (0, 0))

    #5 = 5 + -0.1 -> 5 = 5 - 0.1
    #5 = 5 + 0.1

    #checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: #subtracting 64 from 800
        playerX = 736

    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536: #subtracting 64 from 600
        playerY = 536

    # foe movement and boundaries
    foeX += foeX_change
    
    if foeX <= 0:
        foeX_change = 5
        foeY += foeY_change
    elif foeX >= 736: #subtracting 64 from 800
        foeX_change = -5
        foeY += foeY_change
    

    player(playerX, playerY)
    foe(foeX, foeY)
    pygame.display.flip()