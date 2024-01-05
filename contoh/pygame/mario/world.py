import pygame 

class World:
    img = None
    pos = 0
    screen = None
    blocks = []

    def __init__(self, screen):
        self.img = pygame.image.load('img/w1-1.png')
        self.screen = screen

    def forward(self): # gerakan world
        self.pos -=10

    def draw(self):
        self.screen.blit(self.img,(self.pos,0))