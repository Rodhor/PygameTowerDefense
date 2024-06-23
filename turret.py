import pygame as pg
import constants as c


class Turret(pg.sprite.Sprite):
    def __init__(self, sprite_sheet, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)

        self.cooldown = 1500
        self.last_shot = pg.time.get_ticks()

        ### Position variables ###
        self.tile_x = tile_x
        self.tile_y = tile_y

        # Calculate center coordinates of tile
        # 0.5 is added to get the tile center instead of top and left
        self.x = (self.tile_x + 0.5) * c.TILE_SIZE
        self.y = (self.tile_y + 0.5) * c.TILE_SIZE

        ### Animation variables ###
        self.sprite_sheet = sprite_sheet
        self.animate_list = self.load_images()
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()

        ### Update image ###
        self.image = self.animate_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def load_images(self):
        # Extract individual images from spritesheet
        size = self.sprite_sheet.get_height()
        animation_list = []

        for x in range(c.ANIMATION_STEPS):
            temp_img = self.sprite_sheet.subsurface(x * size, 0, size, size)
            animation_list.append(temp_img)

        return animation_list

    def update(self):
        # Search for new target once turret as cooled down
        if pg.time.get_ticks() - self.last_shot > self.cooldown:
            self.play_animation()

    def play_animation(self):
        # Update image
        self.image = self.animate_list[self.frame_index]

        # Check if enough time as passed since last update
        if pg.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
            self.update_time = pg.time.get_ticks()
            self.frame_index += 1

            # Check if animeation has finisched and set to idle
            if self.frame_index >= len(self.animate_list):
                self.frame_index = 0

                # Record time of last shot and start cooldown
                self.last_shot = pg.time.get_ticks()
