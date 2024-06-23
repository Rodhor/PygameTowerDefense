import pygame as pg
from enemy import Enemy
from world import World
from turret import Turret
from button import Button
import constants as c
import json


# initialise pygame
pg.init()

# create clock
clock = pg.time.Clock()

# create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")


### Game variables
placing_turret = False


### Load images ###
# Map
map_image = pg.image.load("levels/level.png").convert_alpha()


# Individual turret image for cursor
cursor_turret = pg.image.load("assets/images/turrets/cursor_turret.png").convert_alpha()

# enemies
enemy_image = pg.image.load("assets/images/enemies/enemy_1.png").convert_alpha()

# Side panel buttons
buy_turret_image = pg.image.load("assets/images/buttons/buy_turret.png").convert_alpha()
cancel_image = pg.image.load("assets/images/buttons/cancel.png").convert_alpha()


# Load json data for level
with open("levels/level.tmj") as file:
    world_data = json.load(file)


# Create turret
def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE

    # Calculate the sequential number of tile
    mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x

    # Check if currently selected tile is grass - represented by a 7 in the tilemap
    if world.tile_map[mouse_tile_num] == 7:

        # Check if there is already a turret placed on tile
        space_is_free = True
        for turret in turret_group:
            if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
                space_is_free = False

        # If there is no turrets, place a turret
        if space_is_free:
            new_turret = Turret(cursor_turret, mouse_tile_x, mouse_tile_y)
            turret_group.add(new_turret)


# Create World
world = World(world_data, map_image)
world.process_data()

# Create Groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)

# Create sidepanel with buttons
turret_button = Button(c.SCREEN_WIDTH + 30, 120, buy_turret_image, True)
cancel_button = Button(c.SCREEN_WIDTH + 50, 180, cancel_image, True)


# Game loop
run = True
while run:

    clock.tick(c.FPS)

    ####################
    # UPDATING SECTION #
    ####################

    # Update groups
    enemy_group.update()

    ####################
    # Drawing SECTION #
    ####################
    screen.fill("gray100")

    # Draw level
    world.draw(screen)

    # Draw enemy groups
    enemy_group.draw(screen)
    turret_group.draw(screen)

    # Draw buttons
    # Check if a new turret was initiated for placement
    if turret_button.draw(screen):
        placing_turret = True

    # If we are placing turret, show cancel button
    if placing_turret:

        # Show cursor turret
        cursor_rect = cursor_turret.get_rect()
        cursor_pos = pg.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[0] <= c.SCREEN_WIDTH:
            screen.blit(cursor_turret, cursor_rect)

        if cancel_button.draw(screen):
            placing_turret = False

    # Event handler
    for event in pg.event.get():
        # Quit program
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()

            # Check if mouse is on the game area
            if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
                if placing_turret:
                    create_turret(mouse_pos)

    pg.display.flip()

pg.quit()
