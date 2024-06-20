from main import *

class Destructible:
    def __init__(self,health,dropChances,dropItems, scrollSpeed):
        self.h= health
        self.dC=dropChances
        self.dI=dropItems
        self.scr=scrollSpeed
    
    def takeDamage(self, amount):
        self.h -= amount

    def drop(self):
        pass