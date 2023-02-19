import pygame
import random

class Foe:
    def __init__(self, image_filename = "Assets/alien-2.png"):
        self.img = pygame.image.load(image_filename)
        self.x = random.randint(0, 735)
        self.y = random.randint(50, 150)
        self.x_change = 3
        self.y_change = 10

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def update(self):
        speed_increase = 0.3
        # foe movement and boundaries
        self.x += self.x_change
        
        if self.x <= 0:
            self.x_change = abs(self.x_change) + speed_increase
            self.y += self.y_change
        elif self.x >= 736: #subtracting 64 from 800
            self.x_change = -abs(self.x_change) - speed_increase
            self.y += self.y_change

