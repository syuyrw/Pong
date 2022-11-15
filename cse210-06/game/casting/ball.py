import pygame
from random import randint
from game.shared.color import Color
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    #class that represents the ball

    def __init__(self, color, width, height):
        super().__init__

        #set the color and other attributes of the ball

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4,8), randint(-8,8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)