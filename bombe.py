import pygame
from datetime import datetime, timedelta

class Bombe(pygame.sprite.Sprite):

    def __init__(self, player1):
        super().__init__()
        self.image = pygame.image.load('img/bomb1.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = player1.rect.x
        self.rect.y = player1.rect.y
        self._time_created = datetime.now()
        self.explosion = 0
    




