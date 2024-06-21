from character import Character
import random
import pygame
from projectile import Projectile

class Enemy(Character):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, pos, scrollSpeed, color, window, player, world, uptime,):
        super().__init__(health, dropChances, dropItems, scrollSpeed, window, player, world, uptime, speed, dmg, fireRate, color, pos)
        self.randoffsetx = random.randint(-300,300)
        self.randoffsety = random.randint(-300,300)
        self.bullets=[]
        
    def move(self, playerLocation):
        self.uptime +=1
        if self.uptime % 50 == 0:
            self.randoffsetx = random.randint(-200,200)
            self.randoffsety = random.randint(100, 300)
            print("offset was changed")
        if self.h > 0:
            if playerLocation.x-self.randoffsetx > self.pos.x:
                if self.pos.x < self.window.get_width()-20:
                    self.pos.x += self.s
            if playerLocation.x -self.randoffsetx < self.pos.x:
                if self.pos.x >20:
                    self.pos.x -= self.s
            if playerLocation.y-10 - self.randoffsety > self.pos.y:
                if self.pos.y  < self.window.get_height():
                    self.pos.y += self.s
            if playerLocation.y -10 - self.randoffsety < self.pos.y:
                if self.pos.y > 0:
                    self.pos.y -= self.s
            if self.pos.y < self.window.get_height():
                self.pos.y += self.scr
    
    def shoot(self, playerLocation):
        self.uptime +=1
        if self.uptime % 200==0:
            polar = pygame.Vector2((self.pos.x-playerLocation.x),(self.pos.y-playerLocation.y)).as_polar()
            angle = polar[1]
            self.bullets.append(Projectile(1, angle, 5, pygame.Vector2(self.pos.x +10, self.pos.y +10),self.player))
        for i in range(len(self.bullets)):
            if 0 <=i<len(self.bullets):
                self.bullets[-i].moveForEnemy(self.window)



    def takeDamage(self, amount):
        super().takeDamage(amount)
        if self.h ==0:
            self.world.removeEnemy(self)
