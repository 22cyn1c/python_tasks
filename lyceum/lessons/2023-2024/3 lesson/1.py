class Note:

    def __init__(self, note, is_long=False):
        self.note = note
        self.index = PITCHES.index(note)
        self.is_long = is_long

    def play(self):
        print(self.note)

    def __str__(self):
        if self.is_long:
            return d_notes[self.note]
        return self.note

    def __eq__(self, o):
        return self.index == o.index

    def __ne__(self, o):
        return self.index != o.index

    def __lt__(self, o):
        return self.index < o.index

    def __le__(self, o):
        return self.index <= o.index

    def __gt__(self, o):
        return self.index > o.index

    def __ge__(self, o):
        return self.index >= o.index

    def get_interval(self, o):
        return INTERVALS[abs(self.index - o.index)]

    def __lshift__(self, o):
        return Note(PITCHES[(self.index - o) % N], self.is_long)

    def __rshift__(self, o):
        return Note(PITCHES[(self.index + o) % N], self.is_long)


d_notes = {'до': 'до-о', 'ре': 'ре-э', 'ми': 'ми-и', 'фа': 'фа-а', 'соль': 'со-оль', 'ля': 'ля-а',
           'си': 'си-и'}
N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
