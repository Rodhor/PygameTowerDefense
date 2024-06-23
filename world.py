import pygame as pg


class World:
    def __init__(self, world_data, map_image):
        self.tile_map = []
        self.waypoints = []
        self.image = map_image
        self.level_data = world_data

    def process_data(self):
        # look through data to extract relevant infos
        for layer in self.level_data.get("layers", None):
            if layer.get("name", None) == "tilemap":
                self.tile_map = layer.get("data")
            elif layer.get("name", None) == "waypoints":
                for obj in layer.get("objects", None):
                    waypoint_data = obj.get("polyline", None)
                    self.process_waypoints(waypoint_data)

    def process_waypoints(self, data):
        # Iterate through waypoints to extract individual sets of x and y coordinates
        for point in data:
            temp_x = point.get("x")
            temp_y = point.get("y")
            self.waypoints.append((temp_x, temp_y))

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
