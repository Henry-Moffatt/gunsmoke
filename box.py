from main import *

class Box(Destructible):
    def __init__(self, health, dropChances, dropItems):
        super().__init__(health, dropChances, dropItems)