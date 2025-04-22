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
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"},
        {"name" : "Item name",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/bull.png"),
         "description" : "Description here"}
        
    ]