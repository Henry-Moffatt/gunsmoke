from destructible import Destructible

class Box(Destructible):
    def __init__(self, health, dropChances, dropItems, scrollSpeed, window, player, world, uptime):
        super().__init__(health, dropChances, dropItems, scrollSpeed, window, player, world, uptime)