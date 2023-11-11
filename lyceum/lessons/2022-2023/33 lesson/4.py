class MinStat:
    def __init__(self):
        self.a = []

    def add_number(self, v):
        self.a.append(v)

    def result(self):
        if self.a:
            return min(self.a)
        else:
            return None


class MaxStat:
    def __init__(self):
        self.a = []

    def add_number(self, v):
        self.a.append(v)

    def result(self):
        if self.a:
            return max(self.a)
        else:
            return None


class AverageStat:
    def __init__(self):
        self.a = []

    def add_number(self, v):
        self.a.append(v)

    def result(self):
        if self.a:
            return sum(self.a) / len(self.a)
        else:
            return None