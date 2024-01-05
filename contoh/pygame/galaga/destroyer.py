import pygame
from drone import Drone

class Destroyer(Drone):
    def __init__(self,screen):
        Drone.__init__(self,screen)
        self.img_drone = pygame.image.load("destroyer.png")