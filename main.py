import pygame as pg
from enemy import Enemy
import constants as c



# initialise pygame
pg.init()


# create clock
clock = pg.time.Clock()

# create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")


# Load images
enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()

enemy = Enemy((200, 300), enemy_image)

# Crete Groups
enemy_group = pg.sprite.Group()


# Game loop 
run = True
while run:

    clock.tick(c.FPS)

    # Event handler
    for event in pg.event.get():
      # Quit program
        if event.type == pg.QUIT:
            run = False


pg.quit()



