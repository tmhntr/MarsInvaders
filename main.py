import pygame
from pygame.locals import *
#initilze the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Mars Invaders")
icon = pygame.image.load('Assets/mars-2.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('Assets/spaceship.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY)) #blit means to draw

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                playerX += 40
            if event.key == pygame.K_LEFT:
                playerX -= 40
            if event.key == pygame.K_UP:
                playerY -= 40
            if event.key == pygame.K_DOWN:
                playerY += 40

    #RGB - Red, Green, Blue
    screen.fill((75, 32, 16))

    player()
    pygame.display.flip()