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
         "description" : "A weapon to strike down the Minotaur with."},
        {"name" : "Shield",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/shield.png"),
         "description" : "A shield to protect yourself with."},
        {"name" : "Potion_2",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion. Seems a bit past it's expiration date though..."},
        {"name" : "Potion_1.25",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion. Do you really want to drink it though...?"},
        {"name" : "Potion_1.5",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion. Kind of gunky. Might be expired."},
        {"name" : "Potion_0.5",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion. Unlabelled. May kill you or save you. Safer not to drink it at all."},
        {"name" : "Amulet_HP",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet. Shiny."},
        {"name" : "Amulet_Ow",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet. Doesn't seem like it does anything."},
        {"name" : "Amulet_Ow_Min",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet. Might curse you."},
        {"name" : "Amulet_T_speed",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A myseterious amulet. A fancy trinket."},
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
         "description" : "A mysterious amulet."},
        {"name" : "Amulet_strength",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/amulet.png"),
         "description" : "A mysterious amulet. Doesn't really do anything..."},
        {"name" : "Potion_0.25",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion. ...Is this just sugar water?"},
        {"name" : "Potion_0.75",
         "icon" : load_image("https://raw.githubusercontent.com/katherine-lau/Minotaur-Maze-Game/main/assets/potion.png"),
         "description" : "A potion. Might be toxic."}
        
    ]
