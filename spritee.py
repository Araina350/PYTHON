import pygame
import random
SW,SH = 500,400
MS = 5
FS = 72
pygame.init()
back_i = pygame.transform.scale(pygame.image.load("/Users/aishwaryaagarwal/Desktop/PYTHON/HD-wallpaper-mario-stage-new-nintendo-world (1).jpg")(SW,SH))
Fo = pygame.font.SysFont("ALGERIAN",FS)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.color("Dodgerblue"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect
    def move(self,x_change,y_change):
        self.rect.x = max(min(self.rect.x + x_change, SW - self.rect.width),0)
        self.rect.y = max(min(self.rect.y + y_change, SH - self.rect.height),0)
        