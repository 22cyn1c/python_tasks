class AmericanDate:
    def __init__(self, y, m, d):
        self.y = str(y)
        self.m = str(m)
        self.d = str(d)
        self.d1 = self.d
        self.m1 = self.m
        if len(self.d) == 1:
            self.d1 = '0' + self.d
        if len(self.m) == 1:
            self.m1 = '0' + self.m

    def format(self):
        return f'{self.m1}.{self.d1}.{self.y}'

    def set_year(self, sy):
        self.y = sy

    def set_day(self, sd):
        self.d = str(sd)
        self.d1 = self.d
        if len(self.d) == 1:
            self.d1 = '0' + self.d

    def set_month(self, sm):
        self.m = str(sm)
        self.m1 = self.m
        if len(self.m) == 1:
            self.m1 = '0' + self.m

    def get_year(self):
        return self.y

    def get_day(self):
        return self.d

    def get_month(self):
        return self.m


class EuropeanDate:
    def __init__(self, y, m, d):
        self.y = str(y)
        self.m = str(m)
        self.d = str(d)
        self.d1 = self.d
        self.m1 = self.m
        if len(self.d) == 1:
            self.d1 = '0' + self.d
        if len(self.m) == 1:
            self.m1 = '0' + self.m

    def format(self):
        return f'{self.d1}.{self.m1}.{self.y}'

    def set_year(self, sy):
        self.y = sy

    def set_day(self, sd):
        self.d = str(sd)
        self.d1 = self.d
        if len(self.d) == 1:
            self.d1 = '0' + self.d

    def set_month(self, sm):
        self.m = str(sm)
        self.m1 = self.m
        if len(self.m) == 1:
            self.m1 = '0' + self.m

    def get_year(self):
        return self.y

    def get_day(self):
        return self.d

    def get_month(self):
        return self.m