import pygame as pg

class World():
    def __init__(self, world_data, map_image):
        self.image = map_image
        self.level_data = world_data

    def process_data(self):
        # look through data to extract relevant infos
        for layer in self.level_data.get('layers', None):
            if layer.get('name', None) == 'waypoints':
                print(layer)


    def draw(self, surface):
        surface.blit(self.image,(0,0))

