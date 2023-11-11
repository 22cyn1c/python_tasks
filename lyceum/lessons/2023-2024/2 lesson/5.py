class Point:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y

    def get_x(self):
        return int(self.x)

    def get_y(self):
        return int(self.y)

    def get_coords(self):
        return (self.x, self.y)

    def __invert__(self):
        return Point(self.n, self.y, self.x)

    def __str__(self):
        return f'{self.n}({self.x}, {self.y})'
