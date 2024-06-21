import random
from enemy import Enemy
import pygame

class Environment():
    def __init__(self, scrollSpeed, player, wind, world, uptime):
        self.scr = scrollSpeed
        self.player=player
        self.window= wind
        self.boxes = []
        self.enemies = []
        self.buildings= []
        self.world = self
        self.uptime = uptime
    
    def instantiateBox():
        pass

    def instantiateBuilding():
        pass

    def spawnEnemy(self, uptime):
        if uptime % random.randint(1, 1000)==0:
            if len(self.enemies) <uptime/1000:
                self.enemies.append(Enemy(1, 0,0, 4, 1, 1, pygame.Vector2(random.randint(10,390), 10), self.scr, (255,0,0), self.window,self.player,self.world, self.uptime))

    def healthCheck(self, index):
        if self.enemies[index].h >0:
            return True
        else:
            return False

    def manager(self, playerLocation):
        for i in range(0,len(self.enemies)):
            if 0 <=i<len(self.enemies):
                if self.healthCheck(-i):
                    for n in range(0, len(self.player.bullets)):
                        if self.enemies[-i].rect.colliderect(self.player.bullets[n]):
                            self.enemies[-i].takeDamage(self.player.bullets[n].d)
                            break
                    self.enemies[-i].move(playerLocation)
                    self.enemies[-i].draw()
                    self.enemies[-i].shoot(playerLocation)
                else:
                    self.removeEnemy(-i)
                    self.player.increaseScore(100)

    def removeEnemy(self, enemyToRemove):
        self.enemies.pop(enemyToRemove)
