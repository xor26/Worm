class BasicObject:
    def __init__(self, x, y, speed_x, speed_y):
        self._x = x
        self._y = y
        self._speed_x = speed_x
        self._speed_y = speed_y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def speed_x(self):
        return self._speed_x

    @property
    def speed_y(self):
        return self._speed_y

    @x.setter
    def x(self, value):
        pass

    @y.setter
    def y(self, value):
        pass

    @speed_x.setter
    def speed_x(self, value):
        pass

    @speed_y.setter
    def speed_y(self, value):
        pass

    def update(self):
        self._x += self.speed_x
        self._y += self.speed_y

    def draw(self, surface):
        pass
