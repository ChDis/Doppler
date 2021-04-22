from point import Point


class Observer(Point):
    def __init__(self, coordinates, velocity, size, screen, color):
        super().__init__(coordinates, velocity, size, screen, color)
        