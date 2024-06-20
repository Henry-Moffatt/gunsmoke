from main import *

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
        self.s+=amount
    
    def increaseFireRate(self, amount):
        self.f += amount
    
    def move(self):
        keys =pygame.key.get_pressed()
        speed = self.s
        if keys[pygame.K_UP]:
            if self.pos.y > 30:
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    speed = self.s * math.sqrt(2)/2
                self.pos.y -=speed
        if keys[pygame.K_DOWN]:
            if self.pos.y < window.get_height()-20:
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    speed = self.s * math.sqrt(2)/2
                self.pos.y += speed
        if keys[pygame.K_LEFT]:
            if self.pos.x > 5:
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    speed = self.s * math.sqrt(2)/2
                self.pos.x -=speed
        if keys[pygame.K_RIGHT]:
            if self.pos.x < window.get_width()-20:
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    speed = self.s * math.sqrt(2)/2
                self.pos.x +=speed
        if self.pos.y < window.get_height()-20:
            self.pos.y +=self.scr


    def shoot(self, dt):
        bulletSpeed=7
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            bulletSpeed = 7+self.s
        if keys[pygame.K_DOWN]:
            bulletSpeed = 9-self.s
        if dt % 10 == 0:
            
            if keys[pygame.K_z] and keys[pygame.K_x]==False and keys[pygame.K_c] == False:
                self.bullets.append(Projectile(self.d, -35, bulletSpeed, pygame.Vector2(self.pos.x +4, self.pos.y)))
                self.bullets.append(Projectile(self.d, -25, bulletSpeed, pygame.Vector2(self.pos.x +14, self.pos.y)))
            if keys[pygame.K_x] and keys [pygame.K_c]==False and keys[pygame.K_z] == False:
                self.bullets.append(Projectile(self.d, -5, bulletSpeed, pygame.Vector2(self.pos.x +4, self.pos.y)))
                self.bullets.append(Projectile(self.d, 5, bulletSpeed, pygame.Vector2(self.pos.x +14, self.pos.y)))
            if keys [pygame.K_c] and keys [pygame.K_x]==False and keys[pygame.K_z] == False:
                self.bullets.append(Projectile(self.d, 25, bulletSpeed, pygame.Vector2(self.pos.x +4, self.pos.y)))
                self.bullets.append(Projectile(self.d, 35, bulletSpeed, pygame.Vector2(self.pos.x +14, self.pos.y)))

        for i in range(len(self.bullets)):
            if 0 <=i<len(self.bullets):
                self.bullets[-i].move(window)
                
    def checkDamage(self):
        for i in range(len(world.enemies)):
            if 0 <=i<len(self.bullets):
                for n in range(len(world.enemies[-i].bullets)):
                    if 0 <=n<len(world.enemies[-i].bullets):
                        if self.rect.colliderect(world.enemies[-i].bullets[n]):
                            self.takeDamage(1)
                            world.enemies[-i].bullets.pop()
        if self.h <= 0:
            pygame.quit()

    def removeProjectile(self, itemToRemove):
        self.bullets.remove(itemToRemove)
