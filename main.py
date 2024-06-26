#Define the code to be run
def main():
    import pygame
    import random
    import math

    #All classes with a health attribute inherit from here
    class Destructible:
        def __init__(self,health, scrollSpeed):
            self.h= health
            self.scr=scrollSpeed
        
        def takeDamage(self, amount):
            self.h -= amount

        #Chooses whether a powerup will be dropped, and what type
        def drop(self):
            dice = random.random()
            if dice <=0.1:
                return 2
            elif 0.1 < dice <= 0.4:
                return 1
            else:
                return False

    #Class for the crates
    class Box(Destructible):
        def __init__(self, health ,scrollSpeed, pos):
            super().__init__(health , scrollSpeed)
            self.position = pygame.Vector2(pos.x,pos.y)
            self.rect=pygame.rect.Rect(self.position.x,self.position.y,25,25)
            self.color = (0,0, self.h * 255/7)
            self.drawnRect =pygame.draw.rect(window, self.color, self.rect)
            self.live=True
            self.dropped = False
            self.touched=[]
        
        #moves the crate along the screen in time with the scroll speed
        def move(self):
            if self.live:
                self.position.y += self.scr
        
        #any function with "draw" in the title simply draws the object in question to the window
        #It does not inherit since each draw function is different for each classes' individual needs
        def draw(self):
            if self.live:
                self.rect=pygame.rect.Rect(self.position.x,self.position.y,25,25)        
                self.drawnRect  =pygame.draw.rect(window, self.color, self.rect)
        
        #Checks for and deals damage to the box
        def checkDamage(self):
            for n in range(0, len(player.bullets)):
                if self.rect.colliderect(player.bullets[n]):
                    if self.h > 1:
                        if  player.bullets[n] not in self.touched:
                            self.takeDamage(1)
                            self.color = (0,1/(self.h * 7/255), self.h * 255/7)
                            self.touched.append(player.bullets[n])
                    else:
                        x= super().drop()
                        if x!= False:
                            if self.dropped== False:
                                world.powerups.append(powerUp(x,self.position))
                                self.dropped = True
                            
                        self.live = False
                    
                        
            if self.dropped:
                dt = 0
                if dt >1:
                    world.boxes.remove(self)
                else:
                    dt +=1           

    #class for the characters. Players and enemies inherit this
    class Character(Destructible):
        def __init__(self, health , speed, dmg,pos, scrollSpeed,color):
            super().__init__(health , scrollSpeed)
            self.pos=pygame.Vector2(pos.x, pos.y)
            self.speed = speed
            self.d = dmg
            self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,20,20)
            self.drawnRect =  self.drawnRect =pygame.draw.rect(window, color, self.rect)
            self.c =color

        def draw(self,window):
            if self.h > 0:
                self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,20,20)
                self.drawnRect = pygame.draw.rect(window, self.c, self.rect)
                #The following print statement was a part of the white box testing for this function
                #print("Character was drawn")

            

    #Class for the player. This class was unique and required the implimentation of some polymorphism to differentiate it from enemies and boxes
    class Player(Character):
        def __init__(self, health, speed, dmg, pos, score, scrollSpeed,color):
            super().__init__(health, speed, dmg, pos, scrollSpeed,color)
            self.sc=score
            self.bullets = []

        #The following methods increase a certain attribute, depending on the function
        def increaseScore(self, amount):
            self.sc += amount

        def increaseHealth(self, amount):
            self.h += amount
        
        #Takes player input and moves player
        def move(self):
            keys =pygame.key.get_pressed()
            speed = self.speed
            if keys[pygame.K_UP]:
                if self.pos.y > 0:
                    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        speed = self.speed * math.sqrt(2)/2
                    self.pos.y -=speed
            if keys[pygame.K_DOWN]:
                if self.pos.y < window.get_height()-20:
                    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        speed = self.speed * math.sqrt(2)/2
                    self.pos.y += speed
            if keys[pygame.K_LEFT]:
                if self.pos.x > 80:
                    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        speed = self.speed * math.sqrt(2)/2
                    self.pos.x -=speed
            if keys[pygame.K_RIGHT]:
                if self.pos.x < window.get_width()-100:
                    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        speed = self.speed * math.sqrt(2)/2
                    self.pos.x +=speed
            if self.pos.y < window.get_height()-20:
                self.pos.y +=self.scr
        
        #Takes player input and shoots from player
        def shoot(self, dt):
        
            keys = pygame.key.get_pressed()
            if dt % 10 == 0:
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
                if 0 <= i < len(self.bullets):
                    self.bullets[-i].move(window)
                    
        def checkDamage(self):
            for i in range(len(world.enemies)):
                if 0 <=i < len(world.enemies):
                    for n in range(len(world.enemies[-i].bullets)):
                        if 0 <=n < len(world.enemies[-i].bullets):
                            if self.rect.colliderect(world.enemies[-i].bullets[-n]):
                                self.takeDamage(world.enemies[-i].bullets[-n].d)
                                world.enemies[-i].bullets.pop(-n)
            if self.h <= 0:
                pygame.quit()

        def removeProjectile(self, itemToRemove):
            self.bullets.remove(itemToRemove)

    #Enemy class. Kamikaze enemy inherits from this            
    class Enemy(Character):
        def __init__(self, health,speed, dmg, pos, scrollSpeed,color):
            super().__init__(health, speed, dmg, pos, scrollSpeed,color)
            self.randoffsetx = random.randint(-300,300)
            self.randoffsety = random.randint(-300,300)
            self.bullets=[]
        
        #Move and shoot required a different polymorphic function as enemies and players move different ways
        def move(self, playerLocation):
            
            if uptime % 50 == 0:
                self.randoffsetx = random.randint(-200,200)
                self.randoffsety = random.randint(50, 150)
            if self.h > 0:
                if playerLocation.x-self.randoffsetx > self.pos.x:
                    if self.pos.x < window.get_width()-100:
                        self.pos.x += self.speed
                if playerLocation.x -self.randoffsetx < self.pos.x:
                    if self.pos.x >80:
                        self.pos.x -= self.speed
                if playerLocation.y-self.randoffsety > self.pos.y:
                    if self.pos.y < window.get_height():
                        self.pos.y += self.speed
                if playerLocation.y-self.randoffsety < self.pos.y:
                    if self.pos.y > 20:
                        self.pos.y -= self.speed
        
        def shoot(self, playerLocation):
            if uptime % 150+ random.randint(-20,20)==0:
                if self.pos.y <= playerLocation.y:
                    angle = math.degrees(math.atan((playerLocation.y-self.pos.y)/(playerLocation.x-self.pos.x)))
                    self.bullets.append(Projectile(1, angle, 5, pygame.Vector2(self.pos.x +10, self.pos.y +10)))
                    #The following print statement was a part of the white box testing for this function
                    #print("Bullet was fired")
            for i in range(0,len(self.bullets)):
                if 0 <=i < len(self.bullets):
                    self.bullets[-i].moveForEnemy(window)
                    #The following print statement was a part of the white box testing for this function
                    #print("Bullet was moved")

        def takeDamage(self, amount):
            super().takeDamage(amount)
            #The following print statement was a part of the white box testing for this function
            #print(f"damage was dealt to {self}")
            if self.h ==0:
                #The following print statement was a part of the white box testing for this function
                #print(self.h)
                player.increaseScore(100)
                

    class Kamikaze(Enemy):
        def __init__(self, health, speed, dmg,  pos, scrollSpeed, color):
            super().__init__(health, speed, dmg, pos, scrollSpeed, color)
            self.countDown=40
            self.shot = False
            self.countDownStart= False

        #Required overridden shoot function as the kamikaze enemies shoot in all directions instead of just at player
        def shoot(self, playerLocation):
            if self.h > 0:
                if abs(self.pos.y+10 -playerLocation.y) < 80 and abs(self.pos.x+10 -playerLocation.x) < 80:
                    self.countDownStart = True
                    if self.shot == False:
                        for i in range(0,9):
                            angle =22.5 * i
                            self.bullets.append(Projectile(1, angle, 4, pygame.Vector2(self.pos.x +10, self.pos.y +10)))
                            self.shot = True
                        #The following print statement was a part of the white box testing for this function
                        #print("Boom!")
                    
                    for i in range(0,len(self.bullets)):
                        if 0 <=i < len(self.bullets):
                            self.bullets[-i].moveForEnemy(window)
                    if self.countDown <= 0:
                        self.h -=1
                if self.countDownStart:
                    self.countDown -=1
                    
                
        #required overridden move function as kamikaze enemies have different pathfinding
        def move(self, playerLocation):
            if self.countDownStart == False:
                if self.h > 0:
                    if playerLocation.x > self.pos.x:
                        if self.pos.x < window.get_width()-100:
                            self.pos.x += self.speed
                    if playerLocation.x < self.pos.x:
                        if self.pos.x >80:
                            self.pos.x -= self.speed
                    if playerLocation.y > self.pos.y:
                            self.pos.y += self.speed
                    if playerLocation.y < self.pos.y:
                            self.pos.y -= self.speed
            self.pos.y += scrollSpeed


    #Class for the buildings on the side
    #Required a lot of RNG
    class Building():
        def __init__(self, length, width, pos, scrollSpeed, enemyPresent):
            self.length = length
            self.width = width
            self.pos = pos
            self.scSp = scrollSpeed
            self.enemy = enemyPresent
            self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, self.width, self.length)
            self.enemies=0
            #Adds an enemy instance to be attached to the top of the building
            if self.enemy:
                if self.pos.x > 200:
                    self.enemies=(Enemy(1, 0, 1, pygame.Vector2(self.pos.x-10, self.pos.y+self.length/2-10), scrollSpeed, (255,0,0)))
                else:
                    self.enemies=(Enemy(1, 0, 1, pygame.Vector2(self.pos.x+self.width-10, self.pos.y+self.length/2-10), scrollSpeed, (255,0,0)))
        
        def draw(self):
            self.pos.y += scrollSpeed
            self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, self.width, self.length)
            self.drawnRect = pygame.draw.rect(window, ((145,165,195)),self.rect)
            if self.enemy:
                if self.enemies.h >0:
                    for n in range(0, len(player.bullets)):
                        if self.enemies.rect.colliderect(player.bullets[n]):
                            self.enemies.takeDamage(player.bullets[n].d)
                    self.enemies.pos.y += scrollSpeed
                    self.enemies.draw(window)
                    self.enemies.shoot(player.pos)
                
        

    #The projectile that the player and the enemies fire
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
        
        ### Enemies required a different function for movement of bullets. 
        #   The angles output by the angle between the enemy and the player 
        #   were of a different format than the ones given by the player and
        #   required a different function to make the bullets travel in the right direction
        def moveForEnemy(self,window):
            if self.a < 0:
                self.pos.x -= self.speed* math.cos(math.radians(self.a))
            else:
                self.pos.x += self.speed* math.cos(math.radians(self.a))
            self.pos.y -= self.speed* -abs(math.sin(math.radians(self.a)))
            self.rect = pygame.rect.Rect(self.pos.x, self.pos.y,2,2)
            self.drawnRect = pygame.draw.rect(window, (255,255,255), self.rect)
            self.ut +=1
        
        #Tells the movement functions if the bullets are valid
        #based on where they are and the time since instantiation.
        #Print statements are from white box testing
        def drawCheck(self):
            if self.pos.y > 0 and self.ut <=25:
                #print(True)
                return True
            else:
                #print(False)
                return False
                

    #Manages the instantiation, deaths of enemies and boxes, and the instantiations of 
    class Environment():
        def __init__(self, scrollSpeed):
            self.scr = scrollSpeed
            self.boxes = []
            self.enemies = []
            self.buildings= [Building(150,50,pygame.Vector2(0,0),0, False)]
            self.powerups =[]
            
        #Randomly creates instances of boxes
        def instantiateBox(self):
            if uptime % random.randint(1, 7000)==0:
                self.boxes.append(Box(random.randint(3,7),scrollSpeed,pygame.Vector2(random.randint(80,295),-30)))
            self.boxMgr()
        
        #Moves, draws, and checks whether boxes should be taking damage
        def boxMgr(self):
            for i in range(0,len(self.boxes)):
                self.boxes[i].move()
                self.boxes[i].draw()
                self.boxes[i].checkDamage()
        
        #Randomly creates instances of buildings
        def instantiateBuilding(self):

            length = random.randint(140, 180)
            width = random.randint(60, 80)
            place = random.randint(0,4)
            enemy = bool(random.randint(-10,1))
            bothOffset = random.randint(0,10)
            both=False
            
            if place <= 1:
                place = 0

            elif 1 < place <=3:
                place = window.get_width()-width

            else:
                both=True
                left =bool(random.randint(-10,1))
                right = bool(random.randint(-10,1))
                
            
            if self.buildings[-1].pos.y >= random.randint(0,20):
                if both == True:
                    self.buildings.append(Building(length,width,pygame.Vector2(0, -length), scrollSpeed, not left))
                    self.buildings.append(Building(length-bothOffset,width-bothOffset,pygame.Vector2(window.get_width()-width+bothOffset, -length-bothOffset), scrollSpeed, not right))
                    #The following print statement was a part of the white box testing for this function
                    #print("2 buildings were instantiated")
                else:
                    self.buildings.append(Building(length,width,pygame.Vector2(place, -length), scrollSpeed, not enemy))
                    #The following print statement was a part of the white box testing for this function
                    #print("1 building was instantiated")
        
        #Randomly creates instances of enemies
        def spawnEnemy(self):
            if uptime % random.randint(1, 1000)==0:
                
                if len(self.enemies) <uptime/1000:
                    if random.randint(0,9) == 9:
                        self.enemies.append(Kamikaze(1, 2, 1, pygame.Vector2(random.randint(80,300), -20),scrollSpeed, (255,140,0)))
                    else:
                        self.enemies.append(Enemy(1,2,1,pygame.Vector2(random.randint(80,300), -20),scrollSpeed,(255,0,0)))

        #Checks health of enemies
        def healthCheck(self, index):
            if self.enemies[index].h >0:
                return True
            else:
                return False

        #manages movements, drawing and shooting of enemies
        def manager(self, playerLocation):
            for i in range(0,len(self.enemies)):
                if 0 <= i < len(self.enemies):
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
                        
            #Draws, moves and checks presence of powerups     
            for i in range(0, len(self.powerups)):
                if 0 <= i < len(self.powerups):
                    self.powerups[-i].drawAndCheck()
            #draws and moves buildings
            for i in range(0, len(self.buildings)):
                self.buildings[i].draw()
        
        #removes boxes when boxes are on 0 health
        def removeBox(self, boxToRemove):
            self.boxes.remove(boxToRemove)
            #The following print statement was a part of the white box testing for this function
            #print("Box removed")
        
        #removes enemies when enemies are on 0 health
        def removeEnemy(self, enemyToRemove):
            self.enemies.pop(enemyToRemove)
            #The following print statement was a part of the white box testing for this function
            #print("Enemy removed")

    #Defines powerups
    class powerUp():
        def __init__(self, type, pos) -> None:
            self.t=type
            self.pos = pygame.Vector2(pos.x, pos.y)
            self.rect = pygame.rect.Rect(self.pos.x,self.pos.y,10,10)
            self.collected = False

        def drawAndCheck(self):
            if self.collected == False:
                self.pos.y += scrollSpeed
                self.rect =pygame.rect.Rect(self.pos.x,self.pos.y,10,10)
                self.drawnRect = pygame.draw.rect(window,(255,255,0),self.rect)
            
                if self.rect.colliderect(player): 
                    if self.t == 1:
                        player.increaseScore(1000)
                        #The following print statement was a part of the white box testing for this function
                        #print("Powerup collected")
                        self.collected = True
                    elif self.t == 2:
                        player.increaseHealth(1)
                        #The following print statement was a part of the white box testing for this function
                        #print("Powerup collected")
                        self.collected = True
            else:
                world.powerups.remove(self)
    
    #This function was used for the purpose of black box testing
    #def BlackBoxTest(testee, index):
    #    if testee == world:
    #        print(world.healthCheck(index))
    #    if isinstance(testee, Destructible):
    #        x=y=z=0
    #        x1=y1=z1=False
    #        for i in range(1000):
    #            if testee.drop() == 1:
    #                x+=1
    #            if testee.drop() == 2:
    #                y+=1
    #            if testee.drop() == False:
    #                z+=1
    #        if 0.2 < x/1000 < 0.4:
    #            x1=True
    #        if 0 < y/1000 < 0.2:
    #            y1=True
    #        if 0.4 < z/1000< 1:
    #            z1=True
    #        if x1==y1==z1==True:
    #            print("Result is acceptable")
    #        else:
    #            print("Result is unacceptable")

    pygame.init()

    scrollSpeed = 2
    window = pygame.display.set_mode((400,550))
    window.fill((0,0,0))
    running = True
    clock = pygame.time.Clock()
    uptime =0
    position = pygame.Vector2(window.get_width()/2, window.get_height()/2)

    player = Player(3,5,1,position,0, scrollSpeed,(0,255,0))
    world = Environment(scrollSpeed)
    font = pygame.font.SysFont("Papyrus", 21)
    
    #main game loop
    while running:
        text = font.render(f"Health: {player.h}", False, (200, 200, 200))
        text2 = font.render(f"Score: {player.sc}", False, (200, 200, 200))
        clock.tick(60)
        
        uptime +=1
        window.fill("#B09060")

        #Used for blackbox testing
        #BlackBoxTest(player, 0)
        #if len(world.enemies) > 0:
        #    BlackBoxTest(world, 0)

        world.instantiateBuilding()
        world.instantiateBox()
        world.spawnEnemy()
        world.manager(player.pos)
        
        
        player.draw(window)
        player.move()
        player.shoot(uptime)
        player.checkDamage()
            
        window.blit(text, pygame.Vector2(75,0))
        window.blit(text2, pygame.Vector2(250,0))
            
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

#run the entire program
if __name__ == "__main__":
    main()