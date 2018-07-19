import pygame

import config
from objects.basic_object import BasicObject
from objects.worm_head import WormHead
from objects.worm_segment import WormSegment


class Worm(BasicObject):
    def __init__(self):
        self._head = WormHead(config.worm_start_position_x, config.worm_start_position_y, 0)
        self._segments = []
        y_offset = 10
        oscillation_direction = 1
        for i in range(0, config.worm_segments):
            segment = WormSegment(config.worm_start_position_x,
                                  config.worm_start_position_y+y_offset,
                                  oscillation_direction)
            self._segments.append(segment)
            y_offset += 15
            oscillation_direction *= -1
        super().__init__(config.worm_start_position_x, config.worm_start_position_y,
                         config.worm_x_initial_speed, config.worm_y_initial_speed)

    @BasicObject.speed_x.setter
    def speed_x(self, value):
        self._speed_x = value
        self._head.speed_x = value
        for segment in self._segments:
            segment.speed_x = value

    @BasicObject.speed_y.setter
    def speed_y(self, value):
        self._speed_y = value
        self._head.speed_y = value
        for segment in self._segments:
            segment.speed_y = value

    def draw(self, surface):
        self._head.update()
        self._head.draw(surface)
        for segment in self._segments:
            segment.update()
            segment.draw(surface)
        first_lb = self._head.left_border
        first_rb = self._head.right_border
        for segment in self._segments:
            second_lb = segment.left_border
            second_rb = segment.right_border
            pygame.draw.aaline(surface, config.color_aqua, first_lb, second_lb, 15)
            pygame.draw.aaline(surface, config.color_aqua, first_rb, second_rb, 15)
            first_lb = second_lb
            first_rb = second_rb





