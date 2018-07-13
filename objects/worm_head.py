import pygame

from objects.basic_object import BasicObject


class WormHead(BasicObject):
    def __init__(self, x, y, angle):
        super().__init__(x, y, 0, 0)
        self._angle = angle

    def draw(self, surface):
        first_point = (self._x-10, self._y)
        second_point = (self._x+10, self._y)
        third_point = (self._x, self._y-10)
        pygame.draw.polygon(surface, (0, 255, 255), (first_point, second_point, third_point), 5)
