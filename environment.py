from main import *

class Environment():
    def __init__(self, scrollSpeed):
        self.scr = scrollSpeed
        self.boxes = []
        self.enemies = []
        self.buildings= []
    
    def instantiateBox():
        pass

    def instantiateBuilding():
        pass

    def spawnEnemy(self, uptime):
        if uptime % random.randint(1, 1000)==0:
            if len(self.enemies) <uptime/1000:
                self.enemies.append(Enemy(1,0,0,3,1,0,0,pygame.Vector2(random.randint(10,390), 10),scrollSpeed,(255,0,0)))

    def healthCheck(self, index):
        if self.enemies[index].h >0:
            return True
        else:
            return False

    def manager(self, playerLocation):
        for i in range(0,len(self.enemies)):
            if 0 <=i<len(self.enemies):
                if self.healthCheck(-i):
                    for n in range(0, len(player.bullets)):
                        if self.enemies[-i].rect.colliderect(player.bullets[n]):
                            self.enemies[-i].takeDamage(player.bullets[n].d)
                            break
                    self.enemies[-i].move(playerLocation)
                    self.enemies[-i].draw(window)
                    self.enemies[-i].shoot(playerLocation)
                else:
                    self.removeEnemy(-i)
                    player.increaseScore(100)

    def removeEnemy(self, enemyToRemove):
        self.enemies.pop(enemyToRemove)
