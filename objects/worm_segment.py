from math import cos, sin

import pygame

import config
from objects.basic_object import BasicObject


class WormSegment(BasicObject):

    def __init__(self, x, y, oscillation_direction):
        """oscillation_plane_angle - angle of inclination of the plane of oscillation"""
        super().__init__(x, y, 0, 0)
        self._oscillation_plane_angle = 0
        self._oscillation_speed = config.worm_segments_oscillation_speed * oscillation_direction
        self._radius = config.worm_segments_radius
        self._oscillation_offset = 0

    @property
    def oscillation_plane_angle(self):
        return self._oscillation_plane_angle

    @oscillation_plane_angle.setter
    def oscillation_plane_angle(self, value):
        self._oscillation_plane_angle = value

    def update(self):
        oscillation_pojection_on_x = cos(self._oscillation_plane_angle)*self._oscillation_speed
        oscillation_pojection_on_y = sin(self._oscillation_plane_angle)*self._oscillation_speed
        self._oscillation_offset += self._oscillation_speed
        if abs(self._oscillation_offset) >= 10:
            self._oscillation_speed *= -1
        self._x += self.speed_x+int(oscillation_pojection_on_x)
        self._y += self.speed_y+int(oscillation_pojection_on_y)

    def draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 255), (self.x, self.y), self._radius)

