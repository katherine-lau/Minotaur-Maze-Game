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
        {"name" : "Potion",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Potion",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Potion",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Potion",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Amulet",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet."},
        {"name" : "Amulet",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet."},
        {"name" : "Amulet",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet."},
        {"name" : "Amulet",
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
        {"name" : "Amulet",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A mysterious amulet."},
        {"name" : "Amulet",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A mysterious amulet."},
        {"name" : "Potion",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."},
        {"name" : "Potion",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion."}
        
    ]