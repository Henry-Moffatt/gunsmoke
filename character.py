from destructible import Destructible
import pygame

class Character(Destructible):
    def __init__(self, health, dropChances, dropItems, scrollSpeed, window, player, world, uptime, speed, dmg, fireRate, color, pos):
        super().__init__(health, dropChances, dropItems, scrollSpeed, window, player, world, uptime)
        self.pos=pygame.Vector2(pos.x, pos.y)
        self.s = speed
        self.d = dmg
        self.f= fireRate
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,20,20)
        self.drawnRect =  self.drawnRect =pygame.draw.rect(window, color, self.rect)
        self.c =color
        self.window = window

    def draw(self):
        if self.h > 0:
            self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,20,20)
            self.drawnRect = pygame.draw.rect(self.window, self.c, self.rect)
