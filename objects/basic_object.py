class BasicObject:
    def __init__(self, x, y, speed_x, speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def left_border(self):
        return [self.x, self.y]

    def right_border(self):
        return [self.x, self.y]

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, surface):
        pass

