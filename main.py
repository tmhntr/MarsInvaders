import pygame
import random
import math 
from pygame import mixer

from foe import Foe

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

#Background resisizing
back_img = pygame.image.load('Assets/marsat4.png')
back_img = pygame.transform.scale(back_img, (800, 600))

#Background music 
mixer.music.load('Assets/music.wav')
mixer.music.play(-1) #plays music in loop

#Bullet
bullet_img = pygame.image.load('Assets/bullet.png')
bullet_img = pygame.transform.rotate(bullet_img, 90)
bullet_img = pygame.transform.scale(bullet_img, (64, 64))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
#Ready - You can't see the bullet on the screen
bullet_state = "ready"
#Fire - The bullet is currently moving

#Score
score = 0
font = pygame.font.Font('Assets/PLANK___.ttf', 32)

textX = 10
textY = 10

def show_score(x, y):
    score_box = font.render("Score: " + str(score), True, (255, 0, 255))
    screen.blit(score_box, (x, y))

def player(x, y):
    screen.blit(player_img, (x, y)) #blit means to draw

# def foe(x, y):
#     screen.blit(foe_img, (x, y)) #blit means to draw

foe_list = []

for i in range(5):
    foe_list.append(Foe())

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x, y + 10))

def isCollision(foeX, foeY, bulletX, bulletY):
    distance = math.sqrt(math.pow(foeX - bulletX, 2) + (math.pow(foeY - bulletY, 2)))
    return (distance < 27)

#Game loop
running = True
speed = 2

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
            #check for fire bullet
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('Assets/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
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

    for foe in foe_list:
        foe.update()

    #Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    for foe in foe_list:
        #Collision
        if isCollision(foe.x, foe.y, bulletX, bulletY):
            explosion_sound = mixer.Sound('Assets/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 1
            foe_list.remove(foe)
            foe_list.append(Foe())
            

    # #Collision
    # if isCollision(foeX, foeY, bulletX, bulletY):
    #     bulletY = 480
    #     bullet_state = "ready"
    #     score += 1
    #     print(score)
    #     foeX_change = 3
    #     foeX = random.randint(0, 735)
    #     foeY = random.randint(50, 150)
    

    player(playerX, playerY)
    show_score(textX, textY)
    for foe in foe_list:
        foe.draw(screen)
    pygame.display.flip()