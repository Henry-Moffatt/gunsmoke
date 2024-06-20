from main import *

class Character(Destructible):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon,pos, scrollSpeed,color):
        super().__init__(health, dropChances, dropItems, scrollSpeed)
        self.pos=pygame.Vector2(pos.x, pos.y)
        self.s = speed
        self.d = dmg
        self.f= fireRate
        self.w = weapon
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,20,20)
        self.drawnRect =  self.drawnRect =pygame.draw.rect(window, color, self.rect)
        self.c =color

    def draw(self,window):
        if self.h > 0:
            self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,20,20)
            self.drawnRect = pygame.draw.rect(window, self.c, self.rect)
