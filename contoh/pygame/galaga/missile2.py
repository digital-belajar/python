import pygame
from missile import Missile

class Missile2(Missile):

    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.img.get_width(),self.img.get_height())