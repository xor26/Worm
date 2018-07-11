import pygame
import config
from basic_object import BasicObject


class WormSimulator:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((config.screen_width, config.screen_height))
        self.screen.fill((0, 0, 0))
        obj = BasicObject(10, 20, 30, 40)
        print(obj.__dict__)

    def run(self):
        while 1:
            self.clock.tick(25)
            self.screen.fill((0, 0, 0))
            pygame.display.flip()


if __name__ == '__main__':
    WormSimulator().run()
