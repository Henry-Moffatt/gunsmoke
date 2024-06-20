from main import *

class Projectile():
    def __init__(self, dmg, angle, speed, pos):
        self.d = dmg
        self.a = angle
        self.s = speed
        self.pos=pygame.Vector2(pos.x, pos.y)
        self.rect =  pygame.rect.Rect(self.pos.x, self.pos.y,2,2)
        self.ut = 0
        self.utLim = 100/self.s

    def move(self, window):
        if self.drawCheck(self.utLim):
            self.pos.x += self.s * math.sin(math.radians(self.a))
            self.pos.y -= self.s * math.cos(math.radians(self.a))
            self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,2,2)
            self.drawnRect = pygame.draw.rect(window, (255,255,255), self.rect)
            self.ut +=1
        else:
            player.removeProjectile(self)
    
    def moveForEnemy(self,window):
        if self.drawCheck(300):
            self.pos.x -= self.s * math.cos(math.radians(self.a))
            self.pos.y -= self.s * math.sin(math.radians(self.a))
            self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,2,2)
            self.drawnRect = pygame.draw.rect(window, (255,255,255), self.rect)
            self.ut +=1
    
    def drawCheck(self, utLim):
        if  self.ut <= utLim:
            return True
        else:
            return False