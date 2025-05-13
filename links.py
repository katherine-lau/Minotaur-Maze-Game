import pygame
import requests
from io import BytesIO


def load_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = BytesIO(response.content)
        return pygame.image.load(data).convert_alpha()
    else:
        raise Exception("Failed to load image from URL.")

pygame.init()
pygame.display.set_mode((1,1))

available_items = [
        {"name" : "Sword",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/sword.png"),
         "description" : "A weapon to strike down the Minotaur with. Sharp and lethal."},
        {"name" : "Shield",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/shield.png"),
         "description" : "A shield to protect yourself with. Strong and sturdy."},
        {"name" : "Potion_2",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Potion_1.25",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Potion_1.5",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Potion_0.5",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Amulet_HP",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet. All your wounds have been healed!"},
        {"name" : "Amulet_Ow",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet. Ouch! You've been cursed to take damage!"},
        {"name" : "Amulet_Ow_Min",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet. The minotaur has been cursed!"},
        {"name" : "Amulet_T_speed",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet. Run, run, run!"},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll. The words are all illegible."},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll. Water-damaged"},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll. Old and decayed."},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll. Someone's old grocery list, possibly?"},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll. The words are utter gibberish."},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll. Not helpful."},
        {"name" : "Amulet_min_speed",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A mysterious amulet. Oh no! The minotaur's speed has increased!"},
        {"name" : "Amulet_strength",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet. Hit harder!"},
        {"name" : "Potion_0.25",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Potion_0.75",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        
    ]
