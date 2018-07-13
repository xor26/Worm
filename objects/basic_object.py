class BasicObject:
    def __init__(self, x, y, speed_x, speed_y):
        self._x = x
        self._y = y
        self._speed_x = speed_x
        self._speed_y = speed_y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def speed_x(self):
        return self._speed_x

    @speed_x.setter
    def speed_x(self, value):
        self._speed_x = value

    @property
    def speed_y(self):
        return self._speed_y

    @speed_y.setter
    def speed_y(self, value):
        self._speed_y = value

    def update(self):
        self._x += self._speed_x
        self._y += self._speed_y

    def draw(self, surface):
        pass
