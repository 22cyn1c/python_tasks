class ReversedList:
    def __init__(self, e):
        self.e = e
        self.e = self.e[::-1]

    def __len__(self):
        return len(self.e)

    def __getitem__(self, item):
        return self.e[item]