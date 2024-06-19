import pygame
import random
from pygame.locals import *
import time

drawnRect = 0

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
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon,pos):
        super().__init__(health, dropChances, dropItems)
        self.pos=pos
        self.s = speed
        self.d = dmg
        self.f= fireRate
        self.w = weapon
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,20,20)
        drawnRect =  self.drawnRect =pygame.draw.rect(window, (0,255,0), self.rect)
        

    def shoot(self, angle):
        pass

    def move(self, x, y):
        if x <0:
            self.pos.x -= self.s
        elif x > 0:
            self.pos.x += self.s
        if y < 0:
            self.pos.y -= self.s
        elif y > 0:
            self.pos.y += self.s

    def draw(self,window):
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,20,20)
        window.fill((0,0,0))
        drawnRect = pygame.draw.rect(window, (0,255,0), self.rect)

        


class Player(Character):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon, pos, score, controls):
        super().__init__(health, dropChances, dropItems, speed, dmg, fireRate, weapon, pos)
        self.sc=score
        self.cont =controls

    def increaseScore(self, amount):
        self.sc += amount

    def increaseHealth(self, amount):
        self.h += amount
    
    def increaseSpeed(self, amount):
        self.s+=amount
    
    def increaseFireRate(self, amount):
        self.f += amount
    
    def move(self):
        keys =pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.pos.y > 5:
                self.pos.y -=self.s
        if keys[pygame.K_DOWN]:
            if self.pos.y < window.get_height()-20:
                self.pos.y += self.s
        if keys[pygame.K_LEFT]:
            if self.pos.x > 5:
                self.pos.x -=self.s
        if keys[pygame.K_RIGHT]:
            if self.pos.x < window.get_width()-20:
                self.pos.x +=self.s
        

class Enemy(Character):
    def __innit__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon):
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
clock = pygame.time.Clock()
position = pygame.Vector2(window.get_width()/2, window.get_height()/2)
player = Player(3,0,0,10,10,10,"none",position,10,0)
while running:
        player.draw(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.move()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
