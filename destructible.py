class Destructible:
    def __init__(self,health,dropChances,dropItems, scrollSpeed, window, player, world, uptime):
        self.h= health
        self.dC=dropChances
        self.dI=dropItems
        self.scr=scrollSpeed
        self.window = window
        self.world = world
        self.player = player
        self.uptime = uptime
    
    def takeDamage(self, amount):
        self.h -= amount

    def drop(self):
        pass