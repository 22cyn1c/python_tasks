class BigBell:
    def __init__(self):
        self.c = 0

    def sound(self):
        if self.c == 0:
            print("ding")
            self.c += 1
        elif self.c == 1:
            print("dong")
            self.c = 0