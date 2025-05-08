import pygame
import commons
import gameplay
import maze
import minotaur

def has_item(items):
    has_sword = any(item['name'] == "Sword" for item in items)
    has_shield = any(item['name'] == "Shield" for item in items)
    has_hp_amu = any(item['name'] == "Amulet_HP" for item in items)
    has_ow_amu = any(item['name'] == "Amulet_Ow" for item in items)
    has_ow_min = any(item['name'] == "Amulet_Ow_Min" for item in items)
    has_T_sp_amu = any(item['name'] == "Amulet_T_speed" for item in items)
    has_min_sp_amu = any(item['name'] == "Amulet_min_speed" for item in items)
    return has_sword, has_shield, has_hp_amu, has_ow_amu, has_ow_min, has_T_sp_amu, has_min_sp_amu

def hero_attack(items, damage):
    if minotaur.sword and maze.hero_pos == maze.minotaur_pos:
        maze.minotaur_hp -= damage
        if any(item['name'] == "Potion_2" for item in items):
            maze.minotaur_hp -= (damage + 125)
        if any(item['name'] == "Potion_1.25" for item in items):
            maze.minotaur_hp -= (damage + 100)
        if any(item['name'] == "Potion_1.5" for item in items):
            maze.minotaur_hp -= (damage + 65)
        if any(item['name'] == "Potion_0.5" for item in items):
            maze.minotaur_hp -= (damage - 50)
        if any(item['name'] == "Potion_0.25" for item in items):
            maze.minotaur_hp -= (damage - 25)
        if any(item['name'] == "Potion_0.75" for item in items):
            maze.minotaur_hp -= (damage - 75)
        if any(item['name'] == "Amulet_strength" for item in items):
            maze.minotaur_hp -= damage * 2
    return damage
    #if minotaur.shield and maze.hero_pos == maze.minotaur_pos:
        #maze.hero_hp -= 0

    
