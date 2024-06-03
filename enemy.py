import pygame pg



class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self. rect = self.image.get_recht()
        self.rect.center = pos






