import pygame as pg
from enemy import Enemy
from world import World
import constants as c
import json


# initialise pygame
pg.init()

# create clock
clock = pg.time.Clock()

# create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")

### Load images ###

# Map
map_image = pg.image.load("levels/level.png").convert_alpha()

# enemies
enemy_image = pg.image.load("assets/images/enemies/enemy_1.png").convert_alpha()

# Load json data for level
with open("levels/level.tmj") as file:
    world_data = json.load(file)


# Create World
world = World(world_data, map_image)
world.process_data()


# Crete Groups
enemy_group = pg.sprite.Group()

waypoints = [(100, 100), (400, 200), (400, 100), (200, 300)]

enemy = Enemy(waypoints, enemy_image)

enemy_group.add(enemy)

# Game loop
run = True
while run:

    clock.tick(c.FPS)

    screen.fill("grey100")

    # Draw level
    world.draw(screen)

    # draw enemy path
    pg.draw.lines(screen, "grey0", False, waypoints)

    # Update groups
    enemy_group.update()

    # Draw enemy groups
    enemy_group.draw(screen)

    # Event handler
    for event in pg.event.get():
        # Quit program
        if event.type == pg.QUIT:
            run = False

    # Update display
    pg.display.flip()

pg.quit()
