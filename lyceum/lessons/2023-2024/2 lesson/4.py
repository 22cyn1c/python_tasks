class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return int(self.x)

    def get_y(self):
        return int(self.y)

    def get_coords(self):
        return (self.x, self.y)
