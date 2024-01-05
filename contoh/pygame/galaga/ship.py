import pygame

class Ship:
    def __init__(self,screen):
        self.img_ship = pygame.image.load('ship1.png')
        self.x = 250
        self.y = 450
        self.screen = screen

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def die(self):
        pass

    def draw(self):
        self.screen.blit(self.img_ship,(self.x,self.y))
