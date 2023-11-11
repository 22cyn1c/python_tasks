class Profile:
    def __init__(self, name):
        self.n = name

    def info(self):
        return ''

    def describe(self):
        return f'{self.n}, {self.info()}'


class Vacancy(Profile):
    def __init__(self, name, zp):
        super().__init__(name)
        self.zp = zp

    def info(self):
        return f'Предлагаемая зарплата: {self.zp}'


class Resume(Profile):
    def __init__(self, name, st):
        super().__init__(name)
        self.st = st

    def info(self):
        return f'Стаж работы: {self.st}'
