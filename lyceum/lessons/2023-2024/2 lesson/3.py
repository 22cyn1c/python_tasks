class Note:

    def __init__(self, note, is_long=False):
        d_notes = {'до': 'до-о', 'ре': 'ре-э', 'ми': 'ми-и', 'фа': 'фа-а', 'соль': 'со-оль',
                   'ля': 'ля-а', 'си': 'си-и'}
        if is_long:
            self.note = d_notes[note]
        else:
            self.note = note

    def play(self):
        print(self.note)

    def __str__(self):
        return self.note


class LoudNote(Note):
    def __str__(self):
        return self.note.upper()


class DefaultNote(Note):
    def __init__(self, note='до', is_long=False):
        super().__init__(note, is_long)


class NoteWithOctave(Note):
    def __init__(self, note, octave, is_long=False):
        super().__init__(note, is_long)
        self.octave = octave

    def __str__(self):
        return f'{self.note} ({self.octave})'


PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
