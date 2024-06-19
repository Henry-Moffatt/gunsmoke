import pygame
import random
from pygame.locals import *
import time

class Destructible:
    def __init__(self,health,dropChances,dropItems):
        self.h= health
        self.dC=dropChances
        self.dI=dropItems
    
    def takeDamage(self, amount):
        self.h -= amount

    def drop(self):
        pass

class Box(Destructible):
    def __init__(self, health, dropChances, dropItems):
        super().__init__(health, dropChances, dropItems)

class Character(Destructible):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon):
        super().__init__(health, dropChances, dropItems)
        self.s = speed
        self.d = dmg
        self.f= fireRate
        self.w = weapon
        self.rect = pygame.rect.Rect(200, 225, 20, 20)
        self.drawnRect =pygame.draw.rect(window, (0,255,0), self.rect)

    def shoot(self, angle):
        pass

    def move(self, x, y):
        self.rect.move_ip(x,y)
        self.drawnRect
        self.drawnRect=pygame.draw.rect(window, (0,255,0), self.rect)
        


class Player(Character):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon, score, controls):
        super().__init__(health, dropChances, dropItems, speed, dmg, fireRate, weapon)
        self.sc=score
        self.cont =controls
    
    def instantiatePlayer(self):
        pass

    def increaseScore(self, amount):
        self.sc += amount

    def increaseHealth(self, amount):
        self.h += amount
    
    def increaseSpeed(self, amount):
        self.s+=amount
    
    def increaseFireRate(self, amount):
        self.f += amount

class Enemy(Character):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon):
        super().__init__(health, dropChances, dropItems, speed, dmg, fireRate, weapon)
        

    def trackPlayer():
        pass

class BuildingEnemy(Enemy):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon):
        super().__init__(health, dropChances, dropItems, speed, dmg, fireRate, weapon)

class Projectile():
    def __init__(self, dmg, angle, speed):
        self.d = dmg
        self.a = angle
        self.s = speed

class Environment():
    def __init__(self, scrollSpeed):
        self.scr = scrollSpeed

    def scroll(self):
        pass

    def instantiateBox():
        pass

    def instantiateBuilding():
        pass

pygame.init()
window = pygame.display.set_mode((400,550))
window.fill((0,0,0))
running = True

player = Player(0,0,10,10, 10, "none", 0,0, controls=["w","a"])
while running:
    time.sleep(0.01)
    player.move(1,1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
