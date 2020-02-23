import pygame
from player import Player1

class Game:

    def __init__(self):
        self.player1 = Player1()
        self.pressed = {}