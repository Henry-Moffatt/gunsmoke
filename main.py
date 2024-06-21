import pygame
import random
from pygame.locals import *
import math
from player import Player
from environment import Environment

pygame.init()
window = pygame.display.set_mode((400,550))
window.fill((0,0,0))
running = True
clock = pygame.time.Clock()
uptime =0

position = pygame.Vector2(window.get_width()/2, window.get_height()/2)
pos2 = pygame.Vector2(window.get_width()/2, window.get_height()/2)

scrollSpeed = 1
player = 0

world = Environment(scrollSpeed, player, window, 0, uptime)
player = Player(3,0,0,5,10,2,position,0,0, scrollSpeed,(0,255,0), window, world, uptime)
world = Environment(scrollSpeed, player, window, 0, uptime)

font = pygame.font.SysFont("Papyrus", 21)

while running:
        text = font.render(f"Health: {player.h}", False, (200, 200, 200))
        text2 = font.render(f"Score: {player.sc}", False, (200, 200, 200))
        dt =clock.tick(60)
        uptime +=1
        window.fill((0,0,0))
        player.draw()
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
        pygame.display.flip()
