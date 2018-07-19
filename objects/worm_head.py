import pygame

import config
from objects.basic_object import BasicObject


class WormHead(BasicObject):
    def __init__(self, x, y, angle):
        super().__init__(x, y, 0, 0)
        self._angle = angle
        self.left_point = [self._x - 10, self._y]
        self.right_point = [self._x + 10, self._y]
        self.top_point = [self._x, self._y - 10]

    def update(self):
        self.left_point[0] = self.left_point[0] + self._speed_x
        self.left_point[1] = self.left_point[1] + self._speed_y

        self.right_point[0] = self.right_point[0] + self._speed_x
        self.right_point[1] = self.right_point[1] + self._speed_y

        self.top_point[0] = self.top_point[0] + self._speed_x
        self.top_point[1] = self.top_point[1] + self._speed_y

    def draw(self, surface):
        pygame.draw.polygon(surface, config.color_aqua,
                            (self.left_point, self.right_point, self.top_point), 5)

    @property
    def left_border(self):
        return self.left_point

    @property
    def right_border(self):
        return self.right_point

