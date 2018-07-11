class BasicObject:
    def __init__(self, x, y, speed_x, speed_y):
        self._pos_x = x
        self._pos_y = y
        self._speed_x = speed_x
        self._speed_y = speed_y

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @property
    def speed_x(self):
        return self._speed_x

    @property
    def speed_y(self):
        return self._speed_y

    @pos_x.setter
    def pos_x(self, value):
        pass

    @pos_y.setter
    def pos_y(self, value):
        pass

    @speed_x.setter
    def speed_x(self, value):
        pass

    @speed_y.setter
    def speed_y(self, value):
        pass

    def update(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

    def draw(self):
        pass
