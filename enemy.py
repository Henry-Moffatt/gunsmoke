from main import *

class Enemy(Character):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon, pos, scrollSpeed,color):
        super().__init__(health, dropChances, dropItems, speed, dmg, fireRate, weapon, pos, scrollSpeed,color)
        self.randoffsetx = random.randint(-300,300)
        self.randoffsety = random.randint(-300,300)
        self.bullets=[]
        
    def move(self, playerLocation):
        
        if uptime % 50 == 0:
            self.randoffsetx = random.randint(-200,200)
            self.randoffsety = random.randint(100, 300)
        if self.h > 0:
            if playerLocation.x-self.randoffsetx > self.pos.x:
                if self.pos.x < window.get_width()-20:
                    self.pos.x += self.s
            if playerLocation.x -self.randoffsetx < self.pos.x:
                if self.pos.x >20:
                    self.pos.x -= self.s
            if playerLocation.y-10 - self.randoffsety > self.pos.y:
                if self.pos.y  < window.get_height():
                    self.pos.y += self.s
            if playerLocation.y -10 - self.randoffsety < self.pos.y:
                if self.pos.y > 0:
                    self.pos.y -= self.s
            if self.pos.y < window.get_height():
                self.pos.y += scrollSpeed
    
    def shoot(self, playerLocation):
        if uptime % 200==0:
            polar = pygame.Vector2((self.pos.x-playerLocation.x),(self.pos.y-playerLocation.y)).as_polar()
            angle = polar[1]
            self.bullets.append(Projectile(1, angle, 5, pygame.Vector2(self.pos.x +10, self.pos.y +10)))
        for i in range(len(self.bullets)):
            if 0 <=i<len(self.bullets):
                self.bullets[-i].moveForEnemy(window)



    def takeDamage(self, amount):
        super().takeDamage(amount)
        if self.h ==0:
            world.removeEnemy(self)
