import pygame

class Missile:
    def __init__(self, screen):
        self.img = pygame.image.load('shot.png')
        self.x = 0
        self.y = 0
        self.speed = 20
        self.launched = False
        self.screen = screen

    def launch(self,x,y):
        self.x = x
        self.y = y
        self.launched = True

    def gone(self):
        self.launched = False

    def move(self):
        if self.launched:
            self.y -= self.speed
        if self.y<0:
            self.gone()

    def draw(self):
        self.screen.blit(self.img,(self.x, self.y))