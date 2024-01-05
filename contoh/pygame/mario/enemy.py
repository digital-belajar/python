import pygame

class Enemy:
    rect = pygame.Rect(0,0,0,0)
    img = []
    img_index = 0
    screen = None

    def __init__(self,screen,x,y):
        self.rect = pygame.Rect(0,0,0,0)
        self.rect.x = x
        self.rect.y = y
        self.rect.width = 32
        self.rect.height = 32
        self.screen = screen
        self.img = [pygame.image.load('img/gomba1.png'),
                    pygame.image.load('img/gomba2.png')]

    def move(self):  # gerakan enemy
        self.rect.x -= 5

    def draw(self):  # gambar enemy
        self.screen.blit(self.img[self.img_index],self.rect)
        self.img_index = 1 if self.img_index == 0 else 0
            
    def hit(self, charrect):
        return self.rect.colliderect(charrect)