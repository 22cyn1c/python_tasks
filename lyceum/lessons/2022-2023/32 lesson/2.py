class Button:
    def __init__(self):
        self.c = 0

    def click(self):

        self.c += 1

    def click_count(self):
        return self.c

    def reset(self):
        self.c = 0