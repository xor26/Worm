import pygame
import config
from objects.worm import Worm


class WormSimulator:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((config.screen_width, config.screen_height))
        self.screen.fill((0, 0, 0))

        self.objects = []
        worm = Worm()
        self.objects.append(worm)

    def run(self):
        while 1:
            self.clock.tick(25)
            self.screen.fill((0, 0, 0))
            for game_object in self.objects:
                game_object.draw(self.screen)

            pygame.display.flip()


if __name__ == '__main__':
    WormSimulator().run()
