import pygame
from bombe import Bombe

class Player1(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 1
        self.all_bombe = pygame.sprite.Group()
        self.image = pygame.image.load('img/p_1_down.png')
        self.rect = self.image.get_rect()
        self.rect.x = 29
        self.rect.y = 58

    def put_bombe(self):
        self.all_bombe.add(Bombe(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
    
    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity