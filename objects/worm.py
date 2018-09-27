import pygame

import config
from objects.basic_object import BasicObject
from objects.worm_head import WormHead
from objects.worm_segment import WormSegment


class Worm(BasicObject):
    def __init__(self):
        self.head = WormHead(config.worm_start_position_x, config.worm_start_position_y, 0)
        self.segments = []
        y_offset = 10
        oscillation_direction = 1
        for i in range(0, config.worm_segments):
            segment = WormSegment(config.worm_start_position_x,
                                  config.worm_start_position_y+y_offset,
                                  oscillation_direction)
            self.segments.append(segment)
            y_offset += 15
            oscillation_direction *= -1
        super().__init__(config.worm_start_position_x, config.worm_start_position_y,
                         config.worm_x_initial_speed, config.worm_y_initial_speed)

    def speed_x(self, value):
        self.speed_x = value
        self.head.speed_x = value
        for segment in self.segments:
            segment.speed_x = value

    def speed_y(self, value):
        self.speed_y = value
        self.head.speed_y = value
        for segment in self.segments:
            segment.speed_y = value

    def draw(self, surface):
        self.head.update()
        self.head.draw(surface)
        for segment in self.segments:
            segment.update()
            segment.draw(surface)
        first_lb = self.head.left_border
        first_rb = self.head.right_border
        for segment in self.segments:
            second_lb = segment.left_border
            second_rb = segment.right_border
            pygame.draw.aaline(surface, config.color_aqua, first_lb, second_lb, 15)
            pygame.draw.aaline(surface, config.color_aqua, first_rb, second_rb, 15)
            first_lb = second_lb
            first_rb = second_rb





