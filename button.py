import pygame as pg


class Button:
    def __init__(self, x, y, image):

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        # get mouse position
        pos = pg.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                pass

        # Draw button on screen
        surface.blit(self.image, self.rect)
