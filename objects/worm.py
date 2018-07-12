import config
from objects.basic_object import BasicObject
from objects.worm_head import WormHead
from objects.worm_segment import WormSegment


class Worm(BasicObject):
    def __init__(self, x, y, speed_x, speed_y,):
        super().__init__(x, y, speed_x, speed_y)
        self._head = WormHead(x, y, 0)
        self._segments = []
        y_offset = 10
        oscillation_direction = 1
        for i in range(0, config.worm_segments):
            segment = WormSegment(x, y+y_offset, oscillation_direction)
            self._segments.append(segment)
            y_offset += 10
            oscillation_direction *= -1

    def get_segments(self):
        return self._segments

    @BasicObject.speed_x.setter
    def speed_x(self, value):
        self._speed_x = value
        for segment in self._segments:
            segment._speed_x = value

    @BasicObject.speed_y.setter
    def speed_y(self, value):
        self._speed_y = value
        for segment in self._segments:
            segment._speed_y = value

    def draw(self, surface):
        self._head.draw(surface)
        for segment in self._segments:
            segment.update()
            segment.draw(surface)
