class Selector:
    def __init__(self, values):
        self.values = values
        self.od = []
        self.ev = []
        for i in self.values:
            if i % 2 == 0:
                self.ev.append(i)
            else:
                self.od.append(i)

    def get_odds(self):
        return self.od

    def get_evens(self):
        return self.ev