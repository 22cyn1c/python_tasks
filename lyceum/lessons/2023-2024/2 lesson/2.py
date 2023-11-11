class Note:
    long_notes = 'до-о», «ре-э», «ми-и», «фа-а», «со-оль», «ля-а», «си-и'.split('», «')
    notes = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
    d_notes = dict(zip(notes, long_notes))

    def __init__(self, note, flag=False):
        if flag:
            self.note = Note.d_notes[note]
        else:
            self.note = note

    def play(self):
        print(self.note)

    def __str__(self):
        return self.note
