class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.p = proteins
        self.f = fats
        self.c = carbohydrates
        self.k = self.p * 4 + self.f * 9 + self.c * 4

    def get_proteins(self):
        return self.p

    def get_fats(self):
        return self.f

    def get_carbohydrates(self):
        return self.c

    def get_kcalories(self):
        return self.k

    def __add__(self, other):
        s = self.p + other.p
        m = self.f + other.f
        c = self.c + other.c
        return FoodInfo(s, m, c)