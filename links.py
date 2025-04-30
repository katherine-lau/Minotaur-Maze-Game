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
         "description" : "A weapon to defend yourself with."},
        {"name" : "Shield",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/shield.png"),
         "description" : "A shield to protect yourself with."},
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
         "description" : "A myseterious amulet."},
        {"name" : "Amulet_Ow",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet."},
        {"name" : "Amulet_Ow_Min",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet."},
        {"name" : "Amulet_T_speed",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet."},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll."},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll."},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll."},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll."},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll."},
        {"name" : "Scroll",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/artifact.png"),
         "description" : "An ancient scroll."},
        {"name" : "Amulet_min_speed",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A mysterious amulet."},
        {"name" : "Amulet_strength",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A mysterious amulet."},
        {"name" : "Potion_0.25",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Potion_0.75",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."}
        
    ]
