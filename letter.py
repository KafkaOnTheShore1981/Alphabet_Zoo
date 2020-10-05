import pygame
import random
from pygame.sprite import Sprite


class Letter(Sprite):

    def __init__(self, az_settings, screen):
        super().__init__()
        self.screen = screen
        self.az_settings = az_settings
        a = random.randint(97, 122)
        c = chr(a)
        self.image = pygame.image.load('images/' + c.upper() + '.png')
        self.ascii = a

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = random.randint(100, self.screen_rect.right - 100)
        self.rect.top = self.screen_rect.top
        self.center = float(self.rect.centerx)

    def update(self):
        if self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.az_settings.letter_speed_factor
