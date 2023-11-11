class MinMaxWordFinder:
    def __init__(self):
        self.t = 0
        self.t1 = 10 * 99
        self.mx = []
        self.mn = []

    def add_sentence(self, s):
        for i in s.split():
            if len(i) > self.t:
                self.t = len(i)
                self.mx = []
                self.mx.append(i)
            elif len(i) == self.t:
                if i not in self.mx:
                    self.mx.append(i)
            if len(i) < self.t1:
                self.t1 = len(i)
                self.mn = []
                self.mn.append(i)
            elif len(i) == self.t1:
                self.mn.append(i)

    def shortest_words(self):
        return sorted(self.mn)

    def longest_words(self):
        return sorted(self.mx)