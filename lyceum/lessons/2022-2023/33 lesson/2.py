class LeftParagraph:
    def __init__(self, n):
        self.list_words = []
        self.n = n

    def add_word(self, word):
        self.list_words.append(word)

    def end(self):
        s = ''
        k = 0
        for word in self.list_words:
            if k + len(word) <= self.n:
                s += word + ' '
                k += len(word) + 1
            else:
                print(s.rstrip())
                s = word + ' '
                k = len(word) + 1
        if k != 0:
            print(s)
        self.list_words = []


class RightParagraph:
    def __init__(self, n):
        self.list_words = []
        self.n = n

    def add_word(self, word):
        self.list_words.append(word)

    def end(self):
        s = ''
        k = 0
        for word in self.list_words:
            if k + len(word) <= self.n:
                s += word + ' '
                k += len(word) + 1
            else:
                print(' ' * (self.n - k + 1) + s.rstrip())
                s = word + ' '
                k = len(word) + 1
        if k != 0:
            print(' ' * (self.n - k + 1) + s.rstrip())
        self.list_words = []
