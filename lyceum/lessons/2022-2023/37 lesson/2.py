class Bishop:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'B'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if not (0 <= self.row <= 7 and 0 <= self.col <= 7 and 0 <= row <= 7 and 0 <= col <= 7):
            return False
        for i in range(-7, 8):
            if self.row + i == row and self.col + i == col:
                return True
            if self.row - i == row and self.col - i == col:
                return True
            if self.row - i == row and self.col + i == col:
                return True
            if self.row - i == row and self.col + i == col:
                return True
        return False