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

available_items = [
        {"name" : "Item name",
         "icon" : load_image("Link here"),
         "description" : "Description here"}
    ]