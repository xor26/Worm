import pygame

from objects.basic_object import BasicObject


class WormHead(BasicObject):
    def __init__(self, x, y, angle):
        super().__init__(x, y, 0, 0)
        self._angle = angle

    def draw(self, surface):
        pass
        # pygame.draw.rect(surface,  (0, 255, 255), (self.x+5, self.y+5, self.x-5, self.y-5), 10)
