class Date:
    def __init__(self, m, d):
        self.m = m
        self.d = d

    def __sub__(self, other):
        if self.m == 1:
            m = 0
        elif self.m == 2:
            m = 31
        elif self.m == 3:
            m = 59
        elif self.m == 4:
            m = 90
        elif self.m == 5:
            m = 120
        elif self.m == 6:
            m = 151
        elif self.m == 7:
            m = 181
        elif self.m == 8:
            m = 212
        elif self.m == 9:
            m = 243
        elif self.m == 10:
            m = 273
        elif self.m == 11:
            m = 304
        else:
            m = 334
        if other.m == 1:
            m1 = 0
        elif other.m == 2:
            m1 = 31
        elif other.m == 3:
            m1 = 59
        elif other.m == 4:
            m1 = 90
        elif other.m == 5:
            m1 = 120
        elif other.m == 6:
            m1 = 151
        elif other.m == 7:
            m1 = 181
        elif other.m == 8:
            m1 = 212
        elif other.m == 9:
            m1 = 243
        elif other.m == 10:
            m1 = 273
        elif other.m == 11:
            m1 = 304
        else:
            m1 = 334
        d = m + self.d
        d1 = m1 + other.d
        return d - d1