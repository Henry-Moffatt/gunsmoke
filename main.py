import pygame
import random
from pygame.locals import *
import math

drawnRect = 0

class Destructible:
    def __init__(self,health,dropChances,dropItems, scrollSpeed):
        self.h= health
        self.dC=dropChances
        self.dI=dropItems
        self.scr=scrollSpeed
    
    def takeDamage(self, amount):
        self.h -= amount

    def drop(self):
        dice = random.random()
        if dice <=self.dC[3]:
            return 4
        elif self.dC[3] < dice <= self.dC[2]:
            return 3
        elif self.dC[2] < dice <= self.dC[1]:
            return 2
        elif self.dC[1] < dice <= self.dC[0]:
            return 1
        else:
            return False

class Box(Destructible):
    def __init__(self, health, dropChances, dropItems):
        super().__init__(health, dropChances, dropItems)

class Character(Destructible):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon,pos, scrollSpeed,color):
        super().__init__(health, dropChances, dropItems, scrollSpeed)
        self.pos=pygame.Vector2(pos.x, pos.y)
        self.speed = speed
        self.d = dmg
        self.fire= fireRate
        self.w = weapon
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,20,20)
        self.drawnRect =  self.drawnRect =pygame.draw.rect(window, color, self.rect)
        self.c =color

    def draw(self,window):
        if self.h > 0:
            self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,20,20)
            self.drawnRect = pygame.draw.rect(window, self.c, self.rect)

        


class Player(Character):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon, pos, score, controls, scrollSpeed,color):
        super().__init__(health, dropChances, dropItems, speed, dmg, fireRate, weapon, pos, scrollSpeed,color)
        self.sc=score
        self.cont =controls
        self.bullets = []

    def increaseScore(self, amount):
        self.sc += amount

    def increaseHealth(self, amount):
        self.h += amount
    
    def increaseSpeed(self, amount):
        self.speed+=amount
    
    def increaseFireRate(self, amount):
        self.fire += amount
    
    def move(self):
        keys =pygame.key.get_pressed()
        speed = self.speed
        if keys[pygame.K_UP]:
            if self.pos.y > 5:
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    speed = self.speed * math.sqrt(2)/2
                self.pos.y -=speed
        if keys[pygame.K_DOWN]:
            if self.pos.y < window.get_height()-20:
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    speed = self.speed * math.sqrt(2)/2
                self.pos.y += speed
        if keys[pygame.K_LEFT]:
            if self.pos.x > 5:
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    speed = self.speed * math.sqrt(2)/2
                self.pos.x -=speed
        if keys[pygame.K_RIGHT]:
            if self.pos.x < window.get_width()-20:
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    speed = self.speed * math.sqrt(2)/2
                self.pos.x +=speed
        if self.pos.y < window.get_height()-20:
            self.pos.y +=self.scr

    def shoot(self, dt):
    
        keys = pygame.key.get_pressed()
        if dt % 10/self.fire == 0:
            if keys[pygame.K_z] and keys[pygame.K_x]==False and keys[pygame.K_c] == False:
                self.bullets.append(Projectile(self.d, -35, 5, pygame.Vector2(self.pos.x +4, self.pos.y)))
                self.bullets.append(Projectile(self.d, -25, 5, pygame.Vector2(self.pos.x +14, self.pos.y)))
            if keys[pygame.K_x] and keys [pygame.K_c]==False and keys[pygame.K_z] == False:
                self.bullets.append(Projectile(self.d, -5, 5, pygame.Vector2(self.pos.x +4, self.pos.y)))
                self.bullets.append(Projectile(self.d, 5, 5, pygame.Vector2(self.pos.x +14, self.pos.y)))
            if keys [pygame.K_c] and keys [pygame.K_x]==False and keys[pygame.K_z] == False:
                self.bullets.append(Projectile(self.d, 25, 5, pygame.Vector2(self.pos.x +4, self.pos.y)))
                self.bullets.append(Projectile(self.d, 35, 5, pygame.Vector2(self.pos.x +14, self.pos.y)))

        for i in range(len(self.bullets)):
            self.bullets[-i].move(window)
                
    def checkDamage(self):
        for i in range(len(world.enemies)):
            for n in range(len(world.enemies[i].bullets)):
                if self.rect.colliderect(world.enemies[i].bullets[n]):
                    self.takeDamage(1)
                    world.enemies[i].bullets.pop(n)
        if self.h <= 0:
            pygame.quit()

                
    
    def removeProjectile(self, itemToRemove):
        self.bullets.remove(itemToRemove)
            
                    

class Enemy(Character):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon, pos, scrollSpeed,color):
        super().__init__(health, dropChances, dropItems, speed, dmg, fireRate, weapon, pos, scrollSpeed,color)
        self.randoffsetx = random.randint(-300,300)
        self.randoffsety = random.randint(-300,300)
        self.bullets=[]
        
    def move(self, playerLocation):
        
        if uptime % 50 == 0:
            self.randoffsetx = random.randint(-200,200)
            self.randoffsety = random.randint(50, 150)
        if self.h > 0:
            if playerLocation.x-self.randoffsetx > self.pos.x:
                if self.pos.x < window.get_width()-20:
                    self.pos.x += self.speed
            if playerLocation.x -self.randoffsetx < self.pos.x:
                if self.pos.x >20:
                    self.pos.x -= self.speed
            if playerLocation.y-self.randoffsety > self.pos.y:
                if self.pos.y < window.get_height()+100:
                    self.pos.y += self.speed
            if playerLocation.y-self.randoffsety < self.pos.y:
                if self.pos.y > 20:
                    self.pos.y -= self.speed
    
    def shoot(self, playerLocation):
        if uptime % 200==0:
            
            angle = math.degrees(math.atan((playerLocation.y-self.pos.y)/(playerLocation.x-self.pos.x)))
            self.bullets.append(Projectile(1, angle, 5, pygame.Vector2(self.pos.x +10, self.pos.y +10)))
        for i in range(len(self.bullets)):
            self.bullets[-i].moveForEnemy(window)



    def takeDamage(self, amount):
        super().takeDamage(amount)
        if self.h ==0:
            world.removeEnemy(self)

class BuildingEnemy(Enemy):
    def __init__(self, health, dropChances, dropItems, speed, dmg, fireRate, weapon):
        super().__init__(health, dropChances, dropItems, speed, dmg, fireRate, weapon)

class Projectile():
    def __init__(self, dmg, angle, speed, pos):
        self.d = dmg
        self.a = angle
        self.speed= speed
        self.pos=pygame.Vector2(pos.x, pos.y)
        self.rect =  pygame.rect.Rect(self.pos.x, self.pos.y,2,2)
        self.ut = 0

    def move(self, window):
        if self.drawCheck():
            self.pos.x += self.speed* math.sin(math.radians(self.a))
            self.pos.y -= self.speed* math.cos(math.radians(self.a))
            self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,2,2)
            self.drawnRect = pygame.draw.rect(window, (255,255,255), self.rect)
            self.ut +=1
        else:

            player.removeProjectile(self)
    
    def moveForEnemy(self,window):
        if self.a < 0:
            self.pos.x -= self.speed* math.cos(math.radians(self.a))
        else:
            self.pos.x += self.speed* math.cos(math.radians(self.a))
        self.pos.y -= self.speed* -abs(math.sin(math.radians(self.a)))
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,2,2)
        self.drawnRect = pygame.draw.rect(window, (255,255,255), self.rect)
        self.ut +=1
    
    def drawCheck(self,):
        if self.pos.y > 0 and self.ut <=25:
            return True
        else:
            return False
            


class Environment():
    def __init__(self, scrollSpeed):
        self.scr = scrollSpeed
        self.boxes = []
        self.enemies = []
        self.buildings= []
        self.powerups =[]
    
    def instantiateBox():
        pass

    def instantiateBuilding():
        pass

    def spawnEnemy(self, uptime):
        if uptime % random.randint(1, 1000)==0:
            if len(self.enemies) <uptime/1000:
                self.enemies.append(Enemy(1,[0.4, 0.25, 0.15, 0.1],[4, 3, 2, 1],2,1,0,0,pygame.Vector2(random.randint(10,390), 10),scrollSpeed,(255,0,0)))

    def healthCheck(self, index):
        if self.enemies[index].h >0:
            return True
        else:
            return False

    def manager(self, playerLocation):
        for i in range(0,len(self.enemies)):
            if self.healthCheck(-i):
                for n in range(0, len(player.bullets)):
                    if self.enemies[-i].rect.colliderect(player.bullets[n]):
                        self.enemies[-i].takeDamage(player.bullets[n].d)
                        break
                self.enemies[-i].move(playerLocation)
                self.enemies[-i].draw(window)
                self.enemies[-i].shoot(playerLocation)
            else:
                x=self.enemies[-i].drop()
                if x != False:
                    self.powerups.append(powerUp(x, self.enemies[-i].pos))
                self.removeEnemy(-i)
                player.increaseScore(100)
        for i in range(0, len(self.powerups)):
            self.powerups[i].drawAndCheck()

    def removeEnemy(self, enemyToRemove):
        self.enemies.pop(enemyToRemove)

class powerUp():
    def __init__(self, type, pos) -> None:
        self.t=type
        self.pos = pygame.Vector2(pos.x, pos.y)
        self.rect = pygame.rect.Rect(self.pos.x,self.pos.y,10,10)
        self.collected = False

    def drawAndCheck(self):
        if self.collected == False:
            self.drawnRect = pygame.draw.rect(window,(255,255,0),self.rect)
        
            if self.rect.colliderect(player): 
                print("collision detected")
                print(self.t)
                if self.t == 4:
                    player.increaseScore(1000)
                    self.collected = True
                elif self.t == 3:
                    player.increaseSpeed(2)
                    self.collected = True
                elif self.t == 2:
                    player.increaseFireRate(2)
                    self.collected = True
                elif self.t == 1:
                    player.increaseHealth(1)
                    self.collected = True
        
            
        

pygame.init()
window = pygame.display.set_mode((400,550))
window.fill((0,0,0))
running = True
clock = pygame.time.Clock()
uptime =0

position = pygame.Vector2(window.get_width()/2, window.get_height()/2)
pos2=position = pygame.Vector2(window.get_width()/2, window.get_height()/2)
scrollSpeed = 2
player = Player(3,0,0,5,10,10,"none",position,0,0, scrollSpeed,(0,255,0))
uptime =0
world = Environment(scrollSpeed)
font = pygame.font.SysFont("Papyrus", 21)

while running:
        text = font.render(f"Health: {player.h}", False, (200, 200, 200))
        text2 = font.render(f"Score: {player.sc}", False, (200, 200, 200))
        text3 = font.render(f"Speed: {player.speed}", False, (200, 200, 200))
        text4 = font.render(f"Firerate: {player.fire}", False, (200, 200, 200))
        dt =clock.tick(60)
        uptime +=1
        window.fill((0,0,0))
        player.draw(window)
        world.spawnEnemy(uptime)
        world.manager(player.pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.move()
        player.shoot(uptime)
        player.checkDamage()
        window.blit(text, pygame.Vector2(75,0))
        window.blit(text2, pygame.Vector2(250,0))
        window.blit(text3, position)
        window.blit(text4,pygame.Vector2(25, 20))
        pygame.display.flip()
