import pygame

class Drone:  # nama class
    def __init__(self,screen):
        self.img_drone = pygame.image.load("drone1.png")
        self.x = 0
        self.y = 0
        self.speed = 7
        self.screen = screen
        self.active = True

    def move(self):
        self.x += self.speed
        if self.x<10 or self.x>470:
            self.bounce()

    def bounce(self):
        self.speed *= -1

    def draw(self):
        if self.active:
            self.screen.blit(self.img_drone,(self.x,self.y))

    def spawn(self, x,y):
        self.x = x
        self.y = y
        self.active = True

    def destroy(self):
        self.active = False

    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.img_drone.get_width(),self.img_drone.get_height())