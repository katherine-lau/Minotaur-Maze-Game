import pygame
import commons
import gameplay
import maze
import minotaur

def has_sword_or_shield(items):
    has_sword = any(item['name'] == "Sword" for item in items)
    has_shield = any(item['name'] == "Shield" for item in items)
    return has_sword, has_shield

def hero_attack():
    if minotaur.sword and maze.hero_pos == maze.minotaur_pos:
        maze.minotaur_hp -= 100
    #if minotaur.shield and maze.hero_pos == maze.minotaur_pos:
        #maze.hero_hp -= 0
