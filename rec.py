import pygame
import random
pygame.init
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
BLUE = pygame.Color('Blue')
LIGHTBLUE = pygame.Color('LightBlue')
DARKBLUE = pygame.Color('DarkBlue')
YELLOW = pygame.Color('Yellow')
MANGENTA = pygame.Color('Magenta')
ORANGE = pygame.Color('Orange')
WHITE = pygame.Color('White')
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <=0 or self.rect.right >=500:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))   
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))  
        def color_change(self):
            self.image.fill(random.choice[YELLOW,MANGENTA,ORANGE,WHITE])  
        def change_background_color():
                 