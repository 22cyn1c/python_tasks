class SquareFunction:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def __call__(self, n):
        return (self.n1 * n ** 2 + self.n2 * n, self.n3)[0] + (self.n1 * n ** 2 + self.n2 * n, self.n3)[1]
