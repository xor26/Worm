from random import random, randint

import pygame

SCREEN_SIZE = 800, 600
WHITE = (255, 255, 255)
SEGMENT_RADIUS = 3


class Worm:

    def __init__(self):
        self.segments = {
            '1': [400, 0],
            '2': [400, 10],
            '3': [400, 20],
            '4': [400, 30],
            '5': [400, 40],
        }
        self.segments_speed = {
            '1': 10,
            '2': -10,
            '3': 10,
            '4': -10,
            '5': 10,
        }

        print(self.segments)
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.screen.fill((0, 0, 0))

    def wiggle_segment(self):
        for key in self.segments:
            self.segments[key][0] += self.segments_speed[key]
            self.segments[key][0] += randint(-3, 3)
            if self.segments[key][0] > 500:
                self.segments_speed[key] = -10
            if self.segments[key][0] < 300:
                self.segments_speed[key] = 10

    def draw_segment(self):
        for key in self.segments:
            pygame.draw.circle(self.screen, WHITE, self.segments[key], SEGMENT_RADIUS, SEGMENT_RADIUS)

    def run(self):
        while 1:
            self.clock.tick(25)
            self.screen.fill((0, 0, 0))
            self.wiggle_segment()
            self.draw_segment()
            pygame.display.flip()


if __name__ == '__main__':
    Worm().run()
